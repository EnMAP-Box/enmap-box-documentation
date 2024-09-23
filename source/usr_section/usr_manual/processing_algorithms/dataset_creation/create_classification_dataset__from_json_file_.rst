.. _Create classification dataset (from JSON file):

**********************************************
Create classification dataset (from JSON file)
**********************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from a JSON file and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_. 
Example file (`classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_.pkl.json) can be found in the EnMAP-Box testdata folder).

**Parameters**


:guilabel:`JSON file` [file]
    JSON file containing all information.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromJsonFile``::

    ----------------
    Arguments
    ----------------
    
    jsonFile: JSON file
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    