.. _Subset raster layer bands:

*************************
Subset raster layer bands
*************************

Subsets `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and stores the result as a VRT file.This is a slimmed down version of the more powerful "Translate raster `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_" algorithm.

.. include:: ../../processing_algorithms_includes/raster_miscellaneous/subset_raster_layer_bands.rst

**Parameters**


:guilabel:`Raster layer` [raster]
    Source `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.


:guilabel:`Selected bands` [band]
    Bands to subset and rearrange. An empty selection defaults to all `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in native order.


:guilabel:`Exclude bad bands` [boolean]
    Whether to exclude `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_.

    Default: *False*


:guilabel:`Derive and exclude additional bad bands` [boolean]
    Whether to derive and exclude additional `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_ fully filled with inf, nan or `no data values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_.

    Default: *False*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SubsetRasterLayerBands``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    bandList: Selected bands (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    excludeBadBands: Exclude bad bands
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    excludeDerivedBadBands: Derive and exclude additional bad bands
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    