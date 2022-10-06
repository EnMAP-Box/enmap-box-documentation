.. _Spectral Index Optimizer:

************************
Spectral Index Optimizer
************************

This algorithm finds the optimal two-`feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ index by modelling a `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ variable via linear `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_.

**Parameters**


:guilabel:`Training dataset` [file]
    The `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.


:guilabel:`Formular` [string]
    The formular with variable `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ A and B to be optimized, and up to three fixed features F1, F2 and F3.

    Default: *(A-B) / (A+B)*


:guilabel:`Max. features` [number]
    Limit the number of `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ to be evaluated. Default is to use all features.


:guilabel:`Fixed feature F1` [number]
    Specify to use a fixed `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ F1 in the formular.


:guilabel:`Fixed feature F2` [number]
    Specify to use a fixed `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ F2 in the formular.


:guilabel:`Fixed feature F3` [number]
    Specify to use a fixed `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ F3 in the formular.

**Outputs**


:guilabel:`Output score matrix` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralIndexOptimizer``::

    ----------------
    Arguments
    ----------------
    
    dataset: Training dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    formular: Formular
    	Default value:	(A-B) / (A+B)
    	Argument type:	string
    	Acceptable values:
    		- String value
    maxFeatures: Max. features (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    f1: Fixed feature F1 (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    f2: Fixed feature F2 (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    f3: Fixed feature F3 (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    outScoreMatrix: Output score matrix
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outScoreMatrix: <outputRaster>
    	Output score matrix
    
    