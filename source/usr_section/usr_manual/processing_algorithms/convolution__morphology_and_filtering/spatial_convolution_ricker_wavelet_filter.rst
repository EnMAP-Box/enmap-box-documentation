.. _Spatial convolution Ricker Wavelet filter:

*****************************************
Spatial convolution Ricker Wavelet filter
*****************************************

The Ricker wavelet filter convolves an image with a kernel that approximates the Ricker wavelet, which  is a bell-shaped waveform that resembles a symmetrically shaped hat or a Mexican hat. The Ricker wavelet filter is typically used for detecting and enhancing specific features or structures in an image. It is particularly effective in detecting edges, lines, or other localized patterns with a characteristic scale. The central peak of the Ricker wavelet helps to emphasize these features, while the positive and negative lobes contribute to enhancing the contrast and edges, which smooths the data and removes slowly varying or constant structures (e.g. background). It is useful for peak or multi-scale detection.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution Ricker Wavelet filter`.

    .. figure:: ./img/ricker_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/ricker_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/ricker_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: 9z_IP5DHKvE
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `RickerWavelet2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.RickerWavelet2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import RickerWavelet2DKernel
        kernel = RickerWavelet2DKernel(width=1)

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

``>qgis_process help enmapbox:SpatialConvolutionRickerWaveletFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import RickerWavelet2DKernel
    kernel = RickerWavelet2DKernel(width=1)
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
    
    