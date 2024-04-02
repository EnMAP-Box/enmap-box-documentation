.. _Fit RobustScaler:

****************
Fit RobustScaler
****************

Scale `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ using statistics that are robust to outliers.
This Scaler removes the median and scales the data according to the quantile range (defaults to IQR: Interquartile Range). The IQR is the range between the 1st quartile (25th quantile) and the 3rd quartile (75th quantile).
Centering and scaling happen independently on each `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ by computing the relevant statistics on the `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ in the training set. Median and interquartile range are then stored to be used on later data using the transform method.
Standardization of a `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ is a common requirement for many machine learning `estimators <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-estimator>`_. Typically this is done by removing the mean and scaling to unit variance. However, outliers can often influence the `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ mean / variance in a negative way. In such cases, the median and the interquartile range often give better results.

.. include:: ../../processing_algorithms_includes/transformation/fit_robustscaler.rst

**Parameters**


:guilabel:`Transformer` [string]
    Scikit-learn python code. See `RobustScaler <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html>`_ for information on different parameters.

    Default::

        from sklearn.preprocessing import RobustScaler
        
        transformer = RobustScaler(quantile_range=(25, 75))

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

``>qgis_process help enmapbox:FitRobustscaler``::

    ----------------
    Arguments
    ----------------
    
    transformer: Transformer
    	Default value:	from sklearn.preprocessing import RobustScaler
    
    transformer = RobustScaler(quantile_range=(25, 75))
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
    
    