.. _Fit XGBRFRegressor:

******************
Fit XGBRFRegressor
******************

Implementation of the scikit-learn API for `XGBoost <https://xgboost.readthedocs.io/en/stable/>`_ random forest `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_.

.. include:: ../../processing_algorithms_includes/regression/fit_xgbrfregressor.rst

**Parameters**


:guilabel:`Regressor` [string]
    Scikit-learn python code. See `XGBRFRegressor <https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=XGBRFRegressor#xgboost.XGBRFRegressor>`_ for information on different parameters.

    Default::

        from xgboost import XGBRFRegressor
        
        regressor = XGBRFRegressor(n_estimators=100)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitXgbrfregressor``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Default value:	from xgboost import XGBRFRegressor
    
    regressor = XGBRFRegressor(n_estimators=100)
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataset: Training dataset (optional)
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputRegressor: Output regressor
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressor: <outputFile>
    	Output regressor
    
    