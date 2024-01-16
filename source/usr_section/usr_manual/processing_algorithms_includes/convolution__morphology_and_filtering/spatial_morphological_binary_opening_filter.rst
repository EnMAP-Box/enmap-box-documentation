The filter operates by first applying a binary erosion operation to the input image using a structuring element, which is a predefined shape. The erosion operation removes small 1 regions and shrinks the remaining regions.

Next, a binary dilation operation is applied to the eroded image using the same structuring element. The dilation operation expands the remaining regions, counteracting the shrinkage caused by the erosion operation. The result is a binary image where small foreground regions have been eliminated, and the remaining regions have been smoothed and preserved.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_opening_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_opening_filter_result.png
       :align: center