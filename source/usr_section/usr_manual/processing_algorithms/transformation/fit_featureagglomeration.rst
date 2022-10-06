.. _Fit FeatureAgglomeration:

************************
Fit FeatureAgglomeration
************************

Agglomerate `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.
Recursively merges pair of clusters of features.

**Parameters**


:guilabel:`Transformer` [string]
    Scikit-learn python code. See `FeatureAgglomeration <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html>`_ for information on different parameters.

    Default::

        from sklearn.cluster import FeatureAgglomeration
        
        transformer = FeatureAgglomeration(n_clusters=3)
        

:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ used for fitting the `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_. Mutually exclusive with parameter: `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_


:guilabel:`Sample size` [number]
    Approximate number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ drawn from raster. If 0, whole raster will be used. Note that this is only a hint for limiting the number of rows and columns.

    Default: *1000*


:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_. Mutually exclusive with parameter: `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_

**Outputs**


:guilabel:`Output transformer` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitFeatureagglomeration``::

    ----------------
    Arguments
    ----------------
    
    transformer: Transformer
    	Default value:	from sklearn.cluster import FeatureAgglomeration
    
    transformer = FeatureAgglomeration(n_clusters=3)
    
    	Argument type:	string
    	Acceptable values:
    		- String value
    featureRaster: Raster layer with features (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    sampleSize: Sample size (optional)
    	Default value:	1000
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    dataset: Training dataset (optional)
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputTransformer: Output transformer
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputTransformer: <outputFile>
    	Output transformer
    
    