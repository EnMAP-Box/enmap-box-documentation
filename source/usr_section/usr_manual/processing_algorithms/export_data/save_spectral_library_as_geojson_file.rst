.. _Save spectral library as GeoJSON file:

*************************************
Save spectral library as GeoJSON file
*************************************

Save a `spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-library>`_ as a human-readable GeoJSON text file. All binary profile `fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ will be converted into human-readable dictionary strings.

.. include:: ../../processing_algorithms_includes/export_data/save_spectral_library_as_geojson_file.rst

**Parameters**


:guilabel:`Spectral library` [vector]
    The `spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-library>`_ to be stored as GeoJSON text file.

**Outputs**


:guilabel:`Output file` [fileDestination]
    Destination GeoJSON file.

**Command-line usage**

``>qgis_process help enmapbox:SaveSpectralLibraryAsGeojsonFile``::

    ----------------
    Arguments
    ----------------
    
    library: Spectral library
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    outputFile: Output file
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputFile: <outputFile>
    	Output file
    
    