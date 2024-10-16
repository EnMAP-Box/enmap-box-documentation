.. _Create regression dataset (from continuous-valued raster layer and feature raster):

**********************************************************************************
Create regression dataset (from continuous-valued raster layer and feature raster)
**********************************************************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by sampling data for labeled pixels and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

.. include:: ../../processing_algorithms_includes/dataset_creation/create_regression_dataset__from_continuous-valued_raster_layer_and_feature_raster_.rst

**Parameters**


:guilabel:`Continuous-valued raster layer` [raster]
    `Continuous-valued raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-raster-layer>`_ specifying `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ locations and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `Y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_.If required, the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is reprojected and resampled internally to match the `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ raster `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.
    


:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for sampling `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Targets` [band]
    Bands with `continuous-valued variables <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-variable>`_ used as `targets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_. An empty selection defaults to all `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in native order.


:guilabel:`Exclude bad bands` [boolean]
    Whether to exclude `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_, that are marked as `bad bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-bad-band>`_, or contain no data, inf or nan values in all `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

    Default: *True*

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRegressionDatasetFromContinuousvaluedRasterLayerAndFeatureRaster``::

    ----------------
    Arguments
    ----------------
    
    continuousRaster: Continuous-valued raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    featureRaster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    targets: Targets (optional)
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    excludeBadBands: Exclude bad bands (optional)
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputRegressionDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressionDataset: <outputFile>
    	Output dataset
    
    