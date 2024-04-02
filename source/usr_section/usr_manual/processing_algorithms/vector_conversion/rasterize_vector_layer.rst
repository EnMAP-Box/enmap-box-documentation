.. _Rasterize vector layer:

**********************
Rasterize vector layer
**********************

Converts vector geometries (points, lines and polygons) into a raster `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.

.. include:: ../../processing_algorithms_includes/vector_conversion/rasterize_vector_layer.rst

**Parameters**


:guilabel:`Vector layer` [vector]
    A `vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ to be rasterized.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Init value` [number]
    Pre-initialization value for the output `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

    Default: *0*


:guilabel:`Burn value` [number]
    Fixed value to burn into each pixel, which is touched (point, line) or where the center is covered (polygon) by a geometry.

    Default: *1*


:guilabel:`Burn attribute` [field]
    Numeric vector `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ to use as burn values.


:guilabel:`Burn feature ID` [boolean]
    Whether to use the `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ ID as burn values. Initial value is set to -1. Data type is set to Int32.

    Default: *False*


:guilabel:`Add value` [boolean]
    Whether to add up existing values instead of replacing them.

    Default: *False*


:guilabel:`All touched` [boolean]
    Enables the ALL_TOUCHED rasterization option so that all pixels touched by lines or polygons will be updated, not just those on the line render path, or whose center point is within the polygon.

    Default: *False*


:guilabel:`Data type` [enum]
    Output data type.

    Default: *5*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:RasterizeVectorLayer``::

    ----------------
    Arguments
    ----------------
    
    vector: Vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    grid: Grid
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    initValue: Init value
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    burnValue: Burn value
    	Default value:	1
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    burnAttribute: Burn attribute (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    burnFid: Burn feature ID
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    addValue: Add value
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    allTouched: All touched
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataType: Data type
    	Default value:	5
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
    outputRasterizedVector: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRasterizedVector: <outputRaster>
    	Output raster layer
    
    