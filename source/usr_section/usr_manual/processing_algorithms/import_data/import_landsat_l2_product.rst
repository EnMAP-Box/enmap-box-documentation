.. _Import Landsat L2 product:

*************************
Import Landsat L2 product
*************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ information is set and data is scaled into the 0 to 1 range.Supports Landsat 4 to 9, collection 2. 

.. include:: ../../processing_algorithms_includes/import_data/import_landsat_l2_product.rst

**Parameters**


:guilabel:`Metadata file` [file]
    The *.MTL.txt* metadata file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata MTL.txt file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportLandsatL2Product``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputLandsatL2Raster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputLandsatL2Raster: <outputRaster>
    	Output raster layer
    
    