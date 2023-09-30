.. _Class fraction layer from categorized vector layer:

**************************************************
Class fraction layer from categorized vector layer
**************************************************

Rasterize a `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ into `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ fractions. `Categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ are rasterized at a x10 finer resolution and aggregated to class-wise fractions at destination resolution. This approach leads to fractions that are accurate to the percent.

.. include:: ../../processing_algorithms_includes/classification/class_fraction_layer_from_categorized_vector_layer.rst

**Parameters**


:guilabel:`Categorized vector layer` [vector]
    A `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ to be rasterized.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Minimum pixel coverage [%]` [number]
    Exclude all pixel where (polygon) coverage is smaller than given threshold.

    Default: *0*

**Outputs**


:guilabel:`Output class fraction layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassFractionLayerFromCategorizedVectorLayer``::

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
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputFraction: Output class fraction layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputFraction: <outputRaster>
    	Output class fraction layer
    
    