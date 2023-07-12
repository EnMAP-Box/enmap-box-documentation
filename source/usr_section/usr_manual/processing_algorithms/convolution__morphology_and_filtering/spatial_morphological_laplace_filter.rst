.. _Spatial morphological Laplace filter:

************************************
Spatial morphological Laplace filter
************************************

The Spatial morphological Laplace filter is used to enhance and detect edges or transitions in an image. It combines morphological dilation and erosion operations to isolate high-frequency components associated with image edges.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological Laplace filter`.

    .. figure:: ./img/morph_laplace_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/morph_laplace_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/morph_laplace_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: caGYR2_RzcU
        :width: 100%
        :privacy_mode:

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `morphological_laplace <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.morphological_laplace.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import morphological_laplace
        
        function = lambda array: morphological_laplace(array, size=(3, 3))
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalLaplaceFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import morphological_laplace
    
    function = lambda array: morphological_laplace(array, size=(3, 3))
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
    
    