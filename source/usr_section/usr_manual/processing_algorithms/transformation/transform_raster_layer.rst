.. _Transform raster layer:

**********************
Transform raster layer
**********************

Uses a fitted `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_ to transform a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

.. include:: ../../processing_algorithms_includes/transformation/transform_raster_layer.rst

**Parameters**


:guilabel:`Raster layer with features` [raster]
    The `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be transformed. `Transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ and raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ are matched by name.


:guilabel:`Transformer` [file]
    A fitted `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_.


:guilabel:`Match features and bands by name` [boolean]
    Whether to match raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by name.

    Default: *False*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:TransformRasterLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    transformer: Transformer
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    matchByName: Match features and bands by name (optional)
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
    
    