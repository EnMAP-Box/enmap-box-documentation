import enmapboxtestdata
from tut1_app1.core import regressionBasedUnmixing

regressionBasedUnmixing(filename='fraction.bsq',
                        rasterFilename=enmapboxtestdata.enmap,
                        vectorFilename=enmapboxtestdata.landcover_polygon,
                        classAttribute='level_3_id')

if True: # show the result in a viewer
    from _classic.hubdc.core import openRasterDataset, MapViewer
    rasterDataset = openRasterDataset(filename='fraction.bsq')
    MapViewer().addLayer(rasterDataset.mapLayer().initMultiBandColorRenderer(0, 3, 5, percent=0)).show()
