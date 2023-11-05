.. _Translate raster layer:

**********************
Translate raster layer
**********************

Convert raster data between different formats, potentially performing some operations like spatial subsetting, spatial resampling, reprojection, `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ subsetting, band reordering, data scaling, `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_ specification, and data type conversion.

.. include:: ../../processing_algorithms_includes/raster_conversion/translate_raster_layer.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    Source `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Selected bands` [band]
    Bands to subset and rearrange. An empty selection defaults to all `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in native order.


:guilabel:`Grid` [raster]
    The destination `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Copy metadata` [boolean]
    Whether to copy GDAL metadata from source to destination.

    Default: *True*


:guilabel:`Copy style` [boolean]
    Whether to copy style from source to destination.

    Default: *False*


:guilabel:`Exclude bad bands` [boolean]
    Whether to exclude `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_ (given by BBL metadata item inside ENVI domain). Also see The ENVI Header Format for more details: https://www.l3harrisgeospatial.com/docs/ENVIHeaderFiles.html

    Default: *False*


:guilabel:`Derive and exclude additional bad bands` [boolean]
    Whether to derive and exclude additional `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_ fully filled with inf, nan or `no data values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.

    Default: *False*


:guilabel:`Write ENVI header` [boolean]
    Whether to write an ENVI header *.hdr sidecar file with spectral metadata required for proper visualization in ENVI software.

    Default: *True*


:guilabel:`Spectral raster layer for band subsetting` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ used for specifying a `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ subset by matching the `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_.


:guilabel:`Selected spectral bands` [band]
    `Spectral bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-band>`_ used to match source raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.An empty selection defaults to all bands in native order.


:guilabel:`Data offset value` [number]
    A data offset value applied to each `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Data gain/scale value` [number]
    A data gain/scale value applied to each `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Spatial extent` [extent]
    Spatial extent for clipping the destination `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_, which is given by the source Raster or the selected Grid. In both cases, the extent is aligned with the actual pixel grid to avoid subpixel shifts.


:guilabel:`Column subset` [range]
    Column subset range in pixels to extract.


:guilabel:`Row subset` [range]
    Rows subset range in pixels to extract.


:guilabel:`Resample algorithm` [enum]
    Spatial resample algorithm.

    Default: *0*


:guilabel:`Source no data value` [number]
    The value to be used instead of the original `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.


:guilabel:`No data value` [number]
    The value to be used instead of the default destination `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.


:guilabel:`Unset source no data value` [boolean]
    Whether to unset (i.e. not use) the source `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.

    Default: *False*


:guilabel:`Unset no data value` [boolean]
    Whether to unset the destination `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.

    Default: *False*


:guilabel:`Working Data type` [enum]
    Working data type that is applied before resampling.


:guilabel:`Data type` [enum]
    Output data type.


:guilabel:`Output options` [string]
    Output format and creation options. The default format is GeoTiff with creation options: INTERLEAVE=BAND, COMPRESS=LZW, TILED=YES, BIGTIFF=YES

    Default: **

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:TranslateRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    bandList: Selected bands (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    grid: Grid (optional)
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
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    excludeBadBands: Exclude bad bands
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    excludeDerivedBadBands: Derive and exclude additional bad bands
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    writeEnviHeader: Write ENVI header
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    spectralSubset: Spectral raster layer for band subsetting (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    spectralBandList: Selected spectral bands (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    offset: Data offset value (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    scale: Data gain/scale value (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    extent: Spatial extent (optional)
    	Argument type:	extent
    	Acceptable values:
    		- A comma delimited string of x min, x max, y min, y max. E.g. '4,10,101,105'
    		- Path to a layer. The extent of the layer is used.
    sourceColumns: Column subset (optional)
    	Argument type:	range
    	Acceptable values:
    		- Two comma separated numeric values, e.g. '1,10'
    sourceRows: Row subset (optional)
    	Argument type:	range
    	Acceptable values:
    		- Two comma separated numeric values, e.g. '1,10'
    resampleAlg: Resample algorithm
    	Default value:	0
    	Argument type:	enum
    	Available values:
    		- 0: NearestNeighbour
    		- 1: Bilinear
    		- 2: Cubic
    		- 3: CubicSpline
    		- 4: Lanczos
    		- 5: Average
    		- 6: Mode
    		- 7: Min
    		- 8: Q1
    		- 9: Med
    		- 10: Q3
    		- 11: Max
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    sourceNoData: Source no data value (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    noData: No data value (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    unsetSourceNoData: Unset source no data value
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    unsetNoData: Unset no data value
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    workingType: Working Data type (optional)
    	Argument type:	enum
    	Available values:
    		- 0: Byte
    		- 1: Int16
    		- 2: UInt16
    		- 3: UInt32
    		- 4: Int32
    		- 5: Float32
    		- 6: Float64
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    dataType: Data type (optional)
    	Argument type:	enum
    	Available values:
    		- 0: Byte
    		- 1: Int16
    		- 2: UInt16
    		- 3: UInt32
    		- 4: Int32
    		- 5: Float32
    		- 6: Float64
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    creationProfile: Output options (optional)
    	Default value:	
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputTranslatedRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputTranslatedRaster: <outputRaster>
    	Output raster layer
    
    