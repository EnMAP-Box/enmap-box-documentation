from enmapbox.gui.enmapboxgui import EnMAPBox
from enmapbox.testing import initQgisApplication

if __name__ == '__main__':

    qgsApp = initQgisApplication()
    enmapBox = EnMAPBox(None)
    enmapBox.run()
    qgsApp.exec_()
    qgsApp.exitQgis()
