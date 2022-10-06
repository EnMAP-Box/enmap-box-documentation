.. _Fit GaussianProcessRegressor:

****************************
Fit GaussianProcessRegressor
****************************

Gaussian process `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ (GPR).

**Parameters**


:guilabel:`Regressor` [string]
    Scikit-learn python code. See `GaussianProcessRegressor <https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html>`_ for information on different parameters.

    Default::

        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.gaussian_process import GaussianProcessRegressor
        from sklearn.gaussian_process.kernels import RBF
        
        gpr = GaussianProcessRegressor(RBF())
        regressor = make_pipeline(StandardScaler(), gpr)

:guilabel:`Training dataset` [file]
    `Training dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-training-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ used for fitting the `classifier <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classifier>`_. If not specified, an unfitted classifier is created.

**Outputs**


:guilabel:`Output regressor` [fileDestination]
    `Pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ destination.

**Command-line usage**

``>qgis_process help enmapbox:FitGaussianprocessregressor``::

    ----------------
    Arguments
    ----------------
    
    regressor: Regressor
    	Default value:	from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.gaussian_process import GaussianProcessRegressor
    from sklearn.gaussian_process.kernels import RBF
    
    gpr = GaussianProcessRegressor(RBF())
    regressor = make_pipeline(StandardScaler(), gpr)
    	Argument type:	string
    	Acceptable values:
    		- String value
    dataset: Training dataset (optional)
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputRegressor: Output regressor
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputRegressor: <outputFile>
    	Output regressor
    
    