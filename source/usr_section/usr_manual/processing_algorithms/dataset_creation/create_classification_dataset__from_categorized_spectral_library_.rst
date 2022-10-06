.. _Create classification dataset (from categorized spectral library):

*****************************************************************
Create classification dataset (from categorized spectral library)
*****************************************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ from `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ that matches the given `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.
If the `spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-library>`_ is not categorized, or the `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values is selected manually, categories are derived from `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. To be more precise: i) `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ values are derived from unique `attribute values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-value>`_ (after excluding no data or zero data values), ii) category names are set equal to the category values, and iii) category `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ are picked randomly.

**Parameters**


:guilabel:`Categorized spectral library` [vector]
    `Categorized spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-spectral-library>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ (i.e. `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_) and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. It is assumed, but not enforced, that the spectral characteristics of all spectral profiles match. If not all spectral profiles share the same number of `spectral bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-band>`_, an error is raised.


:guilabel:`Field with class values` [field]
    Field with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values used as `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If not selected, the `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ defined by the renderer is used. If that is also not specified, an error is raised.


:guilabel:`Field with spectral profiles used as features` [field]
    Field with `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_ used as `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_. If not selected, the default `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ named "profiles" is used. If that is also not available, an error is raised.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromCategorizedSpectralLibrary``::

    ----------------
    Arguments
    ----------------
    
    categorizedLibrary: Categorized spectral library
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    categoryField: Field with class values (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    field: Field with spectral profiles used as features (optional)
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
    
    