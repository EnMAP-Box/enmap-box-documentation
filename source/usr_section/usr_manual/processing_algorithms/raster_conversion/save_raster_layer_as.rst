.. _Save raster layer as:

********************
Save raster layer as
********************

Saves a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ as a GeoTiff, ENVI or VRT file. This is a slimmed down version of the more powerful "Translate raster `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_" algorithm.

**Parameters**


:guilabel:`Raster layer` [raster]
    Source `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Copy metadata` [boolean]
    Whether to copy metadata from source to destination.

    Default: *True*


:guilabel:`Copy style` [boolean]
    Whether to copy style from source to destination.

    Default: *True*


:guilabel:`Output options` [string]
    Output format and creation options. The default format is GeoTiff with creation options: INTERLEAVE=BAND, COMPRESS=LZW, TILED=YES, BIGTIFF=YES

    Default: **

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SaveRasterLayerAs``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    copyMetadata: Copy metadata
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    copyStyle: Copy style
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    creationProfile: Output options (optional)
    	Default value:	
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    