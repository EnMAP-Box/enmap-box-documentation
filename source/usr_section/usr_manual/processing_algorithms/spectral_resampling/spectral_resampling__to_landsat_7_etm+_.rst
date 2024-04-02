.. _Spectral resampling (to Landsat 7 ETM+):

***************************************
Spectral resampling (to Landsat 7 ETM+)
***************************************

Spectral resampling to Landsat 7 ETM+ sensor.
For more information see the `mission website <https://www.usgs.gov/core-science-systems/nli/landsat/landsat-satellite-missions>`_.

.. include:: ../../processing_algorithms_includes/spectral_resampling/spectral_resampling__to_landsat_7_etm+_.rst

**Parameters**


:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToLandsat7Etm``::

    ----------------
    Arguments
    ----------------
    
    raster: Spectral raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputResampledRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputResampledRaster: <outputRaster>
    	Output raster layer
    
    