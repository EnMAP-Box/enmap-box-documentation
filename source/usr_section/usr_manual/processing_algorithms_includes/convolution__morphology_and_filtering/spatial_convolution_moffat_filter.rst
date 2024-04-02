When using a Moffat filter, the image is convolved with a kernel that approximates the Moffat distribution. The convolution operation involves multiplying each pixel in the image with the corresponding weight in the kernel and summing the results to determine the value of the convolved pixel. This kernel is a typical model for a seeing limited PSF. An exemplary kernel can be found below.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/ricker_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/moffat_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/moffat_filter_result.png
       :align: center