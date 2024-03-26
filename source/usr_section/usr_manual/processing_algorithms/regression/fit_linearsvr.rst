.. _Fit LinearSVR:

*************
Fit LinearSVR
*************

Linear Support Vector `Regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_.
Similar to SVR with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

.. include:: ../../processing_algorithms_includes/regression/fit_linearsvr.rst


**Parameters**


:guilabel:`Regressor` [string]
    Scikit-learn python code. See `LinearSVR <https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.model_selection import GridSearchCV
        from sklearn.multioutput import MultiOutputRegressor
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import LinearSVR
        
        svr = LinearSVR()
        param_grid = {'epsilon': [0.], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
        tunedSVR = GridSearchCV(cv=3, estimator=svr, scoring='neg_mean_absolute_error', param_grid=param_grid)
        scaledAndTunedSVR = make_pipeline(StandardScaler(), tunedSVR)
        regressor = MultiOutputRegressor(scaledAndTunedSVR)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitLinearsvr``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.multioutput import MultiOutputRegressor
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import LinearSVR
    
    svr = LinearSVR()
    param_grid = {'epsilon': [0.], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
    tunedSVR = GridSearchCV(cv=3, estimator=svr, scoring='neg_mean_absolute_error', param_grid=param_grid)
    scaledAndTunedSVR = make_pipeline(StandardScaler(), tunedSVR)
    regressor = MultiOutputRegressor(scaledAndTunedSVR)
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
    
    