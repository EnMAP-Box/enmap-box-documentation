The Spatial Sobel filter is an image filter used in image processing and computer vision to detect edges in an image. It calculates the gradient magnitude of an image by approximating the gradient using two separate convolution kernels: one for the horizontal direction (Sobel X) and another for the vertical direction (Sobel Y).

The filter operates by convolving the image with the Sobel X and Sobel Y kernels. These kernels are designed to approximate the first derivative of the image intensity in the corresponding directions. By convolving the image with these kernels, the filter estimates the rate of change of pixel intensities in the horizontal and vertical directions.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/sobel_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/sobel_filter_result.png
       :align: center