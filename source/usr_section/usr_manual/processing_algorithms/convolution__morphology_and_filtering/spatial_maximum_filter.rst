.. _Spatial Maximum filter:

**********************
Spatial Maximum filter
**********************

Spatial Maximum filter.

The filter operates by moving a window or kernel across the image and replacing the pixel within the window with the maximum pixel value found within that window. The size of the window determines the extent of the filter's effect on the image.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial Maximum filter`.

    .. figure:: ./img/max_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/max_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/max_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: FZJBUqzvsAE
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `maximum_filter <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.maximum_filter.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import maximum_filter
        
        function = lambda array: maximum_filter(array, size=3)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMaximumFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import maximum_filter
    
    function = lambda array: maximum_filter(array, size=3)
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
    
    