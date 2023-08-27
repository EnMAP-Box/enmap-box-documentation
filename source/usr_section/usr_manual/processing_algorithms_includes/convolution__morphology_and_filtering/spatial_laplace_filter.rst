The Spatial Laplace filter enhances and detects edges or areas of rapid intensity changes in an image by convolving it with a Laplacian kernel. The Laplacian kernel is a matrix that represents the discrete approximation of the Laplace operator, which calculates the sum of the second partial derivatives of the image with respect to the x and y directions. By convolving the image with the Laplacian kernel, the filter highlights areas of significant intensity changes, such as edges or transitions between regions with different intensities. It amplifies these intensity variations by emphasizing high-frequency components in the image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/laplace_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/laplace_filter_result.png
       :align: center