.. _Create regression dataset (from table with target and feature fields):

*********************************************************************
Create regression dataset (from table with target and feature fields)
*********************************************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `attribute table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-table>`_ rows and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_regression_dataset__from_table_with_target_and_feature_fields_.rst


**Parameters**


:guilabel:`Table` [vector]
    `Table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_.


:guilabel:`Fields with features` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. Values may be given as strings, but must be castable to float.


:guilabel:`Fields with targets` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `targets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_. Values may be given as strings, but must be castable to float.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRegressionDatasetFromTableWithTargetAndFeatureFields``::

    ----------------
    Arguments
    ----------------
    
    table: Table
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    featureFields: Fields with features
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    targetFields: Fields with targets
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    outputRegressionDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressionDataset: <outputFile>
    	Output dataset
    
    