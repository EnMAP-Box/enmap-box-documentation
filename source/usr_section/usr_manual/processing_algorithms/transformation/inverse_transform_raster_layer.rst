.. _Inverse transform raster layer:

******************************
Inverse transform raster layer
******************************

Uses a fitted `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_ to inverse transform a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    The `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be inverse transformed.


:guilabel:`Transformer` [file]
    A fitted `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:InverseTransformRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    transformer: Transformer
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    