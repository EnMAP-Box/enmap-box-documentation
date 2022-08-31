.. _Raster math:

***********
Raster math
***********

Perform mathematical calculations on `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ and `vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ data. Use any `NumPy <https://numpy.org/doc/stable/reference/>`_-based arithmetic, or even arbitrary Python code.
See the `RasterMath cookbook recipe <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/raster_math.html>`_ for detailed usage instructions.

**Parameters**


:guilabel:`Code` [string]
    The mathematical calculation to be performed on the selected input arrays.
    Select inputs in the available data sources section or use the `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ R1, ..., R10 and `vector layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-vector-layer>`_ V1, ..., V10.
    In the code snippets section you can find some prepdefined code snippets ready to use.
    See the `RasterMath cookbook recipe <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/raster_math.html>`_ for detailed usage instructions.


:guilabel:`Grid` [raster]
    The destination `grid <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-grid>`_. If not specified, the grid of the first `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ is used.


:guilabel:`32-bit floating-point inputs` [boolean]
    Whether to  cast inputs to 32-bit floating point.

    Default: *True*


:guilabel:`Block overlap` [number]
    The number of columns and rows to read from the neighbouring blocks. Needs to be specified only when performing spatial operations, to avoid artifacts at block borders.


:guilabel:`Monolithic processing` [boolean]
    Whether to read all data for the full extent at once, instead of block-wise processing. This may be useful for some spatially unbound operations, like segmentation or region growing, when calculating global statistics, or if RAM is not an issue at all.

    Default: *False*


:guilabel:`Raster layers mapped to RS` [multilayer]
    Additional list of `raster layers <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ mapped to a list variable RS.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination for writing the default `output <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-output>`_ variable. Additional `outputs <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-output>`_ are written into the same directory. See the `RasterMath cookbook recipe <https://enmap-box.readthedocs.io/en/latest/usr_section/usr_cookbook/raster_math.html>`_ for detailed usage instructions.

**Command-line usage**

``>qgis_process help enmapbox:RasterMath``::

    ----------------
    Arguments
    ----------------
    
    code: Code
    	Argument type:	string
    	Acceptable values:
    		- String value
    grid: Grid (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    floatInput: 32-bit floating-point inputs
    	Default value:	true
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    overlap: Block overlap (optional)
    	Argument type:	number
    	Acceptable values:
    		- A numeric value
    monolithic: Monolithic processing (optional)
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    R1: Raster layer mapped to R1 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R2: Raster layer mapped to R2 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R3: Raster layer mapped to R3 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R4: Raster layer mapped to R4 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R5: Raster layer mapped to R5 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R6: Raster layer mapped to R6 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R7: Raster layer mapped to R7 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R8: Raster layer mapped to R8 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R9: Raster layer mapped to R9 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    R10: Raster layer mapped to R10 (optional)
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    V1: Vector layer mapped to V1 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V2: Vector layer mapped to V2 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V3: Vector layer mapped to V3 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V4: Vector layer mapped to V4 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V5: Vector layer mapped to V5 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V6: Vector layer mapped to V6 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V7: Vector layer mapped to V7 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V8: Vector layer mapped to V8 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V9: Vector layer mapped to V9 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    V10: Vector layer mapped to V10 (optional)
    	Argument type:	vector
    	Acceptable values:
    		- Path to a vector layer
    RS: Raster layers mapped to RS (optional)
    	Argument type:	multilayer
    outputRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRaster: <outputRaster>
    	Output raster layer
    
    