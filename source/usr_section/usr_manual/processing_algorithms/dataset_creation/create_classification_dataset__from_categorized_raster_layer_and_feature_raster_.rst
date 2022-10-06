.. _Create classification dataset (from categorized raster layer and feature raster):

********************************************************************************
Create classification dataset (from categorized raster layer and feature raster)
********************************************************************************

Create a `classification <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by sampling data for pixels that match the given `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_. 
If the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is not categorized, or the `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values is selected manually, categories are derived from sampled data itself. To be more precise: i) `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ values are derived from unique raster band values (after excluding no data or zero data pixel), ii) category names are set equal to the category values, and iii) category `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ are picked randomly.

**Parameters**


:guilabel:`Categorized raster layer` [raster]
    `Categorized raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-raster-layer>`_ specifying `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ locations and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_. If required, the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is reprojected and resampled internally to match the `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ raster `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.
    


:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for sampling `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Band with class values` [band]
    Band with `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values. If not selected, the `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ defined by the renderer is used. If that is also not specified, the first band is used.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateClassificationDatasetFromCategorizedRasterLayerAndFeatureRaster``::

    ----------------
    Arguments
    ----------------
    
    categorizedRaster: Categorized raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    featureRaster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    categoryBand: Band with class values (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    