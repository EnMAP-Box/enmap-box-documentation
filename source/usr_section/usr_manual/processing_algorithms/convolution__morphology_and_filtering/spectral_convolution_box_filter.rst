.. _Spectral convolution Box filter:

*******************************
Spectral convolution Box filter
*******************************

The Spectral convolution Box filter is used to reduce noise by averaging values within a defined neighborhood, defined by a window with equal weights. The size of the window determines the extent of the blurring effect. The filter is not isotropic and can produce artifact, when applied repeatedly to the same data.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.
    .. figure::
       :align: center

3. View the processed image in comparison to the original.

    .. figure::
       :align: center


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `Box1DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.Box1DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import Box1DKernel
        kernel = Box1DKernel(width=5)

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

``>qgis_process help enmapbox:SpectralConvolutionBoxFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import Box1DKernel
    kernel = Box1DKernel(width=5)
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
    
    