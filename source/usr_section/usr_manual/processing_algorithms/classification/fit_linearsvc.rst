.. _Fit LinearSVC:

*************
Fit LinearSVC
*************

Linear Support Vector `Classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_. 
Similar to SVC with parameter kernel='linear', but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_. 
This `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ supports both dense and sparse input and the multiclass support is handled according to a one-vs-the-rest scheme.

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code. See `LinearSVC <http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html>`_, `GridSearchCV <http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_, `StandardScaler <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.model_selection import GridSearchCV
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import LinearSVC
        
        svc = LinearSVC()
        param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
        tunedSVC = GridSearchCV(cv=3, estimator=svc, scoring='f1_macro', param_grid=param_grid)
        classifier = make_pipeline(StandardScaler(), tunedSVC)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitLinearsvc``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import LinearSVC
    
    svc = LinearSVC()
    param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
    tunedSVC = GridSearchCV(cv=3, estimator=svc, scoring='f1_macro', param_grid=param_grid)
    classifier = make_pipeline(StandardScaler(), tunedSVC)
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
    
    