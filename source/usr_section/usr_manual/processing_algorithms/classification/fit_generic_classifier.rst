.. _Fit generic classifier:

**********************
Fit generic classifier
**********************

A generic `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code.

    Default::

        from sklearn.dummy import DummyClassifier
        
        classifier = DummyClassifier()

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitGenericClassifier``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from sklearn.dummy import DummyClassifier
    
    classifier = DummyClassifier()
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
    
    