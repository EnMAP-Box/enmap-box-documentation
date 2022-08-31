.. _Create default paletted raster renderer:

***************************************
Create default paletted raster renderer
***************************************

Create a paletted raster renderer from given `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ and set it as the default style of the given `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.
This will create/overwrite the QML sidecar file of the given raster `layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-layer>`_.

**Parameters**


:guilabel:`Raster layer` [raster]
    The `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ for which to create the QML sidecar file.


:guilabel:`Band` [band]
    The renderer `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.


:guilabel:`Categories` [string]
    Comma separated list of tuples with `category <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-category>`_ value, name and `color <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-color>`_ information. E.g.
    (1, 'Urban', '#FF0000'), (2, 'Forest', '#00FF00'), (3, 'Water', '#0000FF')

**Command-line usage**

``>qgis_process help enmapbox:CreateDefaultPalettedRasterRenderer``::

    ----------------
    Arguments
    ----------------
    
    raster: Raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    band: Band
    	Argument type:	band
    	Acceptable values:
    		- Integer value representing an existing raster band number
    categories: Categories
    	Argument type:	string
    	Acceptable values:
    		- String value
    
    ----------------
    Outputs
    ----------------
    
    
    