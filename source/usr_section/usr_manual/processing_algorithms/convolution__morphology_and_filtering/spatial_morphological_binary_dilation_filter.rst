.. _Spatial morphological Binary Dilation filter:

********************************************
Spatial morphological Binary Dilation filter
********************************************

The spatial morphological binary dilation filter expands or dilates regions of foreground or 1 pixels in a binary image. It is used for tasks such as noise removal, boundary enhancement, and image segmentation, providing a way to fill gaps, smooth out regions, and connect adjacent pixels or objects.

The filter operates by moving a structuring element across the image. The structuring element defines the neighborhood around each pixel that will be considered during the dilation operation.

For each pixel in the image, the dilation filter checks if any 1 pixels within the structuring element are present. If at least one 1 pixel is found, the filter sets the corresponding pixel in the output image as 1. Thus, the filter expands the regions of 1 pixels by including neighboring pixels within the defined neighborhood.

When applying this algorithm to continous image data, the input will be binarised.

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Binary Dilation filter`.

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
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_dilation.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import binary_dilation, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: binary_dilation(array, structure=structure, iterations=1)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryDilationFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import binary_dilation, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_dilation(array, structure=structure, iterations=1)
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
    
    