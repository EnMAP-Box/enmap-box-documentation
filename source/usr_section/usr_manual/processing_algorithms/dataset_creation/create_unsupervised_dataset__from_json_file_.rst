.. _Create unsupervised dataset (from JSON file):

********************************************
Create unsupervised dataset (from JSON file)
********************************************

Create a unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from a JSON file and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_unsupervised_dataset__from_json_file_.rst

**Parameters**


:guilabel:`JSON file` [file]
    JSON file containing all information.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromJsonFile``::

    ----------------
    Arguments
    ----------------
    
    jsonFile: JSON file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputUnsupervisedDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputUnsupervisedDataset: <outputFile>
    	Output dataset
    
    