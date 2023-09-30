.. _Fit LGBMClassifier:

******************
Fit LGBMClassifier
******************

Implementation of the scikit-learn API for `LightGBM <https://lightgbm.readthedocs.io/>`_ `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code. See `LGBMClassifier <https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html#lightgbm-lgbmclassifier>`_ for information on different parameters.

    Default::

        from lightgbm import LGBMClassifier
        classifier = LGBMClassifier(n_estimators=100)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitLgbmclassifier``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from lightgbm import LGBMClassifier
    classifier = LGBMClassifier(n_estimators=100)
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataset: Training dataset (optional)
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputClassifier: Output classifier
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassifier: <outputFile>
    	Output classifier
    
    