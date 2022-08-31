.. _Apply mask layer to raster layer:

********************************
Apply mask layer to raster layer
********************************

Areas where the `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_ evaluates to false are set to the source `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_ (0, if undefined).

**Parameters**


:guilabel:`Raster layer` [raster]
    Source `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Mask layer` [layer]
    A `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ApplyMaskLayerToRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    mask: Mask layer
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    