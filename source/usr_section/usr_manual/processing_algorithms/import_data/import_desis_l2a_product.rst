.. _Import DESIS L2A product:

************************
Import DESIS L2A product
************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information is set and data is scaled into the 0 to 10000 range.
Note that the DESIS L2D spectral data file is `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ interleaved by pixel and compressed, which is very disadvantageous for visualization in QGIS / EnMAP-Box. For faster exploration concider saving the resulting VRT `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ as GTiff format via the "Translate raster `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_" algorithm.

**Parameters**


:guilabel:`Metadata file` [file]
    The metadata XML file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata XML file directly from your system file browser onto the EnMAP-Box map view area.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportDesisL2AProduct``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputDesisL2ARaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputDesisL2ARaster: <outputRaster>
    	Output raster layer
    
    