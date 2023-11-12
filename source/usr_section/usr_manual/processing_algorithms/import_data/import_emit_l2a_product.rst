.. _Import EMIT L2A product:

***********************
Import EMIT L2A product
***********************

Prepare a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ from the given product. `Wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information is set and data is scaled into the 0 to 1 range.
EMIT website: `https://earth.jpl.nasa.gov/emit/ <https://earth.jpl.nasa.gov/emit/>`_

.. include:: ../../processing_algorithms_includes/import_data/import_emit_l2a_product.rst


**Parameters**


:guilabel:`NetCDF file` [file]
    The EMIT L2A RFL NetCDF product file.
    Instead of executing this algorithm, you may drag&drop the NetCDF file directly from your system file browser a) onto the EnMAP-Box map view area, or b) onto the Sensor Product Import panel.


:guilabel:`Skip bad bands` [boolean]
    Whether to exclude `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_.

    Default: *True*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ImportEmitL2AProduct``::

    ----------------
    Arguments
    ----------------
    
    file: NetCDF file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    skipBadBands: Skip bad bands
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputEmitL2ARaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputEmitL2ARaster: <outputRaster>
    	Output raster layer
    
    