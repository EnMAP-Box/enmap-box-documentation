.. _Create regression dataset (from continuous-valued raster layer and feature raster):

**********************************************************************************
Create regression dataset (from continuous-valued raster layer and feature raster)
**********************************************************************************

Create a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by sampling data for labeled pixels and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

**Parameters**


:guilabel:`Continuous-valued raster layer` [raster]
    `Continuous-valued raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-raster-layer>`_ specifying `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ locations and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `Y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_.If required, the `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ is reprojected and resampled internally to match the `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ raster `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_.
    


:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for sampling `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Targets` [band]
    Bands with `continuous-valued variables <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-variable>`_ used as `targets <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_. An empty selection defaults to all `bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in native order.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.

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
    outputClassificationDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputClassificationDataset: <outputFile>
    	Output dataset
    
    