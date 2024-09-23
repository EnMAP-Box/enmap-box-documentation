.. _Classifier performance report:

*****************************
Classifier performance report
*****************************

Evaluates `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ performance.

.. include:: ../../processing_algorithms_includes/classification/classifier_performance_report.rst

**Parameters**


:guilabel:`Classifier` [file]
    `Classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.


:guilabel:`Test dataset` [file]
    `Test dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-test-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for assessing the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ performance.


:guilabel:`Number of cross-validation folds` [number]
    The number of folds (n>=2) used for assessing `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance.
    If not specified (default), simple test performance is assessed.
    If set to a value of 1, out-of-bag (OOB) performance is assessed. Note that OOB estimates are only supported by some `classifiers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_, e.g. the Random Forest `Classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassifierPerformanceReport``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
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
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputClassifierPerformance: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassifierPerformance: <outputHtml>
    	Output report
    
    