.. _Predict class probability layer:

*******************************
Predict class probability layer
*******************************

Uses a fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ to predict `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. `Classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ features and raster bands are matched by name.


:guilabel:`Classifier` [file]
    A fitted `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.

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
    outputProbability: Output class probability layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputProbability: <outputRaster>
    	Output class probability layer
    
    