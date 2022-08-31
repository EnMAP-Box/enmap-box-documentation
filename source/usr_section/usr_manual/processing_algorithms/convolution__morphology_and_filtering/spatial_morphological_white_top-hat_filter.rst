.. _Spatial morphological White Top-Hat filter:

******************************************
Spatial morphological White Top-Hat filter
******************************************

Spatial morphological White Top-Hat filter. See `Wikipedia <https://en.wikipedia.org/wiki/Top-hat_transform>`_ for general information.

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `scipy.ndimage.white_tophat <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.white_tophat.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import white_tophat
        
        function = lambda array: white_tophat(array, size=(3, 3))
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalWhiteTophatFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import white_tophat
    
    function = lambda array: white_tophat(array, size=(3, 3))
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
    
    