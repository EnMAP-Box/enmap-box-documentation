.. _Spatial Laplace filter:

**********************
Spatial Laplace filter
**********************

Spatial Laplace filter. See `Wikipedia <https://en.wikipedia.org/wiki/Discrete_Laplace_operator#Image_Processing>`_ for general information.

.. include:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/spatial_laplace_filter.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `laplace <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.laplace.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import laplace
        
        function = lambda array: laplace(array)

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialLaplaceFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import laplace
    
    function = lambda array: laplace(array)
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
    
    