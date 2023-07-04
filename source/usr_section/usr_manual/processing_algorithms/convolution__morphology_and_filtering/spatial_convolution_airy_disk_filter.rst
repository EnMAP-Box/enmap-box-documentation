.. _Spatial convolution Airy Disk filter:

************************************
Spatial convolution Airy Disk filter
************************************

2D Airy Disk filter.
 The Airy Disk filter convolves an image with a kernel that approximates the intensity distribution of an Airy disk. The filter enhances the edges and fine details in an image, mimicking the diffraction pattern produced by a circular aperture. This kernel models the diffraction pattern of a circular aperture. The kernel is normalized to a peak value of 1

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.


    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial convolution Airy Disk filter`.

    .. figure:: ./img/select_airy_filter.png
       :align: center

3. Select the raster to process, then click :guilabel:`run`.

    .. figure:: ./img/interface_airy_filter.png
       :align: center

4. Processed image in comparison to the original.

    .. figure:: ./img/result_airy_filter.png
       :align: center

Live demonstration
    ..  youtube:: b_0k3MRt0DQ
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be filtered.


:guilabel:`Kernel` [string]
    Python code. See `AiryDisk2DKernel <http://docs.astropy.org/en/stable/api/astropy.convolution.AiryDisk2DKernel.html>`_ for information on different parameters.

    Default::

        from astropy.convolution import AiryDisk2DKernel
        kernel = AiryDisk2DKernel(radius=1)

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

``>qgis_process help enmapbox:SpatialConvolutionAiryDiskFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    kernel: Kernel
    	Default value:	from astropy.convolution import AiryDisk2DKernel
    kernel = AiryDisk2DKernel(radius=1)
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
    
    