from enmapbox.gui.enmapboxgui import EnMAPBox
from enmapbox.testing import initQgisApplication
from tut1_app1 import RegressionBasedUnmixingApp

if __name__ == '__main__':

    qgsApp = initQgisApplication()
    enmapBox = EnMAPBox(None)
    enmapBox.run()
    enmapBox.openExampleData(mapWindows=1)
    enmapBox.addApplication(RegressionBasedUnmixingApp(enmapBox=enmapBox))
    qgsApp.exec_()
    qgsApp.exitQgis()
