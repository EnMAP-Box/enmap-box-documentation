.. _Create unsupervised dataset (from feature raster):

*************************************************
Create unsupervised dataset (from feature raster)
*************************************************

Create an unsupervised `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by sampling data from valid pixels and store the result as a `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.
A pixel is concidered valid, if the `pixel profile <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pixel-profile>`_ is free of `no data values <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-no-data-value>`_, and not excluded by the (optionally) selected `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_.

**Parameters**


:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for sampling `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_.


:guilabel:`Mask layer` [layer]
    A `mask layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-mask-layer>`_ for limitting `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ locations.


:guilabel:`Sample size` [number]
    Approximate number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ drawn from raster. If 0, whole raster will be used. Note that this is only a hint for limiting the number of rows and columns.

    Default: *0*

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateUnsupervisedDatasetFromFeatureRaster``::

    ----------------
    Arguments
    ----------------
    
    featureRaster: Raster layer with features
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    mask: Mask layer (optional)
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    sampleSize: Sample size (optional)
    	Default value:	0
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    outputUnsupervisedDataset: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputUnsupervisedDataset: <outputFile>
    	Output dataset
    
    