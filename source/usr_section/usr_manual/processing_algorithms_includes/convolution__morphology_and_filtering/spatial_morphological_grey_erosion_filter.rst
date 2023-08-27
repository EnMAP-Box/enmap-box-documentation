The filter operates by moving a structuring element across the image. The structuring element defines the neighborhood around each pixel that will be considered during the erosion operation.

For each pixel in the image, the grey erosion filter finds the minimum pixel value within the structuring element’s neighborhood and assigns this minimum value to the corresponding pixel in the output image.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/erosion_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/erosion_filter_result.png
       :align: center