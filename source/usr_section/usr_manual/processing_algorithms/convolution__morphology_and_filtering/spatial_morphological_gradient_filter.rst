.. _Spatial morphological Gradient filter:

*************************************
Spatial morphological Gradient filter
*************************************

The Spatial Morphological Gradient filter calculates the difference between the dilation and erosion of an image using a structuring element. Dilation expands the regions of an image, while erosion shrinks them. By taking the difference between these two operations, the filter effectively enhances the boundaries or edges of objects in the image.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Gradient filter`.

    .. figure:: ./img/gradient_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/gradient_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/gradient_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: iae_3UMqw-A
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.morphological_gradient.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import morphological_gradient, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: morphological_gradient(array, structure=structure)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalGradientFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import morphological_gradient, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: morphological_gradient(array, structure=structure)
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
    
    