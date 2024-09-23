.. _Create spectral library (from regression dataset):

*************************************************
Create spectral library (from regression dataset)
*************************************************

Create a `spectral library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-library>`_ from a `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

**Parameters**


:guilabel:`Dataset` [file]
    A `regression <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-regression>`_ `dataset <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-dataset>`_.

**Outputs**


:guilabel:`Output spectral library` [vectorDestination]
    Vector file destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateSpectralLibraryFromRegressionDataset``::

    ----------------
    Arguments
    ----------------
    
    dataset: Dataset
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputLibrary: Output spectral library
    	Argument type:	vectorDestination
    	Acceptable values:
    		- Path for new vector layer
    
    ----------------
    Outputs
    ----------------
    
    outputLibrary: <outputVector>
    	Output spectral library
    
    