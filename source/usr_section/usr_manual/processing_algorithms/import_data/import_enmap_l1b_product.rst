.. _Import EnMAP L1B product:

************************
Import EnMAP L1B product
************************

Prepare VNIR and SWIR `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information is set and data is scaled according to data gain/offset values.

**Parameters**


:guilabel:`Metadata file` [file]
    The metadata XML file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata XML file directly from your system file browser onto the EnMAP-Box map view area.

**Outputs**


:guilabel:`Output VNIR raster layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output SWIR raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportEnmapL1BProduct``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputEnmapL1BRasterVnir: Output VNIR raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputEnmapL1BRasterSwir: Output SWIR raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputEnmapL1BRasterVnir: <outputRaster>
    	Output VNIR raster layer
    outputEnmapL1BRasterSwir: <outputRaster>
    	Output SWIR raster layer
    
    