.. _Create mask raster layer:

************************
Create mask raster layer
************************

Create a `mask raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-raster-layer>`_ by applying a user-defined evaluation function `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise to a source `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be processed `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_-wise.


:guilabel:`Function` [string]
    Python code defining the evaluation function. The defined function must return a binary-valued array with same shape as the input array.

    Default::

        import numpy as np
        
        def function(array: np.ndarray, noDataValue: float):
        
            # if source no data value is not defined, use zero as no data value
            if noDataValue is None:
                noDataValue = 0
        
            # mask no data pixel
            marray = np.not_equal(array, noDataValue)
        
            # mask inf and nan pixel
            marray[np.logical_not(np.isfinite(array))] = 0
        
            # include further masking criteria here
            pass
        
            return marray
**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateMaskRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    function: Function
    	Default value:	import numpy as np
    
    def function(array: np.ndarray, noDataValue: float):
    
        # if source no data value is not defined, use zero as no data value
        if noDataValue is None:
            noDataValue = 0
    
        # mask no data pixel
        marray = np.not_equal(array, noDataValue)
    
        # mask inf and nan pixel
        marray[np.logical_not(np.isfinite(array))] = 0
    
        # include further masking criteria here
        pass
    
        return marray
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
    
    