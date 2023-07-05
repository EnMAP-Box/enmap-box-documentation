.. _Spatial Gaussian Gradient Magnitude filter:

******************************************
Spatial Gaussian Gradient Magnitude filter
******************************************

The Spatial Gaussian Gradient Magnitude filter computes the magnitude of the gradient of an image using Gaussian derivatives, providing a measure of the strength of the gradient at each pixel and helping to highlight edges and transitions in the image.. The filter operates by convolving the image with a pair of Gaussian derivative kernels—one for the x-direction and another for the y-direction. These kernels are derived from the Gaussian function and are used to estimate the image gradient in both the horizontal and vertical directions.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial Gaussian Gradient Magnitude filter`.

    .. figure:: ./img/ggrad_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/ggrad_filter_interface.png
       :align: center

4. Processed image in comparison to the original.

    .. figure:: ./img/ggrad_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: bD6X4Xc4114
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `gaussian_gradient_magnitude <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_gradient_magnitude.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import gaussian_gradient_magnitude
        
        function = lambda array: gaussian_gradient_magnitude(array, sigma=1)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialGaussianGradientMagnitudeFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import gaussian_gradient_magnitude
    
    function = lambda array: gaussian_gradient_magnitude(array, sigma=1)
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
    
    