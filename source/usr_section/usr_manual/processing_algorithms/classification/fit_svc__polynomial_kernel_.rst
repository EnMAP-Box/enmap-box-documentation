.. _Fit SVC (polynomial kernel):

***************************
Fit SVC (polynomial kernel)
***************************

C-Support Vector `Classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_. 
The implementation is based on libsvm. The fit time scales at least quadratically with the number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ and may be impractical beyond tens of thousands of samples. 
The multiclass support is handled according to a one-vs-one scheme.

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code. See `SVC <http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html>`_, `GridSearchCV <http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html>`_, `StandardScaler <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.model_selection import GridSearchCV
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVC
        
        svc = SVC(probability=False)
        param_grid = {'kernel': ['poly'],
                      'coef0': [0],
                      'degree': [3],
                      'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                      'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
        tunedSVC = GridSearchCV(cv=3, estimator=svc, scoring='f1_macro', param_grid=param_grid)
        classifier = make_pipeline(StandardScaler(), tunedSVC)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitSvcPolynomialKernel``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.model_selection import GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    
    svc = SVC(probability=False)
    param_grid = {'kernel': ['poly'],
                  'coef0': [0],
                  'degree': [3],
                  'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                  'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
    tunedSVC = GridSearchCV(cv=3, estimator=svc, scoring='f1_macro', param_grid=param_grid)
    classifier = make_pipeline(StandardScaler(), tunedSVC)
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
    
    