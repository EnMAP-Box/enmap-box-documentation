.. _Fit KMeans:

**********
Fit KMeans
**********

K-Means `clustering <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clustering>`_.

.. include:: ../../processing_algorithms_includes/clustering/fit_kmeans.rst

**Parameters**


:guilabel:`Clusterer` [string]
    Scikit-learn python code. See `KMeans <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>`_ for information on different parameters.

    Default::

        from sklearn.cluster import KMeans
        
        clusterer = KMeans(n_clusters=8)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `clusterer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clusterer>`_. If not specified, an unfitted clusterer is created.

**Outputs**


:guilabel:`Output clusterer` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitKmeans``::

    ----------------
    Arguments
    ----------------
    
    clusterer: Clusterer
    	Default value:	from sklearn.cluster import KMeans
    
    clusterer = KMeans(n_clusters=8)
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataset: Training dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputClusterer: Output clusterer
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClusterer: <outputFile>
    	Output clusterer
    
    