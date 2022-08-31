.. _Predict classification layer:

****************************
Predict classification layer
****************************

Uses a fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ to predict a `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. 
Used in the Cookbook Recipes: `Classification <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/classification.html>`_, `Graphical Modeler <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/graphical_modeler.html>`_ for information on different parameters.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. Classifier features and raster bands are matched by name to allow for `classifiers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ trained on a subset of the raster bands. If raster bands and `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ features are not matching by name, but overall number of bands and features do match, raster bands are used in original order.


:guilabel:`Classifier` [file]
    A fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.

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
    outputClassification: Output classification layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputClassification: <outputRaster>
    	Output classification layer
    
    