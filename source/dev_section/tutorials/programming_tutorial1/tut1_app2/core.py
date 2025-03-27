from _classic.hubdc.core import *

def regressionBasedUnmixing(filename, rasterFilename, vectorFilename, classAttribute,
                            oversampling=10, coverage=0.9, n_estimators=100,
                            blockSize=256):
    #  open datasets
    raster = openRasterDataset(filename=rasterFilename)
    vector = openVectorDataset(filename=vectorFilename)

    numberOfClasses = int(np.max([feature.value(attribute=classAttribute) for feature in vector.features()]))

    profiles = list()
    labels = list()
    for subgrid, i, iy, ix in raster.grid().subgrids(size=blockSize):

        # rasterize landcover polygons into classes (detailed resolution)
        gridOversampled = Grid(extent=subgrid.extent(), resolution=subgrid.resolution() / oversampling)
        idRaster = vector.rasterize(grid=gridOversampled, burnAttribute=classAttribute, initValue=0)
        idArray = idRaster.array()

        # aggregate classes into class cover fractions (target resolution)
        ysize, xsize = subgrid.shape()
        fractionArray = np.empty(shape=(numberOfClasses, ysize, xsize), dtype=np.float32)

        for id in range(1, numberOfClasses+1):

            # create class occurrence mask
            maskArray = np.float32(idArray == id)
            maskRaster = RasterDataset.fromArray(array=maskArray, grid=gridOversampled)

            # aggregate occurrences into fractions
            fractionRaster = maskRaster.translate(grid=subgrid, resampleAlg=gdal.GRA_Average)
            fractionArray[id-1] = fractionRaster.array()

        # calculate pixel coverage
        coverageArray = np.sum(fractionArray, axis=0)

        # draw all samples that satisfy the minimal coverage condition
        valid = coverageArray >= coverage
        profiles.append(raster.array(grid=subgrid)[:, valid])
        labels.append(fractionArray[:, valid])

    # stack subgrid results togethter
    profiles = np.hstack(profiles)
    labels = np.hstack(labels)

    # fit a random forest regressor
    from sklearn.ensemble import RandomForestRegressor
    rfr = RandomForestRegressor(n_estimators=n_estimators)
    X = profiles.T
    y = labels.T
    rfr.fit(X=X, y=y)

    # init result fraction raster
    driver = RasterDriver.fromFilename(filename=filename)
    fractionRaster = driver.create(grid=raster.grid(), bands=numberOfClasses, filename=filename)

    for subgrid, i, iy, ix in raster.grid().subgrids(size=blockSize):

        # predict subgrid fractions
        array = raster.array(grid=subgrid)
        valid = array[0] != raster.noDataValues()[0]
        X = array[:, valid].reshape(raster.zsize(), -1).T
        y = rfr.predict(X=X)
        ysize, xsize = subgrid.shape()
        fractionArray = np.full(shape=(numberOfClasses, ysize, xsize), fill_value=-1., dtype=np.float32)
        fractionArray[:, valid] = y.T

        # write subgrid fractions
        fractionRaster.writeArray(array=fractionArray, grid=subgrid)

    # set metadata
    fractionRaster.setNoDataValue(value=-1)

    # - get class names from attribute definition file (i.e. *.json)
    jsonFilename = join(dirname(vectorFilename), '{}.json'.format(splitext(basename(vectorFilename))[0]))
    if exists(jsonFilename):
        import json
        with open(jsonFilename) as file:
            attributeDefinition = json.load(file)
        for id, name, color in attributeDefinition[classAttribute]['categories']:
            if id == 0:
                continue # skip 'unclassified' class
            fractionRaster.band(index=id-1).setDescription(value=name)
