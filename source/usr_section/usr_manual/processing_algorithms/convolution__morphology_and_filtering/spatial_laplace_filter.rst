.. _Spatial Laplace filter:

**********************
Spatial Laplace filter
**********************

The Spatial Laplace filter enhances and detects edges or areas of rapid intensity changes in an image by convolving it with a Laplacian kernel. The Laplacian kernel is a matrix that represents the discrete approximation of the Laplace operator, which calculates the sum of the second partial derivatives of the image with respect to the x and y directions. By convolving the image with the Laplacian kernel, the filter highlights areas of significant intensity changes, such as edges or transitions between regions with different intensities. It amplifies these intensity variations by emphasizing high-frequency components in the image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/laplace_filter_interface.png
       :align: center

3. View the processed image in comparison to the original.

    .. figure:: ./img/laplace_filter_result.png
       :align: center



**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `laplace <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.laplace.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import laplace
        
        function = lambda array: laplace(array)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialLaplaceFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import laplace
    
    function = lambda array: laplace(array)
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
    
    