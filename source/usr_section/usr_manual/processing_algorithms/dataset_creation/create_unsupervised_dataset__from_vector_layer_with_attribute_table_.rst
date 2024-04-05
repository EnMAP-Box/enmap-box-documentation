.. _Create unsupervised dataset (from vector layer with attribute table):

********************************************************************
Create unsupervised dataset (from vector layer with attribute table)
********************************************************************

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `attribute table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-table>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_unsupervised_dataset__from_vector_layer_with_attribute_table_.rst

**Parameters**


:guilabel:`Vector layer` [vector]
    `Vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ specifying `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Fields with features` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ with values used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromVectorLayerWithAttributeTable``::

    ----------------
    Arguments
    ----------------
    
    vector: Vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    featureFields: Fields with features
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    outputUnsupervisedDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputUnsupervisedDataset: <outputFile>
    	Output dataset
    
    