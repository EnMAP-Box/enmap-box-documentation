.. _Create unsupervised dataset (from spectral library):

***************************************************
Create unsupervised dataset (from spectral library)
***************************************************

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Parameters**


:guilabel:`Spectral library` [vector]
    `Spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-library>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ (i.e. `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_). It is assumed, but not enforced, that the spectral characteristics of all spectral profiles match. If not all spectral profiles share the same number of `spectral bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-band>`_, an error is raised.


:guilabel:`Field with spectral profiles used as features` [field]
    Field with `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_. If not selected, the default `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ named "profiles" is used. If that is also not available, an error is raised.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromSpectralLibrary``::

    ----------------
    Arguments
    ----------------
    
    library: Spectral library
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    field: Field with spectral profiles used as features (optional)
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
    
    