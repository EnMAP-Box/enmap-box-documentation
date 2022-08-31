.. _Create classification dataset (from categorized vector layer and feature raster):

********************************************************************************
Create classification dataset (from categorized vector layer and feature raster)
********************************************************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by sampling data for pixels that match the given `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.
If the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is not categorized, or the `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values is selected manually, categories are derived from the sampled `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. To be more precise: i) `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ values are derived from unique `attribute values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute-value>`_ (after excluding no data or zero data values), ii) category names are set equal to the category values, and iii) category `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ are picked randomly.

**Parameters**


:guilabel:`Categorized vector layer` [vector]
    `Categorized vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-vector-layer>`_ specifying `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ locations and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If required, the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is reprojected and rasterized internally to match the `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ raster `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.


:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for sampling `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Field with class values` [field]
    Field with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values used as `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If not selected, the `field <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-field>`_ defined by the renderer is used. If that is also not specified, an error is raised.


:guilabel:`Minimum pixel coverage` [number]
    Exclude all pixel where (polygon) coverage is smaller than given threshold.

    Default: *50*


:guilabel:`Majority voting` [boolean]
    Whether to use majority voting. Turn off to use simple nearest neighbour resampling, which is much faster, but may result in highly inaccurate `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ decisions.

    Default: *True*

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromCategorizedVectorLayerAndFeatureRaster``::

    ----------------
    Arguments
    ----------------
    
    categorizedVector: Categorized vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    featureRaster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    categoryField: Field with class values (optional)
    	Argument type:	field
    	Acceptable values:
    		- The name of an existing field
    		- ; delimited list of existing field names
    coverage: Minimum pixel coverage
    	Default value:	50
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    majorityVoting: Majority voting
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    