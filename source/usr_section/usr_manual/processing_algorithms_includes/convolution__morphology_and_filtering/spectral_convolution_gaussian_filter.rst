This 1D Gaussian filter applies a weighted average to the values in the image. The weights are determined by a Gaussian distribution, which assigns higher weights to pixels closer to the center of the kernel and lower weights to pixels farther away. It is isotropic and does not produce artifacts.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/spectral_gaussian_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/img/spectral_gaussian_filter_result.png
       :align: center