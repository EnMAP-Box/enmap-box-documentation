.. _Predict regression layer:

************************
Predict regression layer
************************

Uses a fitted `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ to predict a `regression layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. `Regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ features and raster bands are matched by name.


:guilabel:`Regressor` [file]
    A fitted `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Match features and bands by name` [boolean]
    Whether to match raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by name.

    Default: *False*

**Outputs**


:guilabel:`Output regression layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:PredictRegressionLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    regressor: Regressor
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
    outputRegression: Output regression layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRegression: <outputRaster>
    	Output regression layer
    
    