.. _Raster layer bounding polygon:

*****************************
Raster layer bounding polygon
*****************************

Compute `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ bounding polygon that encloses all data pixel.

**Parameters**


:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for bounding polygon calculation.

**Outputs**


:guilabel:`Output vector layer` [vectorDestination]
    Vector file destination.

**Command-line usage**

``>qgis_process help enmapbox:RasterLayerBoundingPolygon``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputVector: Output vector layer
    	Argument type:	vectorDestination
    	Acceptable values:
    		- Path for new vector layer
    
    ----------------
    Outputs
    ----------------
    
    outputVector: <outputVector>
    	Output vector layer
    
    