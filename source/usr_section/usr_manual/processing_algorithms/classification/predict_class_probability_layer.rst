.. _Predict class probability layer:

*******************************
Predict class probability layer
*******************************

Uses a fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ to predict `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.

.. include:: ../../processing_algorithms_includes/classification/predict_class_probability_layer.rst

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. `Classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ features and raster bands are matched by name.


:guilabel:`Classifier` [file]
    A fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.


:guilabel:`Match features and bands by name` [boolean]
    Whether to match raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by name.

    Default: *False*

**Outputs**


:guilabel:`Output class probability layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:PredictClassProbabilityLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    classifier: Classifier
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
    outputProbability: Output class probability layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputProbability: <outputRaster>
    	Output class probability layer
    
    