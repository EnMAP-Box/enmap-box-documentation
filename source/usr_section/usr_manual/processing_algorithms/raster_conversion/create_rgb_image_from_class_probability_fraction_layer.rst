.. _Create RGB image from class probability/fraction layer:

******************************************************
Create RGB image from class probability/fraction layer
******************************************************

Create an `RGB image <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-rgb-image>`_ from a `class fraction layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-fraction-layer>`_ or `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_.The RGB pixel `color <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ of a single pixel is given by the weighted mean of the given `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_.The weights are given by `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ fractions/probabilities (i.e. values between 0 and 1).
For example, pure pixels with cover fractions of 1 appear in its pure category color. A mixed-pixel with a 50% fractions in two `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ colored in red and green,appears in a dull yellow ( 0.5 x (255, 0, 0) + 0.5 x (0, 255, 0) = (127, 127, 0) ).

**Parameters**


:guilabel:`Class probability/fraction layer` [raster]
    A `class fraction layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-fraction-layer>`_ or `class probability layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class-probability-layer>`_ used as weights for calculating final pixel `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_.


:guilabel:`Colors` [string]
    Comma separated list of `hex-color <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-hex-color>`_ strings (e.g. '#FF0000' for red) representing (pure) `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_, one `color <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ for each `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in the given `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ probability/fraction `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_. If not specified, colors have to be specified by a `categorized layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-layer>`_ (Colors from categorized layer).


:guilabel:`Colors from categorized layer` [layer]
    A `categorized layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categorized-layer>`_ with (pure) `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ `colors <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_, one category for each `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ in the given `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ probability/fraction `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_. If not specified, colors have to be specified by list (Colors).

**Outputs**


:guilabel:`Output RGB image` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:CreateRgbImageFromClassProbabilityfractionLayer``::

    ----------------
    Arguments
    ----------------
    
    probability: Class probability/fraction layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    colors: Colors (optional)
    	Argument type:	string
    	Acceptable values:
    		- String value
    colorsLayer: Colors from categorized layer (optional)
    	Argument type:	layer
    	Acceptable values:
    		- Path to a vector, raster or mesh layer
    outputRGBImage: Output RGB image
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputRGBImage: <outputRaster>
    	Output RGB image
    
    