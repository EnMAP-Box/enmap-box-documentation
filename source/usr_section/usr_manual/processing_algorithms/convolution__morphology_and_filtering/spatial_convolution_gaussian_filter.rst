.. _Spatial convolution Gaussian filter:

***********************************
Spatial convolution Gaussian filter
***********************************

This 2D Gaussian filter applies a weighted average to the pixel values in the image. The weights are determined by a Gaussian distribution, which assigns higher weights to pixels closer to the center of the kernel and lower weights to pixels farther away. It is isotropic and does not produce artifacts. An exemplary kernel can be found below.

    .. figure:: ./img/gaussian_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/gaussian_filter_interface.png
       :align: center

3. View the processed image in comparison to the original.

    .. figure:: ./img/gaussian_filter_result.png
       :align: center


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `Gaussian2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.Gaussian2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import Gaussian2DKernel
        kernel = Gaussian2DKernel(x_stddev=1, y_stddev=1)

:guilabel:`Normalize kernel` [boolean]
    Whether to normalize the kernel to have a sum of one.

    Default: *False*


:guilabel:`Interpolate no data pixel` [boolean]
    Whether to interpolate no data pixel. Will result in renormalization of the kernel at each position ignoring pixels with `no data values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.

    Default: *True*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialConvolutionGaussianFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Gaussian2DKernel
    kernel = Gaussian2DKernel(x_stddev=1, y_stddev=1)
    	Argument type:	string
    	Acceptable values:
    		- String value
    normalize: Normalize kernel
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    interpolate: Interpolate no data pixel
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    