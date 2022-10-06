.. _Fit PCA:

*******
Fit PCA
*******

Principal component analysis (PCA).
Linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space. The input data is centered but not scaled for each `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ before applying the SVD.

**Parameters**


:guilabel:`Transformer` [string]
    Scikit-learn python code. See `PCA <https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA
        
        pca = PCA(n_components=0.95)
        transformer = make_pipeline(StandardScaler(), pca)

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

``>qgis_process help enmapbox:FitPca``::

    ----------------
    Arguments
    ----------------
    
    transformer: Transformer
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    
    pca = PCA(n_components=0.95)
    transformer = make_pipeline(StandardScaler(), pca)
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
    
    