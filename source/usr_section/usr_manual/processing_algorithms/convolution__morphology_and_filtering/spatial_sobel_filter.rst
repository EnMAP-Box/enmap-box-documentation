.. _Spatial Sobel filter:

********************
Spatial Sobel filter
********************

Spatial Sobel filter. See `Wikipedia <https://en.wikipedia.org/wiki/Sobel_operator>`_ for general information.

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `sobel <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.sobel.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import sobel
        
        function = lambda array: sobel(array, axis=0)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialSobelFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import sobel
    
    function = lambda array: sobel(array, axis=0)
    	Argument type:	string
    	Acceptable values:
    		- String value
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    