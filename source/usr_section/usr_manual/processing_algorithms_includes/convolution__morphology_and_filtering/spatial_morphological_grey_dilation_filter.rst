The filter operates by moving a structuring element, which is a predefined shape such as a square or a circle, across the image. The structuring element defines the neighborhood around each pixel that will be considered during the dilation operation.

For each pixel in the image, the grey dilation filter finds the maximum pixel value within the structuring element’s neighborhood and assigns this maximum value to the corresponding pixel in the output image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/dilation_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/dilation_filter_result.png
       :align: center