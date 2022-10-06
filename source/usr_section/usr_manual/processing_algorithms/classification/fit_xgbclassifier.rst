.. _Fit XGBClassifier:

*****************
Fit XGBClassifier
*****************

Implementation of the scikit-learn API for `XGBoost <https://xgboost.readthedocs.io/en/stable/>`_ `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_.

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code. See `XGBClassifier <https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=XGBClassifier#xgboost.XGBClassifier>`_ for information on different parameters.

    Default::

        from xgboost import XGBClassifier
        classifier = XGBClassifier(n_estimators=100)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitXgbclassifier``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from xgboost import XGBClassifier
    classifier = XGBClassifier(n_estimators=100)
    	Argument type:	string
    	Acceptable values:
    		- String value
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
    
    