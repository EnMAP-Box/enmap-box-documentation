The Spatial morphological Binary Closing filter is used to close small gaps and fill holes in binary images by performing dilation followed by erosion. It helps to connect nearby regions of the same value and smoothens the boundaries between them, resulting in improved object representation and noise reduction.

The process of binary closing begins with a dilation operation, where a structuring element (a predefined shape such as a disk or a square) is applied to the image. The structuring element moves across the image, and if any part of the structuring element overlaps with an object pixel (1), the corresponding output pixel becomes a 1. This operation expands or enlarges the 1 regions.

After the dilation operation, an erosion operation is performed using the same structuring element. The erosion operation shrinks the 1 regions by removing the outermost pixels that do not fully overlap with the structuring element. This process helps to restore the original size of the objects while eliminating small protrusions or gaps.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/binary_closing_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ./img/binary_closing_filter_result.png
       :align: center