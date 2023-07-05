.. _Spatial convolution Top-Hat filter:

**********************************
Spatial convolution Top-Hat filter
**********************************

2D Top-Hat filter.
The top hat filter is designed to enhance or extract small, bright regions or structures in an image that are significantly smaller than the size of the filter's structuring element. It is particularly useful for detecting localized objects or features against a relatively uniform background. It is an isotropic smoothing filter. It can produce artifacts when applied repeatedly on the same data.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution Top-Hat filter`.

    .. figure:: ./img/tophat_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/tophat_filter_interface.png
       :align: center

4. Processed image in comparison to the original.

    .. figure:: ./img/tophat_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: DZeo3Ble-Is
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `Tophat2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.Tophat2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import Tophat2DKernel
        kernel = Tophat2DKernel(radius=1)

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

``>qgis_process help enmapbox:SpatialConvolutionTophatFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Tophat2DKernel
    kernel = Tophat2DKernel(radius=1)
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
    
    