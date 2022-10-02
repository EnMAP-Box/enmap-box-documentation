import json

from enmapbox import initAll
from enmapbox.exampledata import enmap, landcover_point
from enmapbox.qgispluginsupport.qps.speclib import speclibSettings
from enmapbox.qgispluginsupport.qps.speclib.core.spectrallibrary import SpectralLibraryUtils
from enmapbox.qgispluginsupport.qps.speclib.gui.spectrallibrarywidget import SpectralLibraryWidget
from enmapbox.qgispluginsupport.qps.speclib.io.rastersources import RasterLayerSpectralLibraryIO, RASTER_FIELDS
from enmapbox.testing import start_app
from qgis.core import QgsVectorLayer, QgsApplication, QgsFields

app = start_app()
initAll()
lyrV = QgsVectorLayer(landcover_point, 'Landcover')

fields = QgsFields(RASTER_FIELDS)
for n in ['level_1', 'level_2']:
    fields.append(lyrV.fields().field(n))

importSettings = {'vector_layer': lyrV, 'fields': fields}
profiles = RasterLayerSpectralLibraryIO.importProfiles(enmap, importSettings=importSettings)
for i, p in enumerate(profiles):
    name = 'Profile {} ({},{})'.format(i + 1, p.attribute('px_x'), p.attribute('px_y'))
    p.setAttribute('name', name)
speclib = SpectralLibraryUtils.createSpectralLibrary()
speclib.startEditing()
SpectralLibraryUtils.addProfiles(speclib, profiles, addMissingFields=True)

slw = SpectralLibraryWidget(speclib=speclib)
slw.show()

if True:
    settings = speclibSettings()
    settings.setValue('SpectralProcessingDialog/algorithmId',
                      'enmapbox:SpectralResamplingToPrisma'
                      )
    parameters = dict()

    parameterJson = json.dumps(parameters)
    parameterJson = ''
    settings.setValue('SpectralProcessingDialog/algorithmParameters', '')
slw.actionShowSpectralProcessingDialog.trigger()

QgsApplication.exec_()
