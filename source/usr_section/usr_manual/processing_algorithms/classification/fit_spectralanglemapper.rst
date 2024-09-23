.. _Fit SpectralAngleMapper:

***********************
Fit SpectralAngleMapper
***********************

Spectral Angle Mapper (SAM).
`Samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ are first normalizes to the unit sphere and then classified using nearest neighbour.
See `Docs Center > Using ENVI > Spectral Angle Mapper <https://www.nv5geospatialsoftware.com/docs/SpectralAngleMapper.html>`_ for a more details description.

.. include:: ../../processing_algorithms_includes/classification/fit_spectralanglemapper.rst

**Parameters**


:guilabel:`Classifier` [string]
    Scikit-learn python code. See `Normalizer <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html>`_, `KNeighborsClassifier <https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import Normalizer
        from sklearn.neighbors import KNeighborsClassifier
        
        classifier = make_pipeline(Normalizer(), KNeighborsClassifier(n_neighbors=1))

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output classifier` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitSpectralanglemapper``::

    ----------------
    Arguments
    ----------------
    
    classifier: Classifier
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import Normalizer
    from sklearn.neighbors import KNeighborsClassifier
    
    classifier = make_pipeline(Normalizer(), KNeighborsClassifier(n_neighbors=1))
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
    
    