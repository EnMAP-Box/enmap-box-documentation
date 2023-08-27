.. _Spatial convolution Savitsky-Golay filter:

*****************************************
Spatial convolution Savitsky-Golay filter
*****************************************

2D Savitsky-Golay filter.
See `wikipedia <https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter#Two-dimensional_convolution_coefficients>`_ for details.

.. include:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/spatial_convolution_savitsky-golay_filter.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `sgolay2d <https://scipy-cookbook.readthedocs.io/items/SavitzkyGolay.html#Two-dimensional-data-smoothing-and-least-square-gradient-estimate>`_ from the SciPy cookbook for information on different parameters.

    Default::

        from astropy.convolution import Kernel2D
        from enmapboxprocessing.algorithm.spatialconvolutionsavitskygolay2dalgorithm import sgolay2d
        kernel = Kernel2D(array=sgolay2d(window_size=11, order=3, derivative=None))

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

``>qgis_process help enmapbox:SpatialConvolutionSavitskygolayFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Kernel2D
    from enmapboxprocessing.algorithm.spatialconvolutionsavitskygolay2dalgorithm import sgolay2d
    kernel = Kernel2D(array=sgolay2d(window_size=11, order=3, derivative=None))
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
    
    