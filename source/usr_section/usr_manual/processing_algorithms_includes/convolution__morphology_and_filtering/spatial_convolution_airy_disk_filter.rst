The Airy Disk filter convolves an image with a kernel that approximates the intensity distribution of an Airy disk. The filter enhances the edges and fine details in an image, mimicking the diffraction pattern produced by a circular aperture. The kernel models the diffraction pattern of a circular aperture. The kernel is normalized to a peak value of 1. An exemplary kernel can be found below.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/airy_disk_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/interface_airy_filter.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/result_airy_filter.png
       :align: center
