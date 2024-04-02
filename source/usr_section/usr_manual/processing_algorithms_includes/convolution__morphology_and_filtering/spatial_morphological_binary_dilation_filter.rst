The spatial morphological binary dilation filter expands or dilates regions of foreground or 1 pixels in a binary image. It is used for tasks such as noise removal, boundary enhancement, and image segmentation, providing a way to fill gaps, smooth out regions, and connect adjacent pixels or objects.

The filter operates by moving a structuring element across the image. The structuring element defines the neighborhood around each pixel that will be considered during the dilation operation.

For each pixel in the image, the dilation filter checks if any 1 pixels within the structuring element are present. If at least one 1 pixel is found, the filter sets the corresponding pixel in the output image as 1. Thus, the filter expands the regions of 1 pixels by including neighboring pixels within the defined neighborhood.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_dilation_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_dilation_filter_result.png
       :align: center