The Spectral convolution Box filter is used to reduce noise by averaging reflectance values within a defined neighborhood, defined by a kernel with equal weights. The size of the kernel determines the extent of the averaging effect. The filter is not isotropic and can produce artifact, when applied repeatedly to the same data.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/spectral_box_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/img/spectral_box_filter_result.png
       :align: center