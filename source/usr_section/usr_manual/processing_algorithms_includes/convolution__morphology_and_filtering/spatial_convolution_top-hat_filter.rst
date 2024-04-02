The top hat filter is designed to enhance or extract small, bright regions or structures in an image that are significantly smaller than the size of the filter’s structuring element. It is particularly useful for detecting localized objects or features against a relatively uniform background. It is an isotropic smoothing filter. It can produce artifacts when applied repeatedly on the same data. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/tophat_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/tophat_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/tophat_filter_result.png
       :align: center