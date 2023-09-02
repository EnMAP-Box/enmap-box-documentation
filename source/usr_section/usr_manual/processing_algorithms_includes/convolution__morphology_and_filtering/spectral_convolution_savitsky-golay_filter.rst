The Savitzky-Golay filter is a linear filter that performs convolution using a sliding window over the input data. It aims to smooth the data while preserving features, such as edges or peaks, by fitting a polynomial function within the window and using it to estimate the filtered value at the center point.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/spectral_golay_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/img/spectral_golay_filter_result.png
       :align: center
