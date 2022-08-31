.. _Create classification dataset (from Python code):

************************************************
Create classification dataset (from Python code)
************************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from Python code and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Parameters**


:guilabel:`Code` [string]
    Python code specifying the `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

    Default::

        from enmapboxprocessing.typing import Number, List, Category, ClassifierDump
        
        # specify categories and feature names
        categories: List[Category] = [
            Category(value=1, name='class 1', color='#ff0000'),
            Category(value=2, name='class 2', color='#00ff00')
        ]
        features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
        
        # specify features X as 2d-array with shape (samples, features)
        X: List[List[Number]] = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        # specify targets y as 2d-array with shape (samples, 1)
        y: List[List[int]] = [
            [1], [2]
        ]
        
**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromPythonCode``::

    ----------------
    Arguments
    ----------------
    
    code: Code
    	Default value:	from enmapboxprocessing.typing import Number, List, Category, ClassifierDump
    
    # specify categories and feature names
    categories: List[Category] = [
        Category(value=1, name='class 1', color='#ff0000'),
        Category(value=2, name='class 2', color='#00ff00')
    ]
    features: List[str] = ['Feature 1', 'Feature 2', 'Feature 3']
    
    # specify features X as 2d-array with shape (samples, features)
    X: List[List[Number]] = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    # specify targets y as 2d-array with shape (samples, 1)
    y: List[List[int]] = [
        [1], [2]
    ]
    
    	Argument type:	string
    	Acceptable values:
    		- String value
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    