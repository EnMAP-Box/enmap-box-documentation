.. _Create unsupervised dataset (from text file):

********************************************
Create unsupervised dataset (from text file)
********************************************

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from a tabulated text file and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_. 
The format matches that of the `FORCE Higher Level Sampling Submodule <https://force-eo.readthedocs.io/en/latest/components/higher-level/smp/index.html>`_.
An example file (force_features.csv) can be found in the EnMAP-Box testdata folder).

.. include:: ../../processing_algorithms_includes/dataset_creation/create_unsupervised_dataset__from_text_file_.rst

**Parameters**


:guilabel:`File with features` [file]
    Text file with tabulated `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ (no headers). Each row represents the `feature vector <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature-vector>`_ of a `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromTextFile``::

    ----------------
    Arguments
    ----------------
    
    featureFile: File with features
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputUnsupervisedDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputUnsupervisedDataset: <outputFile>
    	Output dataset
    
    