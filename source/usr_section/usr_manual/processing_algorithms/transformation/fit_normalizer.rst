.. _Fit Normalizer:

**************
Fit Normalizer
**************

Normalize `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ individually to unit norm.
Each `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ (i.e. each row of the data matrix) with at least one non zero component is rescaled independently of other samples so that its norm (l1, l2 or inf) equals one.

.. include:: ../../processing_algorithms_includes/transformation/fit_normalizer.rst

**Parameters**


:guilabel:`Transformer` [string]
    Scikit-learn python code. See `Normalizer <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html>`_ for information on different parameters.

    Default::

        from sklearn.preprocessing import Normalizer
        
        transformer = Normalizer()

:guilabel:`Raster layer with features` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ used for fitting the `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_. Mutually exclusive with parameter: `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_


:guilabel:`Sample size` [number]
    Approximate number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ drawn from raster. If 0, whole raster will be used. Note that this is only a hint for limiting the number of rows and columns.

    Default: *1000*


:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `transformer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-transformer>`_. Mutually exclusive with parameter: `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_

**Outputs**


:guilabel:`Output transformer` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitNormalizer``::

    ----------------
    Arguments
    ----------------
    
    transformer: Transformer
    	Default value:	from sklearn.preprocessing import Normalizer
    
    transformer = Normalizer()
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    featureRaster: Raster layer with features (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    sampleSize: Sample size (optional)
    	Default value:	1000
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    dataset: Training dataset (optional)
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputTransformer: Output transformer
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputTransformer: <outputFile>
    	Output transformer
    
    