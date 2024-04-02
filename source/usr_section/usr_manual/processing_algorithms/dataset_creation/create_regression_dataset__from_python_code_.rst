.. _Create regression dataset (from Python code):

********************************************
Create regression dataset (from Python code)
********************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from Python code and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_regression_dataset__from_python_code_.rst

**Parameters**


:guilabel:`Code` [string]
    Python code specifying the `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

    Default::

        from enmapboxprocessing.typing import Number, List, Target, RegressorDump
        
        # specify targets and feature names
        targets: List[Target] = [
            Target(name='variable 1', color='#ff0000'),
            Target(name='variable 2', color='#00ff00')
        ]
        features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
        
        # specify features X as 2d-array with shape (samples, features)
        X: List[List[Number]] = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        # specify targets y as 2d-array with shape (samples, targets)
        y: List[List[float]] = [
            [1.1, 1.2], [2.1, 2.2]
        ]
        
**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRegressionDatasetFromPythonCode``::

    ----------------
    Arguments
    ----------------
    
    code: Code
    	Default value:	from enmapboxprocessing.typing import Number, List, Target, RegressorDump
    
    # specify targets and feature names
    targets: List[Target] = [
        Target(name='variable 1', color='#ff0000'),
        Target(name='variable 2', color='#00ff00')
    ]
    features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
    
    # specify features X as 2d-array with shape (samples, features)
    X: List[List[Number]] = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    # specify targets y as 2d-array with shape (samples, targets)
    y: List[List[float]] = [
        [1.1, 1.2], [2.1, 2.2]
    ]
    
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRegressionDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressionDataset: <outputFile>
    	Output dataset
    
    