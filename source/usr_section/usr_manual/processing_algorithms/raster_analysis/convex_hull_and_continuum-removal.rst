.. _Convex hull and continuum-removal:

*********************************
Convex hull and continuum-removal
*********************************

Calculate convex hull and continuum-removed `raster layers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

.. include:: ../../processing_algorithms_includes/raster_analysis/convex_hull_and_continuum-removal.rst


**Parameters**


:guilabel:`Raster layer` [raster]
    `Raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ with `spectral profiles <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-profile>`_.


:guilabel:`X units` [enum]
    The x units used for convex hull calculations. In case of Nanometers, only `spectral bands <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-band>`_ are used.

    Default: *0*

**Outputs**


:guilabel:`Output convex hull raster layer` [rasterDestination]
    Raster file destination.


:guilabel:`Output continuum removed raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:ConvexHullAndContinuumremoval``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    xUnits: X units
    	Default value:	0
    	Argument type:	enum
    	Available values:
    		- 0: Band numbers
    		- 1: Nanometers
    	Acceptable values:
    		- Number of selected option, e.g. '1'
    		- Comma separated list of options, e.g. '1,3'
    outputConvexHull: Output convex hull raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    outputContinuumRemoved: Output continuum removed raster layer (optional)
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputConvexHull: <outputRaster>
    	Output convex hull raster layer
    outputContinuumRemoved: <outputRaster>
    	Output continuum removed raster layer
    
    