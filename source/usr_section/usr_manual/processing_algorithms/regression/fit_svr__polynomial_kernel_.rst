.. _Fit SVR (polynomial kernel):

***************************
Fit SVR (polynomial kernel)
***************************

Epsilon-Support Vector `Regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_.
The free parameters in the model are C and epsilon.
The implementation is based on libsvm. The fit time complexity is more than quadratic with the number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ which makes it hard to scale to `datasets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ with more than a couple of 10000 samples.

.. include:: ../../processing_algorithms_includes/regression/fit_svr__polynomial_kernel_.rst

**Parameters**


:guilabel:`Regressor` [string]
    Scikit-learn python code. See `SVR <http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html>`_, `GridSearchCV <http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_, `StandardScaler <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.model_selection import GridSearchCV
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVR
        
        svr = SVR()
        param_grid = {'kernel': ['poly'],
                      'epsilon': [0.],
                      'coef0': [0],
                      'degree': [3],
                      'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                      'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
        tunedSVR = GridSearchCV(cv=3, estimator=svr, scoring='neg_mean_absolute_error', param_grid=param_grid)
        regressor = make_pipeline(StandardScaler(), tunedSVR)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitSvrPolynomialKernel``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVR
    
    svr = SVR()
    param_grid = {'kernel': ['poly'],
                  'epsilon': [0.],
                  'coef0': [0],
                  'degree': [3],
                  'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                  'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
    tunedSVR = GridSearchCV(cv=3, estimator=svr, scoring='neg_mean_absolute_error', param_grid=param_grid)
    regressor = make_pipeline(StandardScaler(), tunedSVR)
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
    
    