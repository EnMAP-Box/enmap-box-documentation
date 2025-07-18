
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-CreateUnsupervisedDatasetFromVectorLayerWithAttributeTable:

********************************************************************
Create unsupervised dataset (from vector layer with attribute table)
********************************************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `attribute table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-table>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Open the algorithm from the processing toolbox.

2. Select a vector layer containing your features, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/dataset_creation/img/clusvector.png
       :align: center

3. The output classification dataset will be listed under Models in your Data Sources panel.

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Vector layer` [vector]
    `Vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ specifying `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.

:guilabel:`Fields with features` [field]
    `Fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ with values used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.

**Outputs**

:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromVectorLayerWithAttributeTable``::

    ----------------
    Arguments
    ----------------

    vector: Vector layer
        Argument type:    vector
        Acceptable values:
            - Path to a vector layer
    featureFields: Fields with features
        Argument type:    field
        Acceptable values:
            - The name of an existing field
            - ; delimited list of existing field names
    outputUnsupervisedDataset: Output dataset
        Argument type:    fileDestination
        Acceptable values:
            - Path for new file

    ----------------
    Outputs
    ----------------

    outputUnsupervisedDataset: <outputFile>
        Output dataset

..
  ## AUTOGENERATED COMMAND USAGE END

