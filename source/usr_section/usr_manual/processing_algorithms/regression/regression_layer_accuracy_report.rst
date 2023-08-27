.. _Regression layer accuracy report:

********************************
Regression layer accuracy report
********************************

Estimates map accuracy.We use the formulas as described in `Scikit-Learn Regression metrics <https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics>`_ user guide. Observed and predicted `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ variables are matched by name.

**Parameters**


:guilabel:`Regression layer` [raster]
    A `regression layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression-layer>`_ that is to be assessed.


:guilabel:`Observed continuous-valued layer` [layer]
    A `continuous-valued layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-continuous-valued-layer>`_ representing a (ground truth) observation `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:RegressionLayerAccuracyReport``::

    ----------------
    Arguments
    ----------------
    
    regression: Regression layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    reference: Observed continuous-valued layer
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outRegressionPerformance: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outRegressionPerformance: <outputHtml>
    	Output report
    
    