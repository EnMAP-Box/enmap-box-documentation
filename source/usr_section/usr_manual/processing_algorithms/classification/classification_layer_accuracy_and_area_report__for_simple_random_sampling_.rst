.. _Classification layer accuracy and area report (for simple random sampling):

**************************************************************************
Classification layer accuracy and area report (for simple random sampling)
**************************************************************************

Estimates map accuracy and area proportions for (simple) random sampling. We use the formulas for the stratified random sampling described in Stehman (2014): https://doi.org/10.1080/01431161.2014.930207. Note that (simple) random sampling is a special case of stratified random sampling, with exactly one `stratum <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-stratum>`_. 
Observed and predicted `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ are matched by name, if possible. Otherwise, categories are matched by order (in this case, a warning message is logged).

**Parameters**


:guilabel:`Predicted classification layer` [raster]
    A `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ that is to be assessed.


:guilabel:`Observed categorized layer` [layer]
    A `categorized layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-layer>`_ representing a (ground truth) observation `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_, that was aquired using a (simple) random sampling approach.


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:ClassificationLayerAccuracyAndAreaReportForSimpleRandomSampling``::

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
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outClassificationPerformance: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outClassificationPerformance: <outputHtml>
    	Output report
    
    