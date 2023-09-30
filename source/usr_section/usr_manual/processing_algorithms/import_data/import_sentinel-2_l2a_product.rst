.. _Import Sentinel-2 L2A product:

*****************************
Import Sentinel-2 L2A product
*****************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ information is set and data is scaled into the 0 to 10000 range.

**Parameters**


:guilabel:`Metadata file` [file]
    The MTD_MSIL2A.xml metadata file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata file directly from your system file browser onto the EnMAP-Box map view area.


:guilabel:`Band list` [enum]
    Bands to be stacked together. Defaults to all 10m and 20m `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ ordered by `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_. Note that the destination pixel size matches the smallest/finest pixel size over all selected bands.

    Default: *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportSentinel2L2AProduct``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    bandList: Band list (optional)
    	Default value:	
    	Argument type:	enum
    	Available values:
    		- 0: B1, Coastal aerosol (443 Nanometers)[60 Meter]
    		- 1: B2, Blue (492 Nanometers)[10 Meter]
    		- 2: B3, Green (560 Nanometers)[10 Meter]
    		- 3: B4, Red (665 Nanometers)[10 Meter]
    		- 4: B5, Vegetation red edge (704 Nanometers)[20 Meter]
    		- 5: B6, Vegetation red edge (741 Nanometers)[20 Meter]
    		- 6: B7, Vegetation red edge (783 Nanometers)[20 Meter]
    		- 7: B8, NIR (833 Nanometers)[10 Meter]
    		- 8: B8A, Narrow NIR (865 Nanometers)[20 Meter]
    		- 9: B9, Water vapour (945 Nanometers)[60 Meter]
    		- 10: B11, SWIR (1614 Nanometers)[20 Meter]
    		- 11: B12, SWIR (2202 Nanometers)[20 Meter]
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    outputSentinel2L2ARaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputSentinel2L2ARaster: <outputRaster>
    	Output raster layer
    
    