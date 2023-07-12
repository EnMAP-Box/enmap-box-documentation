.. _Spatial morphological Binary Fill Holes filter:

**********************************************
Spatial morphological Binary Fill Holes filter
**********************************************

The filter operates by iteratively applying a combination of binary dilation and binary erosion operations until all the holes in the image are filled. It performs binary dilation on the complement of the input image (flipping 1 and 0 pixels), followed by a binary intersection with the original input image. This process is repeated until no changes are observed in the resulting image, indicating that all holes have been filled.

When applying this algorithm to continous image data, the input will be binarised.

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Binary Fill Holes filter`.

    .. figure:: ./img/binary_fill_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/binary_fill_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/binary_fill_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: PXm0NMGhfFQ
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_fill_holes.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import binary_fill_holes, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: binary_fill_holes(array, structure=structure)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryFillHolesFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import binary_fill_holes, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_fill_holes(array, structure=structure)
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
    
    