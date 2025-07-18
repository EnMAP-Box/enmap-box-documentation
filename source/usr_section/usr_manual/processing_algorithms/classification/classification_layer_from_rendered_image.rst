
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-ClassificationLayerFromRenderedImage:

****************************************
Classification layer from rendered image
****************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Creates `classification layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-classification-layer>`_ from a rendered image. Classes are derived from the unique renderer RGBA values.

..
  ## AUTOGENERATED DESCRIPTION END

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    The `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be classified.

**Outputs**

:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:ClassificationLayerFromRenderedImage``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    outputClassification: Output classification layer
        Argument type:    rasterDestination
        Acceptable values:
            - Path for new raster layer

    ----------------
    Outputs
    ----------------

    outputClassification: <outputRaster>
        Output classification layer

..
  ## AUTOGENERATED COMMAND USAGE END

