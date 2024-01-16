The spatial morphological binary erosion filter shrinks or erodes regions of 1 pixels in a binary image. The filter operates by moving a structuring element, which is a predefined shape such as a square or a circle, across the binary image. The structuring element defines the neighborhood around each pixel that will be considered during the erosion operation.

For each pixel in the image, the erosion filter checks if all the 1 pixels within the structuring element are present. If only 1 pixels are found, the filter sets the corresponding pixel in the output image as 1. In other words, the filter removes or erodes regions of 1 pixels that do not meet the criteria of the structuring element.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_erosion_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_erosion_filter_result.png
       :align: center