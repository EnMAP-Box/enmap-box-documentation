.. _Spatial convolution Box filter:

******************************
Spatial convolution Box filter
******************************

2D Box filter.
The Spatial convolution Box filter is used to reduce noise and blur an image by averaging pixel values within a defined neighborhood, defined by a square kernel with equal weights. The size of the kernel determines the extent of the blurring effect. The filter is not isotropic and can produce artifact, when applied repeatedly to the same data.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution Box filter`.

    .. figure:: ./img/box_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/box_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/box_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: 4IIO9dqH3B4
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `Box2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.Box2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import Box2DKernel
        kernel = Box2DKernel(width=5)

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

``>qgis_process help enmapbox:SpatialConvolutionBoxFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Box2DKernel
    kernel = Box2DKernel(width=5)
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
    
    