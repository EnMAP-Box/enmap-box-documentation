.. _Rasterize categorized vector layer:

**********************************
Rasterize categorized vector layer
**********************************

Rasterize a `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ into a `categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_. Output `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ names and `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ are given by the source `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_.
Resampling is done via a two-step majority voting approach. First, the categorized `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ is resampled at x10 finer resolution, and subsequently aggregated back to the `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ resolution using majority voting. This approach leads to pixel-wise `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ decisions that are accurate to the percent.

.. include:: ../../processing_algorithms_includes/vector_conversion/rasterize_categorized_vector_layer.rst


**Parameters**


:guilabel:`Categorized vector layer` [vector]
    A `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ to be rasterized.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Minimum pixel coverage [%]` [number]
    Exclude all pixel where (polygon) coverage is smaller than given threshold.

    Default: *50*


:guilabel:`Majority voting` [boolean]
    Whether to use majority voting. Turn off to use simple nearest neighbour resampling, which is much faster, but may result in highly inaccurate `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ decisions.

    Default: *True*

**Outputs**


:guilabel:`Output categorized raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:RasterizeCategorizedVectorLayer``::

    ----------------
    Arguments
    ----------------
    
    categorizedVector: Categorized vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    grid: Grid
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    coverage: Minimum pixel coverage [%]
    	Default value:	50
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    majorityVoting: Majority voting
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRasterizedCategories: Output categorized raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRasterizedCategories: <outputRaster>
    	Output categorized raster layer
    
    