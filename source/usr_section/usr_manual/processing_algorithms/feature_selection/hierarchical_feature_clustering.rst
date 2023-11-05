.. _Hierarchical feature clustering:

*******************************
Hierarchical feature clustering
*******************************

Evaluate `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ multicollinearity by performing hierarchical/agglomerative `clustering <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-clustering>`_ with Ward linkage using squared Spearman rank-order correlation as distance between `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_. The result report includes i) pairwise squared Spearman rank-order correlation matrix, ii) clustering dendrogram, iii) inter-cluster correlation distribution, iv) intra-cluster correlation distribution, and v) a clustering hierarchy `table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ detailing selected cluster representatives for each cluster size n.
For further analysis, all relevant results are also stored as a JSON sidecar file next to the report.

.. include:: ../../processing_algorithms_includes/feature_selection/hierarchical_feature_clustering.rst

**Parameters**


:guilabel:`Dataset` [file]
    `Dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ to be evaluated.


:guilabel:`Do not report plots` [boolean]
    Skip the creation of plots, which can take a lot of time for large `features <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ sets.

    Default: *False*


:guilabel:`Open output report in webbrowser after running algorithm` [boolean]
    Whether to open the output report in the web browser.

    Default: *True*

**Outputs**


:guilabel:`Output report` [fileDestination]
    Report file destination.

**Command-line usage**

``>qgis_process help enmapbox:HierarchicalFeatureClustering``::

    ----------------
    Arguments
    ----------------
    
    dataset: Dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    noPlot: Do not report plots
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    openReport: Open output report in webbrowser after running algorithm
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputHierarchicalFeatureClustering: Output report
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputHierarchicalFeatureClustering: <outputHtml>
    	Output report
    
    