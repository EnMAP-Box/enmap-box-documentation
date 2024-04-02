.. _Layer to mask raster layer :

***************************
Layer to mask raster layer 
***************************

Interprete a `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ as a `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_.

.. include:: ../../processing_algorithms_includes/masking/layer_to_mask_raster_layer_.rst

**Parameters**


:guilabel:`Layer` [layer]
    A `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ to be interpreted as a `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_.


:guilabel:`Grid` [raster]
    The target `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_. Can be skipped if the source `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

**Outputs**


:guilabel:`Output mask raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:LayerToMaskRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Layer
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    grid: Grid (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputMask: Output mask raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputMask: <outputRaster>
    	Output mask raster layer
    
    