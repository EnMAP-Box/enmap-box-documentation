.. _Sample raster layer values:

**************************
Sample raster layer values
**************************

Creates a new `point layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-point-layer>`_ with the same `attributes <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute>`_ of the input `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_ and the raster values corresponding to the pixels covered by polygons or point location.
The resulting point vector contains 1) all input attributes from the Locations vector,  2) attributes SAMPLE_{i}, one for each input raster `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_, 3) two attributes PIXEL_X, PIXEL_Y for storing the raster pixel locations (zero-based),and 4), in case of polygon locations, an `attribute <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-attribute>`_ COVER for storing the pixel coverage (%).
Note that we assume non-overlapping `feature <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-feature>`_ geometries! In case of overlapping geometries, split the Locations layer into non-overlapping subsets, perform the sampling for each subset individually, and finally concatenate the results.

**Parameters**


:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ data from.


:guilabel:`Vector layer` [vector]
    A `vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ defining the locations to `sample <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_.


:guilabel:`Pixel coverage (%)` [range]
    `Samples <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-sample>`_ with polygon pixel coverage outside the given range are excluded. This parameter has no effect in case of point locations.

    Default: *[50, 100]*

**Outputs**


:guilabel:`Output point layer` [vectorDestination]
    Vector file destination.

**Command-line usage**

``>qgis_process help enmapbox:SampleRasterLayerValues``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    vector: Vector layer
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    coverageRange: Pixel coverage (%) (optional)
    	Default value:	
    	Argument type:	range
    	Acceptable values:
    		- Two comma separated numeric values, e.g. '1,10'
    outputPointsData: Output point layer
    	Argument type:	vectorDestination
    	Acceptable values:
    		- Path for new vector layer
    
    ----------------
    Outputs
    ----------------
    
    outputPointsData: <outputVector>
    	Output point layer
    
    