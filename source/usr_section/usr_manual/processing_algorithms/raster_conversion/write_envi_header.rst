.. _Write ENVI header:

*****************
Write ENVI header
*****************

Write/update the ENVI *.hdr* header file to enable full compatibility to the ENVI software. The header file stores `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_, FWHM and `bad band multiplier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band-multiplier>`_ (BBL) information.

.. include:: ../../processing_algorithms_includes/raster_conversion/write_envi_header.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    Source GeoTiff /ENVI `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

**Command-line usage**

``>qgis_process help enmapbox:WriteEnviHeader``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    
    ----------------
    Outputs
    ----------------
    
    
    