.. _Spatial convolution custom filter:

*********************************
Spatial convolution custom filter
*********************************

This filter allows to create a custom spatial 2D filter kernel from a list or an array.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution custom filter`.

    .. figure:: ./img/custom_filter_location.png
       :align: center

3. Select the raster to process and adjust the kernel weights in the command window, then click :guilabel:`run`.

    .. figure:: ./img/custom_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/custom_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: uJZTiigWfsc
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `CustomKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.CustomKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import CustomKernel
        array = [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]
        kernel = CustomKernel(array)

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

``>qgis_process help enmapbox:SpatialConvolutionCustomFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import CustomKernel
    array = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
    kernel = CustomKernel(array)
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
    
    