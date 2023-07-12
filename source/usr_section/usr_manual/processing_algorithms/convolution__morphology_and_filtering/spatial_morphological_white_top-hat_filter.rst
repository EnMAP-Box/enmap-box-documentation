.. _Spatial morphological White Top-Hat filter:

******************************************
Spatial morphological White Top-Hat filter
******************************************

The Spatial morphological White Top-Hat filter is used to extract and enhance small bright structures or features from an image. It is achieved through a combination of morphological closing and subtraction operations, isolating the desired components while suppressing lower intensity regions.

Usage:

1. Open the Processing Toolbox with :guilabel:`View > Panels > Processing Toolbox`.

    .. figure:: ./img/open_toolbox.png
       :align: center

2. Select the corresponding filter under :guilabel:`EnMAP-Box > convolution, morphology and filtering > Spatial morphological White Top-Hat filter`.

    .. figure:: ./img/white_tophat_filter_location.png
       :align: center

3. Select the raster to process and modify the parameterization if necessary, then click :guilabel:`run`.

    .. figure:: ./img/white_tophat_filter_interface.png
       :align: center

4. View the processed image in comparison to the original.

    .. figure:: ./img/white_tophat_filter_result.png
       :align: center

Live demonstration
    ..  youtube:: kohPCSUq8Kk
        :width: 100%
        :privacy_mode:


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `scipy.ndimage.white_tophat <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.white_tophat.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.morphology import white_tophat
        
        function = lambda array: white_tophat(array, size=(3, 3))
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialMorphologicalWhiteTophatFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.morphology import white_tophat
    
    function = lambda array: white_tophat(array, size=(3, 3))
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
    
    