.. _Spatial convolution ring filter:

*******************************
Spatial convolution ring filter
*******************************

2D Ring filter.
The Ring filter kernel is the difference between two Top-Hat kernels of different width. This kernel is useful for, e.g., background estimation. It can further be used to extract circular or ring-shaped patterns in the image. It achieves this by assigning higher weights to the pixels located closer to the center of the kernel and lower weights to those farther away. This weighting scheme helps to enhance the circular or ring-like structures and suppress other image components.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution ring filter`.

    .. figure:: ./img/ring_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/ring_filter_interface.png
       :align: center

4. Processed image in comparison to the original.

    .. figure:: ./img/ring_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: BxZ4zu3a9Jw
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `Ring2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.Ring2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import Ring2DKernel
        kernel = Ring2DKernel(radius_in=3, width=2)

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

``>qgis_process help enmapbox:SpatialConvolutionRingFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Ring2DKernel
    kernel = Ring2DKernel(radius_in=3, width=2)
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
    
    