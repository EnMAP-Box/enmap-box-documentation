The Spatial convolution Box filter is used to reduce noise and blur an image by averaging pixel values within a defined neighborhood, defined by a square kernel with equal weights. The size of the kernel determines the extent of the blurring effect. The filter is not isotropic and can produce artifact, when applied repeatedly to the same data. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/box_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/box_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/box_filter_result.png
       :align: center