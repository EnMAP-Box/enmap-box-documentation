# 0
from _classic.hubdc.core import *
# 1
def regressionBasedUnmixing(filename, rasterFilename, vectorFilename, classAttribute,
                            oversampling=10, coverage=0.9, n_estimators=100):
    '''
    This function derives landcover pixel fractions from the given raster and vector maps,
    fits a random forest regressor to that dataset and applies it the the raster predicting
    (multi-band) landcover fractions and stores it at the given ``filename``.

    :param filename: output fraction raster filename
    :param rasterFilename: input raster filename
    :param vectorFilename: input vector filename
    :param classAttribute: attribute with class ids (values 1 to number of classes)
    :param oversampling: oversampling factor defines how accurate the landcover polygons
                         are aggregated into pixel fractions
    :param coverage: threshold between 0 and 1 that defines the minimal coverage a pixel
                     must have to be concidered as training sample.
    :param n_estimators: number of trees used for the random forest regressor
    '''

# 2
    #  open datasets
    raster = openRasterDataset(filename=rasterFilename)
    vector = openVectorDataset(filename=vectorFilename)
# 3
    # rasterize landcover polygons into classes (detailed resolution)
    grid = raster.grid()
    gridOversampled = Grid(extent=grid.extent(), resolution=grid.resolution() / oversampling)
    idRaster = vector.rasterize(grid=gridOversampled, burnAttribute=classAttribute, initValue=0)
    idArray = idRaster.array()
# 4a
    # aggregate classes into class cover fractions (target resolution)
    numberOfClasses = int(np.max(idArray))
    ysize, xsize = grid.shape()
    fractionArray = np.empty(shape=(numberOfClasses, ysize, xsize), dtype=np.float32)
# 4b
    for id in range(1, numberOfClasses+1):

        # create class occurrence mask
        maskArray = np.float32(idArray == id)
        maskRaster = RasterDataset.fromArray(array=maskArray, grid=gridOversampled)
# 4c
        # aggregate occurrences into fractions
        fractionRaster = maskRaster.translate(grid=grid, resampleAlg=gdal.GRA_Average)
        fractionArray[id-1] = fractionRaster.array()
# 5
    # calculate pixel coverage
    coverageArray = np.sum(fractionArray, axis=0)
# 6
    # draw all samples that satisfy the minimal coverage condition
    valid = coverageArray >= coverage
    profiles = raster.array()[:, valid]
    labels = fractionArray[:, valid]
# 7
    # fit a random forest regressor
    from sklearn.ensemble import RandomForestRegressor
    rfr = RandomForestRegressor(n_estimators=n_estimators)
    X = profiles.T
    y = labels.T
    rfr.fit(X=X, y=y)
# 8
    # predict fraction map
    array = raster.array()
    valid = array[0] != raster.noDataValues()[0]
    X = array[:, valid].reshape(raster.zsize(), -1).T
    y = rfr.predict(X=X)
    fractionArray = np.full(shape=(numberOfClasses, ysize, xsize), fill_value=-1., dtype=np.float32)
    fractionArray[:, valid] = y.T
# 9a
    # store as raster and set metadata
    driver = RasterDriver.fromFilename(filename=filename)
    fractionRaster = RasterDataset.fromArray(array=fractionArray, grid=grid, filename=filename, driver=driver)
    fractionRaster.setNoDataValue(value=-1)
# 9b
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
