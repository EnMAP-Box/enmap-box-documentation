.. _Class fraction layer from categorized vector layer:

**************************************************
Class fraction layer from categorized vector layer
**************************************************

Rasterize a `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ into `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ fractions. `Categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ are rasterized at a x10 finer resolution and aggregated to class-wise fractions at destination resolution. This approach leads to fractions that are accurate to the percent.

**Parameters**


:guilabel:`Categorized vector layer` [vector]
    A `categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ to be rasterized.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.

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
    outputFraction: Output class fraction layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputFraction: <outputRaster>
    	Output class fraction layer
    
    