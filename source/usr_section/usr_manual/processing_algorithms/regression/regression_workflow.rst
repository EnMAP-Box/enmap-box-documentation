.. _Regression workflow:

*******************
Regression workflow
*******************

The `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ workflow combines `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ fitting, map prediction and accuracy assessment.

**Parameters**


:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Regressor` [string]
    Scikit-Learn Python code specifying a `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.


:guilabel:`Number of cross-validation folds` [number]
    The number of folds used for assessing `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance.

    Default: *10*


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.


:guilabel:`Output regression layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output regressor performance report` [fileDestination]
    Output report file destination.

**Command-line usage**

``>qgis_process help enmapbox:RegressionWorkflow``::

    ----------------
    Arguments
    ----------------
    
    dataset: Training dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    regressor: Regressor
    	Argument type:	string
    	Acceptable values:
    		- String value
    raster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    nfold: Number of cross-validation folds (optional)
    	Default value:	10
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputRegressor: Output regressor
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputRegression: Output regression layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputRegressorPerformance: Output regressor performance report (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressor: <outputFile>
    	Output regressor
    outputRegression: <outputRaster>
    	Output regression layer
    outputRegressorPerformance: <outputHtml>
    	Output regressor performance report
    
    