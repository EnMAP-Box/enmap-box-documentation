.. _Spatial morphological Binary Erosion filter:

*******************************************
Spatial morphological Binary Erosion filter
*******************************************

the spatial morphological binary erosion filter shrinks or erodes regions of 1 pixels in a binary image. The filter operates by moving a structuring element, which is a predefined shape such as a square or a circle, across the binary image. The structuring element defines the neighborhood around each pixel that will be considered during the erosion operation.

For each pixel in the image, the erosion filter checks if all the 1 pixels within the structuring element are present. If only 1 pixels are found, the filter sets the corresponding pixel in the output image as 1. In other words, the filter removes or erodes regions of 1 pixels that do not meet the criteria of the structuring element.

When applying this algorithm to continous image data, the input will be binarised.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/binary_erosion_filter_interface.png
       :align: center

3. View the processed image in comparison to the original.

    .. figure:: ./img/binary_erosion_filter_result.png
       :align: center



**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_erosion.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import binary_erosion, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: binary_erosion(array, structure=structure, iterations=1)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryErosionFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import binary_erosion, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_erosion(array, structure=structure, iterations=1)
    	Argument type:	string
    	Acceptable values:
    		- String value
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    