.. _Create regression dataset (from Python code):

********************************************
Create regression dataset (from Python code)
********************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from Python code and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

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
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

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
    outputRegressionDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressionDataset: <outputFile>
    	Output dataset
    
    