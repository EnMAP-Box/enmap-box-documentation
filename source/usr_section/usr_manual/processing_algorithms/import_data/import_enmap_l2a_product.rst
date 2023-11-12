.. _Import EnMAP L2A product:

************************
Import EnMAP L2A product
************************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information is set and data is scaled into the 0 to 1 range.

.. include:: ../../processing_algorithms_includes/import_data/import_enmap_l2a_product.rst


**Parameters**


:guilabel:`Metadata file` [file]
    The metadata XML file associated with the product.
    Instead of executing this algorithm, you may drag&drop the metadata XML file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.


:guilabel:`Set bad bands` [boolean]
    Whether to mark no data `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ as `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_.

    Default: *True*


:guilabel:`Exclude bad bands` [boolean]
    Whether to exclude `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.

    Default: *True*


:guilabel:`Detector overlap region` [enum]
    Different options for handling the detector overlap region from 900 to 1000 nanometers. For the Moving average filter, a kernel size of 3 is used.

    Default: *4*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportEnmapL2AProduct``::

    ----------------
    Arguments
    ----------------
    
    file: Metadata file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    setBadBands: Set bad bands (optional)
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    excludeBadBands: Exclude bad bands (optional)
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    detectorOverlap: Detector overlap region
    	Default value:	4
    	Argument type:	enum
    	Available values:
    		- 0: Order by detector (VNIR, SWIR)
    		- 1: Order by wavelength (default order)
    		- 2: Moving average filter
    		- 3: VNIR only
    		- 4: SWIR only
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    outputEnmapL2ARaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputEnmapL2ARaster: <outputRaster>
    	Output raster layer
    
    