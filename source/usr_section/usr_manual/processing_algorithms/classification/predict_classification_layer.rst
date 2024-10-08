.. _Predict classification layer:

****************************
Predict classification layer
****************************

Uses a fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ to predict a `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. 
Used in the Cookbook Recipes: `Classification <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/classification.html>`_, `Graphical Modeler <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/graphical_modeler.html>`_ for information on different parameters.

.. include:: ../../processing_algorithms_includes/classification/predict_classification_layer.rst

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. Classifier features and raster bands are matched by name to allow for `classifiers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ trained on a subset of the raster bands. If raster bands and `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ features are not matching by name, but overall number of bands and features do match, raster bands are used in original order.


:guilabel:`Classifier` [file]
    A fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.


:guilabel:`Match features and bands by name` [boolean]
    Whether to match raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by name.

    Default: *False*

**Outputs**


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:PredictClassificationLayer``::

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
    outputClassification: Output classification layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputClassification: <outputRaster>
    	Output classification layer
    
    