.. _Classification layer from class probability/fraction layer:

**********************************************************
Classification layer from class probability/fraction layer
**********************************************************

Creates `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ or `class fraction layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-fraction-layer>`_. Winner `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ is given by the class with maximum class probabiliy/fraction.

**Parameters**


:guilabel:`Class probability layer` [raster]
    A `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ or `class fraction layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-fraction-layer>`_ to be classified.

**Outputs**


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassificationLayerFromClassProbabilityfractionLayer``::

    ----------------
    Arguments
    ----------------
    
    probability: Class probability layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    outputClassification: Output classification layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputClassification: <outputRaster>
    	Output classification layer
    
    