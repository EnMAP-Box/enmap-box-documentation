.. _Select features from dataset:

****************************
Select features from dataset
****************************

Subset and/or reorder `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ in `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.

**Parameters**


:guilabel:`Dataset` [file]
    `Dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ to select `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ from.


:guilabel:`Selected features` [string]
    Comma separated list of `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ names or positions. E.g. use <code>1, 'Feature 2', 3</code> to select the first three `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Command-line usage**

``>qgis_process help enmapbox:SelectFeaturesFromDataset``::

    ----------------
    Arguments
    ----------------
    
    dataset: Dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    featureList: Selected features
    	Argument type:	string
    	Acceptable values:
    		- String value
    outputDatasetFeatureSubset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputDatasetFeatureSubset: <outputFile>
    	Output dataset
    
    