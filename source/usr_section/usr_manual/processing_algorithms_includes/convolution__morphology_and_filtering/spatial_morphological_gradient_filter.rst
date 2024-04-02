The Spatial Morphological Gradient filter calculates the difference between the dilation and erosion of an image using a structuring element. Dilation expands the regions of an image, while erosion shrinks them. By taking the difference between these two operations, the filter effectively enhances the boundaries or edges of objects in the image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/gradient_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/gradient_filter_result.png
       :align: center