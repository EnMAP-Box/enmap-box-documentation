.. _Regressor performance report:

****************************
Regressor performance report
****************************

Evaluates `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ performance.

**Parameters**


:guilabel:`Regressor` [file]
    `Regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.


:guilabel:`Test dataset` [file]
    `Test dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-test-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for assessing the `regressor <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regressor>`_ performance.


:guilabel:`Number of cross-validation folds` [number]
    The number of folds used for assessing `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance. If not specified (default), simple test performance is assessed.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Output report file destination.

**Command-line usage**

``>qgis_process help enmapbox:RegressorPerformanceReport``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    dataset: Test dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    nfold: Number of cross-validation folds (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputRegressorPerformance: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressorPerformance: <outputHtml>
    	Output report
    
    