.. _Random samples from regression dataset:

**************************************
Random samples from regression dataset
**************************************

Split a `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ by randomly drawing `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.

**Parameters**


:guilabel:`Regression dataset` [file]
    `Regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_ `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_ with `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ data `X <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-x>`_ and `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ data `y <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-y>`_ to draw from.


:guilabel:`Number of stratification bins` [number]
    Number of bins used to stratify the `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ range.

    Default: *1*


:guilabel:`Number of samples per bin` [string]
    Number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ to draw from each bin. Set a single value N to draw N samples for each bin. Set a list of values N1, N2, ... Ni, ... to draw Ni samples for bin i.


:guilabel:`Draw with replacement` [boolean]
    Whether to draw `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ with replacement.

    Default: *False*


:guilabel:`Draw proportional` [boolean]
    Whether to interprete number of `samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ N or Ni as percentage to be drawn from each bin.

    Default: *False*


:guilabel:`Random seed` [number]
    The seed for the random generator can be provided.

**Outputs**


:guilabel:`Output dataset` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.Stores sampled data.


:guilabel:`Output dataset complement` [fileDestination]
    Destination `pickle file <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-pickle-file>`_.Stores remaining data that was not sampled.

**Command-line usage**

``>qgis_process help enmapbox:RandomSamplesFromRegressionDataset``::

    ----------------
    Arguments
    ----------------
    
    dataset: Regression dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    bins: Number of stratification bins
    	Default value:	1
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    n: Number of samples per bin
    	Argument type:	string
    	Acceptable values:
    		- String value
    replace: Draw with replacement
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    proportional: Draw proportional
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    seed: Random seed (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    outputDatasetRandomSample: Output dataset
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputDatasetRandomSampleComplement: Output dataset complement (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    
    ----------------
    Outputs
    ----------------
    
    outputDatasetRandomSample: <outputFile>
    	Output dataset
    outputDatasetRandomSampleComplement: <outputFile>
    	Output dataset complement
    
    