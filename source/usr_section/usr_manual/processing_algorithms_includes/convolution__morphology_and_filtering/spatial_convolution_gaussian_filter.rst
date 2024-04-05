This 2D Gaussian filter applies a weighted average to the pixel values in the image. The weights are determined by a Gaussian distribution, which assigns higher weights to pixels closer to the center of the kernel and lower weights to pixels farther away. It is isotropic and does not produce artifacts. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/gaussian_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/gausian_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/gaussian_filter_result.png
       :align: center