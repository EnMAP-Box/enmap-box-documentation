.. _Spatial morphological Binary Closing filter:

*******************************************
Spatial morphological Binary Closing filter
*******************************************

The Spatial morphological Binary Closing filter is used to close small gaps and fill holes in binary images by performing dilation followed by erosion. It helps to connect nearby regions of the same value and smoothens the boundaries between them, resulting in improved object representation and noise reduction.

The process of binary closing begins with a dilation operation, where a structuring element (a predefined shape such as a disk or a square) is applied to the image. The structuring element moves across the image, and if any part of the structuring element overlaps with an object pixel (1), the corresponding output pixel becomes a 1. This operation expands or enlarges the 1 regions.

After the dilation operation, an erosion operation is performed using the same structuring element. The erosion operation shrinks the 1 regions by removing the outermost pixels that do not fully overlap with the structuring element. This process helps to restore the original size of the objects while eliminating small protrusions or gaps.

When applying this algorithm to continous image data, the input will be binarised.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Binary Closing filter`.

    .. figure:: ./img/binary_dilation_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/binary_dilation_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/binary_dilation_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: Hdt1yiDXw7U
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_closing.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import binary_closing, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: binary_closing(array, structure=structure, iterations=1)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryClosingFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import binary_closing, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_closing(array, structure=structure, iterations=1)
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
    
    