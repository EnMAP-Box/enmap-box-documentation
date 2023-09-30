.. _Classification layer from rendered image:

****************************************
Classification layer from rendered image
****************************************

Creates `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from a rendered image. Classes are derived from the unique renderer RGBA values.

**Parameters**


:guilabel:`Raster layer` [raster]
    The `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be classified.

**Outputs**


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassificationLayerFromRenderedImage``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputClassification: Output classification layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputClassification: <outputRaster>
    	Output classification layer
    
    