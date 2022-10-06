.. _Merge classification datasets:

*****************************
Merge classification datasets
*****************************

Merges a list of `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `datasets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

**Parameters**


:guilabel:`Datasets` [multilayer]
    `Classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `datasets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ to be merged.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:MergeClassificationDatasets``::

    ----------------
    Arguments
    ----------------
    
    datasets: Datasets
    	Argument type:	multilayer
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    