.. _Predict (unsupervised) classification layer:

*******************************************
Predict (unsupervised) classification layer
*******************************************

Uses a fitted `clusterer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clusterer>`_ to predict an (unsupervised) `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from a `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. Clusterer features and raster bands are matched by name to allow for `clusterers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clusterer>`_ trained on a subset of the raster bands. If raster bands and `clusterer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clusterer>`_ features are not matching by name, but overall number of bands and features do match, raster bands are used in original order.


:guilabel:`Clusterer` [file]
    A fitted `clusterer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clusterer>`_.

**Outputs**


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:PredictUnsupervisedClassificationLayer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    clusterer: Clusterer
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
    
    