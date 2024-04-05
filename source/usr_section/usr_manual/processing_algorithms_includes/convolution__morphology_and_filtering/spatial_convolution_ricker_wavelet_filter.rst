The Ricker wavelet filter convolves an image with a kernel that approximates the Ricker wavelet, which is a bell-shaped waveform that resembles a symmetrically shaped hat or a Mexican hat. The Ricker wavelet filter is typically used for detecting and enhancing specific features or structures in an image. It is particularly effective in detecting edges, lines, or other localized patterns with a characteristic scale. The central peak of the Ricker wavelet helps to emphasize these features, while the positive and negative lobes contribute to enhancing the contrast and edges, which smooths the data and removes slowly varying or constant structures (e.g. background). It is useful for peak or multi-scale detection. An exemplary kernel can be found below.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/airy_disk_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/ricker_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/img/ricker_filter_result.png
       :align: center