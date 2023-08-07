.. _Spatial Percentile filter:

*************************
Spatial Percentile filter
*************************

A Spatial Percentile Filter is an image filtering technique that aims to enhance or suppress certain features in an image based on their intensity values. It is a non-linear filter that replaces the value of a pixel with a specified percentile value of its neighborhood.


Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select the raster to process  and modify the parameterization if necessary, then click :guilabel:`run`.
    .. figure:: ./img/percentile_filter_interface.png
       :align: center

3. View the processed image in comparison to the original.

    .. figure:: ./img/percentile_filter_result.png
       :align: center



**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `percentile_filter <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.percentile_filter.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import percentile_filter
        
        function = lambda array: percentile_filter(array, percentile=50, size=3)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialPercentileFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import percentile_filter
    
    function = lambda array: percentile_filter(array, percentile=50, size=3)
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
    
    