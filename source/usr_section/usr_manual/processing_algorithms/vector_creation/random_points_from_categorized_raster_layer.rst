.. _Random points from categorized raster layer:

*******************************************
Random points from categorized raster layer
*******************************************

This algorithm creates a new `point layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-point-layer>`_ with a given number of random points, all of them within the `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ of the given `categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_.

.. include:: ../../processing_algorithms_includes/vector_creation/random_points_from_categorized_raster_layer.rst

**Parameters**


:guilabel:`Categorized raster layer` [raster]
    A `categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_ to draw points from.


:guilabel:`Number of points per category` [string]
    Number of points to draw from each `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_. Set a single value N to draw N points for each category. Set a list of values N1, N2, ... Ni, ... to draw Ni points for category i.


:guilabel:`Minimum distance between points (in meters)` [number]
    A minimum (Euclidean) distance between points can be specified.

    Default: *0*


:guilabel:`Minimum distance between points inside category (in meters)` [number]
    A minimum (Euclidean) distance between points in a `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ can be specified.

    Default: *0*


:guilabel:`Random seed` [number]
    The seed for the random generator can be provided.

**Outputs**


:guilabel:`Output point layer` [vectorDestination]
    Vector file destination.

**Command-line usage**

``>qgis_process help enmapbox:RandomPointsFromCategorizedRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    stratification: Categorized raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    n: Number of points per category
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
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
    
    