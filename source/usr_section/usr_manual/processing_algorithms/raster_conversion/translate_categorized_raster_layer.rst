.. _Translate categorized raster layer:

**********************************
Translate categorized raster layer
**********************************

Translates `categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_ into target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.
Resampling is done via a two-step majority voting approach. First, the categorized `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ is resampled at x10 finer resolution, and subsequently aggregated back to the `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ resolution using majority voting. This approach leads to pixel-wise `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ decisions that are accurate to the percent.

.. include:: ../../processing_algorithms_includes/raster_conversion/translate_categorized_raster_layer.rst

**Parameters**


:guilabel:`Categorized raster layer` [raster]
    A `categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_ to be resampled.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Majority voting` [boolean]
    Whether to use majority voting. Turn off to use simple nearest neighbour resampling, which is much faster, but may result in highly inaccurate decisions.

    Default: *True*

**Outputs**


:guilabel:`Output categorized raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:TranslateCategorizedRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    categorizedRaster: Categorized raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    grid: Grid
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    majorityVoting: Majority voting
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputTranslatedCategorizedRaster: Output categorized raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputTranslatedCategorizedRaster: <outputRaster>
    	Output categorized raster layer
    
    