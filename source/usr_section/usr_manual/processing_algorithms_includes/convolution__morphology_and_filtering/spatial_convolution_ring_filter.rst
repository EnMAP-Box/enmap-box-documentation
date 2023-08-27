The Ring filter kernel is the difference between two Top-Hat kernels of different width. This kernel is useful for, e.g., background estimation. It can further be used to extract circular or ring-shaped patterns in the image. It achieves this by assigning higher weights to the pixels located closer to the center of the kernel and lower weights to those farther away. This weighting scheme helps to enhance the circular or ring-like structures and suppress other image components. An exemplary kernel can be found below.

    .. figure:: ./img/ring_kernel.png
       :align: center


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/ring_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/ring_filter_result.png
       :align: center