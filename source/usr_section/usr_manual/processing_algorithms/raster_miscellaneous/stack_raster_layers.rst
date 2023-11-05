.. _Stack raster layers:

*******************
Stack raster layers
*******************

Stack `raster layers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ and store the result as a VRT file.This is a slimmed down version of the more powerful/complicated GDAL "Build virtual raster" algorithm.
If you also want to delete or rearrange individual `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_, just use the "Subset `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ bands" algorithm afterwards.

.. include:: ../../processing_algorithms_includes/raster_miscellaneous/stack_raster_layers.rst


**Parameters**


:guilabel:`Raster layers` [multilayer]
    Source `raster layers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Grid` [raster]
    Reference `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_ specifying the destination extent, pixel size and projection. If not defined, gdal.BuildVrt defaults are used.


:guilabel:`Band` [number]
    Specify a `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ number used for stacking, instead of using all `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:StackRasterLayers``::

    ----------------
    Arguments
    ----------------
    
    rasters: Raster layers
    	Argument type:	multilayer
    grid: Grid (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    band: Band (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
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
    
    