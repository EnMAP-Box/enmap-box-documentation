
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-ReclassifyRasterLayer:

***********************
Reclassify raster layer
***********************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

This algorithm reclassifies a raster by assigning new `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ values based on a class mapping.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select a raster to process.

3. Under :guilabel:`Class mapping` note which raster values shall be reclassified by writing the original value, followed by the new value, e. g. [1:1, 2:1, 3:2 ...]. In this example, classes 1 and 2 will be combined into a new class 1, while class 3 will be assigned a new value of 2.

4. Optionally you can define class names and visualisation under :guilabel:`Categories` as seen in the example below. Then, click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/classification/img/reclassify_interface.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    A `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_ to be reclassified.

:guilabel:`Class mapping` [string]
    A list of source to `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ `class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ value mappings. E.g. to merge source values 1 and 2 into target value 1, and source values 3 and 4 into target value 2, use {1:1, 2:1, 3:2, 4:2}

:guilabel:`Categories` [string]
    A list of `target <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-target>`_ `categories <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-categories>`_ in short notation: \[\(1, '`Class <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-class>`_ A', '#e60000'\), \(2, 'Class B', '#267300'\)\]

:guilabel:`No data value` [number]
    Value used to fill no data regions.
    Default: *0*

**Outputs**

:guilabel:`Output classification layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:ReclassifyRasterLayer``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    mapping: Class mapping
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    categories: Categories (optional)
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    noDataValue: No data value
        Default value:    0
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
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

