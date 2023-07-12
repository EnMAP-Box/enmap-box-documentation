.. _Spatial morphological Binary Opening filter:

*******************************************
Spatial morphological Binary Opening filter
*******************************************

The filter operates by first applying a binary erosion operation to the input image using a structuring element, which is a predefined shape. The erosion operation removes small 1 regions and shrinks the remaining regions.

Next, a binary dilation operation is applied to the eroded image using the same structuring element. The dilation operation expands the remaining regions, counteracting the shrinkage caused by the erosion operation. The result is a binary image where small foreground regions have been eliminated, and the remaining regions have been smoothed and preserved.

When applying this algorithm to continous image data, the input will be binarised.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Binary Opening filter`.

    .. figure:: ./img/binary_opening_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/binary_opening_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/binary_opening_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: Zf8spYv1Xuw
        :width: 100%
        :privacy_mode:


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_opening.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import binary_opening, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: binary_opening(array, structure=structure, iterations=1)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryOpeningFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import binary_opening, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_opening(array, structure=structure, iterations=1)
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
    
    