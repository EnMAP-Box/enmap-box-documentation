.. _Import PRISMA L1 product:

************************
Import PRISMA L1 product
************************

Import PRISMA L1 product from HE5 file to QGIS/GDAL conform GTiff/VRT file format.Note that for the spectral cube and error matrix, the interleave is transposed and stored as GTiff to enable proper visualization in QGIS.All other sub-`datasets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ are stored as light-weight VRT files.
For further details visit the `PRISMA Documentation Area <http://prisma.asi.it/missionselect/docs.php>`_.

**Parameters**


:guilabel:`File` [file]
    The HE5 product file.
    The main data contained in the PRS_L1_HRC Swath is the Radiometric Calibrated Coregistersed Hyperspectral Cube. All `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ of VNIR Cube and all bands of SWIR Cube are keystone corrected with respect to VNIR Cube `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ 128 only considering shift Across track.
    The PRS_L1_PCO Swath basically contains the Radiometric Calibrated Coregistered Panchromatic Image. The PAN Cube is coregistered with respect to VNIR Cube taking into account of the Along Track coregistration. PAN Cube also takes into account the Across track offset PAN – VNIR. All pixel of PAN Cube are keystone corrected with respect to VNIR Cube band 128 only considering shift Across track.
    Instead of executing this algorithm, you may drag&drop the HE5 file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.


:guilabel:`Spectral region` [enum]
    Spectral region to be imported.

    Default: *0*

**Outputs**


:guilabel:`Output VNIR/SWIR Cube raster layer` [rasterDestination]
    VNIR/SWIR Cube GTiff raster file destination.


:guilabel:`Output PAN raster layer` [rasterDestination]
    PAN VRT raster file destination.


:guilabel:`Output Cloud Mask raster layer` [rasterDestination]
    Cloud Mask VRT raster file destination.


:guilabel:`Output Land Cover Mask raster layer` [rasterDestination]
    Land Cover Mask VRT raster file destination.


:guilabel:`Output Sun Glint Mask raster layer` [rasterDestination]
    Sun Glint Mask VRT raster file destination.


:guilabel:`Output VNIR/SWIR Error Matrix raster layer` [rasterDestination]
    VNIR/SWIR Pixel Error Matrix GTiff raster file destination.


:guilabel:`Output VNIR/SWIR Geolocation Fields raster layer` [rasterDestination]
    VNIR/SWIR Geolocation `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ VRT raster file destination. Includes Latitude and Longitude `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Output PAN Geolocation Fields raster layer` [rasterDestination]
    PAN Geolocation `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ VRT raster file destination. Includes Latitude and Longitude `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Output PAN Error Matrix raster layer` [rasterDestination]
    PAN Pixel Error Matrix VRT raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportPrismaL1Product``::

    ----------------
    Arguments
    ----------------
    
    file: File
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    spectralRegion: Spectral region
    	Default value:	0
    	Argument type:	enum
    	Available values:
    		- 0: VNIR/SWIR combined
    		- 1: VNIR only
    		- 2: SWIR only
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    outputPrismaL1_spectralCube: Output VNIR/SWIR Cube raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_panCube: Output PAN raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_cloudMask: Output Cloud Mask raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_landCoverMask: Output Land Cover Mask raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_sunGlintMask: Output Sun Glint Mask raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrisma1_spectralErrorMatrix: Output VNIR/SWIR Error Matrix raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_spectralGeolocationFields: Output VNIR/SWIR Geolocation Fields raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_panGeolocationFields: Output PAN Geolocation Fields raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPrismaL1_panErrorMatrix: Output PAN Error Matrix raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputPrismaL1_spectralCube: <outputRaster>
    	Output VNIR/SWIR Cube raster layer
    outputPrismaL1_panCube: <outputRaster>
    	Output PAN raster layer
    outputPrismaL1_cloudMask: <outputRaster>
    	Output Cloud Mask raster layer
    outputPrismaL1_landCoverMask: <outputRaster>
    	Output Land Cover Mask raster layer
    outputPrismaL1_sunGlintMask: <outputRaster>
    	Output Sun Glint Mask raster layer
    outputPrisma1_spectralErrorMatrix: <outputRaster>
    	Output VNIR/SWIR Error Matrix raster layer
    outputPrismaL1_spectralGeolocationFields: <outputRaster>
    	Output VNIR/SWIR Geolocation Fields raster layer
    outputPrismaL1_panGeolocationFields: <outputRaster>
    	Output PAN Geolocation Fields raster layer
    outputPrismaL1_panErrorMatrix: <outputRaster>
    	Output PAN Error Matrix raster layer
    
    