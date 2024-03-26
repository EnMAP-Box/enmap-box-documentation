The filter operates by iteratively applying a combination of binary dilation and binary erosion operations until all the holes in the image are filled. It performs binary dilation on the complement of the input image (flipping 1 and 0 pixels), followed by a binary intersection with the original input image. This process is repeated until no changes are observed in the resulting image, indicating that all holes have been filled.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_fill_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/binary_fill_filter_result.png
       :align: center