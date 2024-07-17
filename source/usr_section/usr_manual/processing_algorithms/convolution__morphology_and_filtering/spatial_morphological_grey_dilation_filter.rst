.. _Spatial morphological Grey Dilation filter:

******************************************
Spatial morphological Grey Dilation filter
******************************************

Spatial morphological Grey Dilation filter. See `Wikipedia <https://en.wikipedia.org/wiki/Dilation_(morphology)>`_ for general information.

.. include:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/spatial_morphological_grey_dilation_filter.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `grey_dilation <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.grey_dilation.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage import grey_dilation, generate_binary_structure, iterate_structure
        
        structure = generate_binary_structure(rank=2, connectivity=1)
        structure = iterate_structure(structure=structure, iterations=1)
        function = lambda array: grey_dilation(array, structure=structure)

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalGreyDilationFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage import grey_dilation, generate_binary_structure, iterate_structure
    
    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: grey_dilation(array, structure=structure)
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    