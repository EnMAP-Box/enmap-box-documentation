The Spatial Gaussian Gradient Magnitude filter computes the magnitude of the gradient of an image using Gaussian derivatives, providing a measure of the strength of the gradient at each pixel and helping to highlight edges and transitions in the image. The filter operates by convolving the image with a pair of Gaussian derivative kernels—one for the x-direction and another for the y-direction. These kernels are derived from the Gaussian function and are used to estimate the image gradient in both the horizontal and vertical directions.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/ggrad_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/ggrad_filter_result.png
       :align: center