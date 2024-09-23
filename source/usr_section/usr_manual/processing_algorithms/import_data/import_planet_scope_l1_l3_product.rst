.. _Import Planet Scope L1/L3 product:

*********************************
Import Planet Scope L1/L3 product
*********************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ information is set and data is scaled into the 0 to 1 range.

**Parameters**


:guilabel:`Scene collection file` [file]
    The PSScene_collection.json file associated with the product.
    Instead of executing this algorithm, you may drag&drop the PSScene_collection.json file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.

**Outputs**


:guilabel:`Output SR raster layer` [rasterDestination]
     Surface Reflectance raster file destination.


:guilabel:`Output UDM2 raster layer` [rasterDestination]
     Usable Data Mask (UDM2) raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportPlanetScopeL1L3Product``::

    ----------------
    Arguments
    ----------------
    
    file: Scene collection file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputPlanetScopeL3BRasterSR: Output SR raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputPlanetScopeL3BRasterQA: Output UDM2 raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputPlanetScopeL3BRasterSR: <outputRaster>
    	Output SR raster layer
    outputPlanetScopeL3BRasterQA: <outputRaster>
    	Output UDM2 raster layer
    
    