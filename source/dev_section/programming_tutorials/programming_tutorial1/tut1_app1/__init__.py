from enmapbox.gui.applications import EnMAPBoxApplication
from tut1_app1.processingalgorithm import RegressionBasedUnmixingProcessingAlgorithm

def enmapboxApplicationFactory(enmapBox):
    return [RegressionBasedUnmixingApp(enmapBox)]

class RegressionBasedUnmixingApp(EnMAPBoxApplication):
    def __init__(self, enmapBox, parent=None):
        super().__init__(enmapBox, parent=parent)

        self.name = 'Regression-based Unmixing Application'
        self.version = 'dev'
        self.licence = 'GNU GPL-3'

    def processingAlgorithms(self):
        return [RegressionBasedUnmixingProcessingAlgorithm()]
