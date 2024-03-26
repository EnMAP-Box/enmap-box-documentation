.. _Spectral convolution Savitsky-Golay filter:

******************************************
Spectral convolution Savitsky-Golay filter
******************************************

1D Savitsky-Golay filter.
See `wikipedia <https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter>`_ for details.

.. include:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/spectral_convolution_savitsky-golay_filter.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `scipy.signal.savgol_coeffs <https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.savgol_coeffs.html#scipy-signal-savgol-coeffs>`_ for information on different parameters.

    Default::

        from astropy.convolution import Kernel1D
        from scipy.signal import savgol_coeffs
        kernel = Kernel1D(array=savgol_coeffs(window_length=11, polyorder=3, deriv=0))

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

``>qgis_process help enmapbox:SpectralConvolutionSavitskygolayFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Kernel1D
    from scipy.signal import savgol_coeffs
    kernel = Kernel1D(array=savgol_coeffs(window_length=11, polyorder=3, deriv=0))
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    normalize: Normalize kernel
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    interpolate: Interpolate no data pixel
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    