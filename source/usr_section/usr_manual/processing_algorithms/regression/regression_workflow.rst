.. _Regression workflow:

*******************
Regression workflow
*******************

The `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ workflow combines `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ fitting and map prediction.Optionally, the `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance of the regressor can be assessed.

**Parameters**


:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Regressor` [string]
    Scikit-Learn Python code specifying a `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_.


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ for mapping. `Regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ features and raster bands are matched by name. Will be ignored, if map prediction is skipped.


:guilabel:`Number of cross-validation folds` [number]
    The number of folds used for assessing `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance. Will be ignored, if the cross-validation performance assessment is skipped.

    Default: *10*


:guilabel:`Open output cross-validation regressor performance report in webbrowser after running algorithm` [boolean]
    Whether to open the `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance report in the web browser. Will be ignored, if the cross-validation performance assessment is skipped.

    Default: *True*

**Outputs**


:guilabel:`Output cross-validation regressor performance report` [fileDestination]
    Output `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance report file destination.


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.


:guilabel:`Output regression layer` [rasterDestination]
    Predicted map file destination.

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
    openReport: Open output cross-validation regressor performance report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputRegressorPerformance: Output cross-validation regressor performance report (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputRegressor: Output regressor
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputRegression: Output regression layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRegressorPerformance: <outputHtml>
    	Output cross-validation regressor performance report
    outputRegressor: <outputFile>
    	Output regressor
    outputRegression: <outputRaster>
    	Output regression layer
    
    