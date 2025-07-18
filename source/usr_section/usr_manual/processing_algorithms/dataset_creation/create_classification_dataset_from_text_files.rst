
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-CreateClassificationDatasetFromTextFiles:

***********************************************
Create classification dataset (from text files)
***********************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from tabulated text files and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

The format matches that of the `FORCE Higher Level Sampling Submodule <https://force-eo.readthedocs.io/en/latest/components/higher-level/smp/index.html>`_.
Example files \(force_features.csv and force_labels.csv\) can be found in the EnMAP-Box testdata folder\).

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Open the algorithm from the processing toolbox.

2. Select or create a classification dataset and specify the number of stratification bins and the number of samples, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/dataset_creation/img/random_samples_reg.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`File with features` [file]
    Text file with tabulated `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ \(no headers\). Each row represents the `feature vector <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature-vector>`_ of a `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

:guilabel:`File with class values` [file]
    Text file with tabulated `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_ \(no headers\). Each row represents the `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ value of a `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

**Outputs**

:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromTextFiles``::

    ----------------
    Arguments
    ----------------

    featureFile: File with features
        Argument type:    file
        Acceptable values:
            - Path to a file
    valueFile: File with class values
        Argument type:    file
        Acceptable values:
            - Path to a file
    outputClassificationDataset: Output dataset
        Argument type:    fileDestination
        Acceptable values:
            - Path for new file

    ----------------
    Outputs
    ----------------

    outputClassificationDataset: <outputFile>
        Output dataset

..
  ## AUTOGENERATED COMMAND USAGE END

