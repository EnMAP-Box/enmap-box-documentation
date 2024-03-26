.. _Receiver operating characteristic (ROC) and detection error tradeoff (DET) curves:

*********************************************************************************
Receiver operating characteristic (ROC) and detection error tradeoff (DET) curves
*********************************************************************************

Compute receiver operating characteristic (ROC) and detection error tradeoff (DET) curves.
For more details see the Scikit-Learn user guide: `Receiver operating characteristic (ROC) <https://scikit-learn.org/stable/modules/model_evaluation.html#receiver-operating-characteristic-roc>`_ and `Detection error tradeoff (DET) <https://scikit-learn.org/stable/modules/model_evaluation.html#detection-error-tradeoff-det>`_.
Note that observed classes and predicted `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ probabilities are matched by name.

**Parameters**


:guilabel:`Class probability layer` [raster]
    A `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ that is to be assessed.


:guilabel:`Observed categorized layer` [layer]
    A `categorized layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-layer>`_ representing a (ground truth) observation `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:ReceiverOperatingCharacteristicRocAndDetectionErrorTradeoffDetCurves``::

    ----------------
    Arguments
    ----------------
    
    regression: Class probability layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    reference: Observed categorized layer
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
    outRocCurve: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outRocCurve: <outputHtml>
    	Output report
    
    