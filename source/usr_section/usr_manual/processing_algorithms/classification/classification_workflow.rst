.. _Classification workflow:

***********************
Classification workflow
***********************

The `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ workflow combines `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ fitting, map prediction and accuracy assessment.

.. include:: ../../processing_algorithms_includes/classification/classification_workflow.rst

**Parameters**


:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.


:guilabel:`Classifier` [string]
    Scikit-Learn Python code specifying a `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.


:guilabel:`Raster layer with features` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for prediction.


:guilabel:`Match classifier features and raster bands by name` [boolean]
    Whether to match raster `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ and `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_ `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by name.

    Default: *False*


:guilabel:`Number of cross-validation folds` [number]
    The number of folds (n>=2) used for assessing `cross-validation <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-cross-validation>`_ performance.
    If not specified, simple training performance is assessed.
    If set to a value of 1, out-of-bag (OOB) performance is assessed. Note that OOB estimates are only supported by some `classifiers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_, e.g. the Random Forest `Classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.

    Default: *10*


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.


:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output class probability layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output classifier performance report` [fileDestination]
    Report file destination.


:guilabel:`Output classification accuracy and area report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassificationWorkflow``::

    ----------------
    Arguments
    ----------------
    
    dataset: Training dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    classifier: Classifier
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    raster: Raster layer with features (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    matchByName: Match classifier features and raster bands by name (optional)
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    nfold: Number of cross-validation folds (optional)
    	Default value:	10
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    openReport: Open output report in webbrowser after running algorithm (optional)
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputClassifier: Output classifier
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputClassification: Output classification layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputProbability: Output class probability layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputClassifierPerformance: Output classifier performance report (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputClassificationAccuracy: Output classification accuracy and area report (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassifier: <outputFile>
    	Output classifier
    outputClassification: <outputRaster>
    	Output classification layer
    outputProbability: <outputRaster>
    	Output class probability layer
    outputClassifierPerformance: <outputHtml>
    	Output classifier performance report
    outputClassificationAccuracy: <outputHtml>
    	Output classification accuracy and area report
    
    