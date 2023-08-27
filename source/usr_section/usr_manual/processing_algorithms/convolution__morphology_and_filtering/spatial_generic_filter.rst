.. _Spatial generic filter:

**********************
Spatial generic filter
**********************

Spatial generic (user-defined) filter.

.. include:: ../../processing_algorithms_includes/convolution__morphology_and_filtering/spatial_generic_filter.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code. See `generic_filter <https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generic_filter.html>`_ for information on different parameters.

    Default::

        from scipy.ndimage.filters import generic_filter
        import numpy as np
        
        def filter_function(invalues):
            # do whatever you want to create the output value, e.g. np.nansum
            outvalue = np.nansum(invalues)  # replace this line with your code!
            return outvalue
        
        function = lambda array: generic_filter(array, function=filter_function, size=3)
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpatialGenericFilter``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	from scipy.ndimage.filters import generic_filter
    import numpy as np
    
    def filter_function(invalues):
        # do whatever you want to create the output value, e.g. np.nansum
        outvalue = np.nansum(invalues)  # replace this line with your code!
        return outvalue
    
    function = lambda array: generic_filter(array, function=filter_function, size=3)
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
    
    