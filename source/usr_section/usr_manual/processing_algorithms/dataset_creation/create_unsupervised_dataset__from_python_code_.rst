.. _Create unsupervised dataset (from Python code):

**********************************************
Create unsupervised dataset (from Python code)
**********************************************

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from Python code and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_unsupervised_dataset__from_python_code_.rst

**Parameters**


:guilabel:`Code` [string]
    Python code specifying the unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

    Default::

        from enmapboxprocessing.typing import Number, List
        
        # specify feature names
        features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
        
        # specify features X as 2d-array with shape (samples, features)
        X: List[List[Number]] = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        
**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromPythonCode``::

    ----------------
    Arguments
    ----------------
    
    code: Code
    	Default value:	from enmapboxprocessing.typing import Number, List
    
    # specify feature names
    features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
    
    # specify features X as 2d-array with shape (samples, features)
    X: List[List[Number]] = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputUnsupervisedDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputUnsupervisedDataset: <outputFile>
    	Output dataset
    
    