.. _Import DESIS L1B product:

************************
Import DESIS L1B product
************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information is set and data is scaled according to data gain/offset values.

.. include:: ../../processing_algorithms_includes/import_data/import_desis_l1b_product.rst

**Parameters**


:guilabel:`Metadata file` [file]
    The metadata XML file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata XML file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportDesisL1BProduct``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputDesisL1CRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputDesisL1CRaster: <outputRaster>
    	Output raster layer
    
    