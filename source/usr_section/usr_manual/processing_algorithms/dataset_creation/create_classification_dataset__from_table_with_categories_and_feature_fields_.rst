.. _Create classification dataset (from table with categories and feature fields):

*****************************************************************************
Create classification dataset (from table with categories and feature fields)
*****************************************************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `attribute table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-table>`_ rows that match the given `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_. 


**Parameters**


:guilabel:`Table` [vector]
    `Table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_.


:guilabel:`Fields with features` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. Values may be given as strings, but must be castable to float.


:guilabel:`Field with class values` [field]
    `Field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ value.


:guilabel:`Field with class names` [field]
    `Field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ name. If not specified, class values are used as class names.


:guilabel:`Field with class colors` [field]
    `Field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ used as `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ `color <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_. Values may be given as `hex-colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-hex-color>`_, `rgb-colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-rgb-color>`_ or `int-colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-int-color>`_.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromTableWithCategoriesAndFeatureFields``::

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
    valueField: Field with class values
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    nameField: Field with class names (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    colorField: Field with class colors (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    