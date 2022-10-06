.. _Classification layer accuracy and area report (for stratified random sampling):

******************************************************************************
Classification layer accuracy and area report (for stratified random sampling)
******************************************************************************

Estimates map accuracy and area proportions for stratified random sampling as described in Stehman (2014): https://doi.org/10.1080/01431161.2014.930207. 
Observed and predicted `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ are matched by name.

**Parameters**


:guilabel:`Predicted classification layer` [raster]
    A `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ that is to be assessed.


:guilabel:`Observed categorized layer` [layer]
    A `categorized layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-layer>`_ representing a (ground truth) observation `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_, that was aquired using a stratified random sampling approach.


:guilabel:`Stratification layer` [layer]
    A `stratification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-stratification-layer>`_ that was used for drawing the observation `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_. If not defined, the `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ is used as stratification `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassificationLayerAccuracyAndAreaReportForStratifiedRandomSampling``::

    ----------------
    Arguments
    ----------------
    
    classification: Predicted classification layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    reference: Observed categorized layer
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    stratification: Stratification layer (optional)
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    outClassificationPerformance: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outClassificationPerformance: <outputHtml>
    	Output report
    
    