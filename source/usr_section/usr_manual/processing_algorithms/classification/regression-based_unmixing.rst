.. _Regression-based unmixing:

*************************
Regression-based unmixing
*************************

Implementation of the `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_-based unmixing approach `"Ensemble Learning From Synthetically Mixed Training Data for Quantifying Urban Land Cover With Support Vector Regression" <https://doi.org/10.1109/JSTARS.2016.2634859>`_ in IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 10, no. 4, pp. 1640-1650, April 2017.

**Parameters**


:guilabel:`Endmember dataset` [file]
    A `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ with spectral endmembers used for synthetical mixing.


:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be unmixed.


:guilabel:`Regressor` [string]
    Scikit-Learn Python code specifying a `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Number of mixtures per class` [number]
    Number of mixtures per `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_.

    Default: *1000*


:guilabel:`Proportion of background mixtures (%)` [number]
    Proportion of background mixtures.

    Default: *0*


:guilabel:`Include original endmembers` [boolean]
    Whether to include the original library spectra into the `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

    Default: *True*


:guilabel:`Mixing complexity probabilities` [string]
    A list of probabilities for using 2, 3, 4, ... endmember mixing models. Trailing 0 probabilities can be skipped. The default values of 0.5, 0.5,results in 50% 2-endmember and 50% 3-endmember models.

    Default: *0.5, 0.5*


:guilabel:`Allow within-class mixtures` [boolean]
    Whether to allow mixtures with profiles belonging to the same `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_.

    Default: *True*


:guilabel:`Class probabilities` [string]
    A list of probabilities for drawing profiles from each `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_. If not specified, class probabilities are proportional to the class size.


:guilabel:`Ensemble size` [number]
    Number of individual runs/predictions.

    Default: *1*


:guilabel:`Robust decision fusion` [boolean]
    Whether to use median and IQR (interquartile range) aggregation for ensemble decicion fusion. The default is to use mean and standard deviation.

    Default: *False*

**Outputs**


:guilabel:`Output class fraction layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output class fraction variation layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:RegressionbasedUnmixing``::

    ----------------
    Arguments
    ----------------
    
    dataset: Endmember dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    regressor: Regressor
    	Argument type:	string
    	Acceptable values:
    		- String value
    n: Number of mixtures per class
    	Default value:	1000
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    background: Proportion of background mixtures (%)
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    includeEndmember: Include original endmembers
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    mixingProbabilities: Mixing complexity probabilities (optional)
    	Default value:	0.5, 0.5
    	Argument type:	string
    	Acceptable values:
    		- String value
    allowWithinClassMixtures: Allow within-class mixtures
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    classProbabilities: Class probabilities (optional)
    	Argument type:	string
    	Acceptable values:
    		- String value
    ensembleSize: Ensemble size
    	Default value:	1
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    robustFusion: Robust decision fusion (optional)
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputFraction: Output class fraction layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputClassification: Output classification layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputFractionVariation: Output class fraction variation layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputFraction: <outputRaster>
    	Output class fraction layer
    outputClassification: <outputRaster>
    	Output classification layer
    outputFractionVariation: <outputRaster>
    	Output class fraction variation layer
    
    