.. _Create regression dataset (from continuous-valued vector layer with attribute table):

************************************************************************************
Create regression dataset (from continuous-valued vector layer with attribute table)
************************************************************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `attribute table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-table>`_ rows that matches the given `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ variables and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Parameters**


:guilabel:`Continuous-valued vector layer` [vector]
    `Continuous-valued vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-vector-layer>`_ specifying `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_.


:guilabel:`Fields with features` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ with values used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Fields with targets` [field]
    Fields with values used as used as `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If not selected, the `fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ defined by the renderer are used. If those are also not specified, an error is raised.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRegressionDatasetFromContinuousvaluedVectorLayerWithAttributeTable``::

    ----------------
    Arguments
    ----------------
    
    continuousVector: Continuous-valued vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    featureFields: Fields with features
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    targetFields: Fields with targets (optional)
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
    
    