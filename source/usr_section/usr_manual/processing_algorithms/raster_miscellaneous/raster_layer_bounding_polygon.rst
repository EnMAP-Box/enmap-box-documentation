
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-RasterLayerBoundingPolygon:

*****************************
Raster layer bounding polygon
*****************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Compute `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ bounding polygon that encloses all data pixel in a `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_.

..
  ## AUTOGENERATED DESCRIPTION END

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ used for bounding polygon calculation.

:guilabel:`Band` [band]
    A `band <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-band>`_ used for calculation.

:guilabel:`Geometry type` [enum]
    Enclosing geometry type.
    Default: *3*

**Outputs**

:guilabel:`Output vector layer` [vectorDestination]
    Vector file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:RasterLayerBoundingPolygon``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    band: Band
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    geometryType: Geometry type (optional)
        Default value:    3
        Argument type:    enum
        Available values:
            - 0: Envelope (Bounding Box)
            - 1: Minimum Oriented Rectangle
            - 2: Minimum Enclosing Circle
            - 3: Convex Hull
        Acceptable values:
            - Number of selected option, e.g. '1'
            - Comma separated list of options, e.g. '1,3'
    outputVector: Output vector layer
        Argument type:    vectorDestination
        Acceptable values:
            - Path for new vector layer

    ----------------
    Outputs
    ----------------

    outputVector: <outputVector>
        Output vector layer

..
  ## AUTOGENERATED COMMAND USAGE END

