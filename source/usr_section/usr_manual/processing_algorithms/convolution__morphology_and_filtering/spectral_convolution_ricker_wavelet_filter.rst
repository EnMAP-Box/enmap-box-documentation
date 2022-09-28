.. _Spectral convolution Ricker Wavelet filter:

******************************************
Spectral convolution Ricker Wavelet filter
******************************************

1D Ricker Wavelet filter kernel (sometimes known as a Mexican Hat kernel).
The Ricker Wavelet, or inverted Gaussian-Laplace filter, is a bandpass filter. It smooths the data and removes slowly varying or constant structures (e.g. background). It is useful for peak or multi-scale detection.

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `RickerWavelet1DKernel <https://docs.astropy.org/en/stable/en/stable/api/astropy.convolution.RickerWavelet1DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import RickerWavelet1DKernel
        kernel = RickerWavelet1DKernel(width=1)

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

``>qgis_process help enmapbox:SpectralConvolutionRickerWaveletFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import RickerWavelet1DKernel
    kernel = RickerWavelet1DKernel(width=1)
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
    
    