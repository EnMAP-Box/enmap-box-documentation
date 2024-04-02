.. _Fit LinearRegression:

********************
Fit LinearRegression
********************

Ordinary least squares Linear `Regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_.
LinearRegression fits a linear model with coefficients w = (w1, ..., wp) to minimize the residual sum of squares between the observed `targets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ in the `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_, and the targets predicted by the linear approximation.

.. include:: ../../processing_algorithms_includes/regression/fit_linearregression.rst

**Parameters**


:guilabel:`Regressor` [string]
    Scikit-learn python code. See `LinearRegression <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.linear_model import LinearRegression
        
        linearRegression = LinearRegression()
        regressor = make_pipeline(StandardScaler(), linearRegression)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitLinearregression``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression
    
    linearRegression = LinearRegression()
    regressor = make_pipeline(StandardScaler(), linearRegression)
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
    
    