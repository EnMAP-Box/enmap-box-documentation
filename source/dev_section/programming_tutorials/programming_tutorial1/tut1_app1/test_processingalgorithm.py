from os.path import join, dirname
from qgis.core import QgsProcessingFeedback, QgsApplication
from processing.core.Processing import Processing
from tut1_app1.processingalgorithm import RegressionBasedUnmixingProcessingAlgorithm
import enmapboxtestdata

# init QGIS
qgsApp = QgsApplication([], True)
qgsApp.initQgis()
qgsApp.messageLog().messageReceived.connect(lambda *args: print(args[0]))

# init processing framework
Processing.initialize()

# run algorithm
alg = RegressionBasedUnmixingProcessingAlgorithm()
io = {alg.P_RASTER: enmapboxtestdata.enmap,
      alg.P_VECTOR: enmapboxtestdata.landcover_polygon,
      alg.P_FIELD: 'level_2_id',
      alg.P_COVERAGE: 0.9,
      alg.P_OVERSAMPLING: 10,
      alg.P_OUTPUT_FRACTION: join(dirname(__file__), 'fraction.bsq')}
result = Processing.runAlgorithm(alg, parameters=io)

print(result)

if True: # show the result in a viewer
    from _classic.hubdc.core import MapViewer, openRasterDataset
    fraction = openRasterDataset(filename=result[alg.P_OUTPUT_FRACTION])
    MapViewer().addLayer(fraction.mapLayer().initMultiBandColorRenderer(0, 2, 4, percent=0)).show()
