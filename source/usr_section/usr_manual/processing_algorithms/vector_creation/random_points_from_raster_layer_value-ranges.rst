.. _Random points from raster layer value-ranges:

********************************************
Random points from raster layer value-ranges
********************************************

This algorithm creates a new `point layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-point-layer>`_ with a given number of random points, all of them within specified value-ranges of the given raster `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.

**Parameters**


:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Band` [band]
    The `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ to draw points from. If not selected, the first renderer band is used.


:guilabel:`Number of points per value-range` [matrix]
    Number of points N to draw from value-range Minimum to Maximum.Value-ranges can be specified by actual values (e.g. 42) or by percentiles (e.g. p0, p50, p100, etc.).


:guilabel:`Range boundaries` [enum]
    The boundary type used for all value-ranges.

    Default: *0*


:guilabel:`Minimum distance between points (in meters)` [number]
    A minimum (Euclidean) distance between points can be specified.

    Default: *0*


:guilabel:`Minimum distance between points inside category (in meters)` [number]
    A minimum (Euclidean) distance between points in a value-range can be specified.

    Default: *0*


:guilabel:`Random seed` [number]
    The seed for the random generator can be provided.

**Outputs**


:guilabel:`Output point layer` [vectorDestination]
    Vector file destination.

**Command-line usage**

``>qgis_process help enmapbox:RandomPointsFromRasterLayerValueranges``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    band: Band (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    n: Number of points per value-range
    	Argument type:	matrix
    	Acceptable values:
    		- A comma delimited list of values
    boundaries: Range boundaries
    	Default value:	0
    	Argument type:	enum
    	Available values:
    		- 0: min < value <= max
    		- 1: min <= value < max
    		- 2: min <= value <= max
    		- 3: min < value < max
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    distanceGlobal: Minimum distance between points (in meters)
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    distanceStatum: Minimum distance between points inside category (in meters)
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    seed: Random seed (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputPoints: Output point layer
    	Argument type:	vectorDestination
    	Acceptable values:
    		- Path for new vector layer
    
    ----------------
    Outputs
    ----------------
    
    outputPoints: <outputVector>
    	Output point layer
    
    