The filter operates by moving a window or kernel across the image and replacing the pixel within the window with the median pixel value found within that window. The size of the window determines the extent of the filter’s effect on the image.


UUsage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/median_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/median_filter_result.png
       :align: center