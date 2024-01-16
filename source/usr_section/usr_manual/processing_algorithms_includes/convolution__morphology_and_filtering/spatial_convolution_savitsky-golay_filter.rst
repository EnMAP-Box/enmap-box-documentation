The Savitzky-Golay filter is a linear filter that performs convolution using a sliding window over the input data. It aims to smooth the data while preserving important features, such as edges or peaks, by fitting a polynomial function within the window and using it to estimate the filtered value at the center point.

In the case of a Spatial convolution 2D Savitzky-Golay filter, the filter operates on a two-dimensional image. It applies the Savitzky-Golay technique separately along each dimension (rows and columns) of the image.

The main purpose of the 2D Savitzky-Golay filter is to reduce noise and smooth the image while preserving the sharpness and fine details. By fitting a polynomial function to the local neighborhood of each pixel, it provides a weighted average that is influenced by the neighboring pixels, effectively reducing the noise contribution.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/golay_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: source/usr_section/usr_manual/processing_algorithms_includes/convolution__morphology_and_filtering/img/golay_filter_result.png
       :align: center