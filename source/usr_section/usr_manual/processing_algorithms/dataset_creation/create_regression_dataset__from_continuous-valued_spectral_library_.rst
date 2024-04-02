.. _Create regression dataset (from continuous-valued spectral library):

*******************************************************************
Create regression dataset (from continuous-valued spectral library)
*******************************************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ that matches the given `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ variables and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_regression_dataset__from_continuous-valued_spectral_library_.rst

**Parameters**


:guilabel:`Continuous-valued spectral library` [vector]
    `Continuous-valued spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-spectral-library>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ (i.e. `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_) and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. It is assumed, but not enforced, that the spectral characteristics of all spectral profiles match. If not all spectral profiles share the same number of `spectral bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-band>`_, an error is raised.


:guilabel:`Fields with target values` [field]
    Fields with continuous-valued values used as `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If not selected, the `fields <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ defined by the renderer is used. If those are also not specified, an error is raised.


:guilabel:`Field with spectral profiles used as features` [field]
    Field with `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_. If not selected, the default `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ named "profiles" is used. If that is also not available, an error is raised.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRegressionDatasetFromContinuousvaluedSpectralLibrary``::

    ----------------
    Arguments
    ----------------
    
    continuousLibrary: Continuous-valued spectral library
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    targetFields: Fields with target values (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    field: Field with spectral profiles used as features (optional)
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
    
    