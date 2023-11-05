.. _VRT band math:

*************
VRT band math
*************

Create a single-`band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ VRT `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ specifying a `VRT Python Pixel Function <https://gdal.org/drivers/raster/vrt.html#using-derived-bands-with-pixel-functions-in-python>`_. Use any `NumPy <https://numpy.org/doc/stable/reference/>`_-based arithmetic, or even arbitrary Python code.

.. include:: ../../processing_algorithms_includes/raster_analysis/vrt_band_math.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    Input `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Selected bands` [band]
    List of input `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Code` [string]
    The mathematical calculation to be performed on the selected input `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in_ar.Result must be copied to out_ar.
    For detailed usage information read the `VRT Python Pixel Function <https://gdal.org/drivers/raster/vrt.html#using-derived-bands-with-pixel-functions-in-python>`_ docs.


:guilabel:`Data type` [enum]
    Output data type.

    Default: *5*


:guilabel:`No data value` [number]
    Output `no data value <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.


:guilabel:`Band name` [string]
    Output `band name <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band-name>`_.


:guilabel:`Buffer radius` [number]
    The number of columns and rows to read from the neighbouring blocks. Needs to be specified only when performing spatial operations, to avoid artifacts at block borders.

**Outputs**


:guilabel:`Output VRT layer` [rasterDestination]
    VRT file destination.

**Command-line usage**

``>qgis_process help enmapbox:VrtBandMath``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    bandList: Selected bands
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    code: Code
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataType: Data type (optional)
    	Default value:	5
    	Argument type:	enum
    	Available values:
    		- 0: Byte
    		- 1: Int16
    		- 2: UInt16
    		- 3: UInt32
    		- 4: Int32
    		- 5: Float32
    		- 6: Float64
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    noData: No data value (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    bandName: Band name (optional)
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    overlap: Buffer radius (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputVrt: Output VRT layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputVrt: <outputRaster>
    	Output VRT layer
    
    