The 2D Trapezoid filter uses a trapezoidal weighting function. Thus, the filter assigns higher weights to pixels within a certain range and lower weights to pixels outside that range. It can be used to emphasize or suppress certain features in an image within a specific range of values. The trapezoidal shape of the weighting function allows for a controlled transition of the filter’s effect, enabling customization of the filtering operation based on the desired outcome. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/trapez_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/trapez_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/trapez_filter_result.png
       :align: center