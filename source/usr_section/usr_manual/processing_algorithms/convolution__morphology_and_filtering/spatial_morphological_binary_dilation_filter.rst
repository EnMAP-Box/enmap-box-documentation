
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-SpatialMorphologicalBinaryDilationFilter:

********************************************
Spatial morphological Binary Dilation filter
********************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Spatial morphological Binary Dilation filter. See `Wikipedia <https://en.wikipedia.org/wiki/Dilation_(morphology)>`_ for general information.

..
  ## AUTOGENERATED DESCRIPTION END

The spatial morphological binary dilation filter expands or dilates regions of foreground or 1 pixels in a binary image. It is used for tasks such as noise removal, boundary enhancement, and image segmentation, providing a way to fill gaps, smooth out regions, and connect adjacent pixels or objects.

The filter operates by moving a structuring element across the image. The structuring element defines the neighborhood around each pixel that will be considered during the dilation operation.

For each pixel in the image, the dilation filter checks if any 1 pixels within the structuring element are present. If at least one 1 pixel is found, the filter sets the corresponding pixel in the output image as 1. Thus, the filter expands the regions of 1 pixels by including neighboring pixels within the defined neighborhood.

When applying this algorithm to continous image data, the input will be binarised.

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/convolution__morphology_and_filtering/img/binary_dilation_filter_interface.png
       :align: center

3. Processed image in comparison to the original.

    .. figure:: ../../processing_algorithms/convolution__morphology_and_filtering/img/binary_dilation_filter_result.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.

:guilabel:`Function` [string]
    Python code. See `binary_closing <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_dilation.html>`_, `generate_binary_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generate_binary_structure.html>`_, `iterate_structure <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.iterate_structure.html>`_ for information on different parameters.
    Default::

        from scipy.ndimage import binary_dilation, generate_binary_structure, iterate_structure

        structure = generate_binary_structure\(rank=2, connectivity=1\)
        structure = iterate_structure\(structure=structure, iterations=1\)
        function = lambda array: binary_dilation\(array, structure=structure, iterations=1\)

**Outputs**

:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalBinaryDilationFilter``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    function: Function
        Default value:    from scipy.ndimage import binary_dilation, generate_binary_structure, iterate_structure

    structure = generate_binary_structure(rank=2, connectivity=1)
    structure = iterate_structure(structure=structure, iterations=1)
    function = lambda array: binary_dilation(array, structure=structure, iterations=1)
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
        Argument type:    rasterDestination
        Acceptable values:
            - Path for new raster layer

    ----------------
    Outputs
    ----------------

    outputRaster: <outputRaster>
        Output raster layer

..
  ## AUTOGENERATED COMMAND USAGE END

