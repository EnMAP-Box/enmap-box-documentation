.. _Spatial Prewitt filter:

**********************
Spatial Prewitt filter
**********************

The Prewitt filter calculates the gradient of an image by approximating the derivative of the image intensity with respect to the spatial coordinates. It specifically focuses on detecting vertical and horizontal edges in an image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/perwitt_filter_interface.png
       :align: center

3. View the processed image in comparison to the original.

    .. figure:: ./img/perwitt_filter_result.png
       :align: center


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `prewitt <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.prewitt.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import prewitt
        
        function = lambda array: prewitt(array, axis=0)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialPrewittFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import prewitt
    
    function = lambda array: prewitt(array, axis=0)
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
    
    