
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-CreateSpectralIndices:

***********************
Create spectral indices
***********************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Create a stack of `Awesome Spectral Indices <https://awesome-ee-spectral-indices.readthedocs.io/en/latest/list.html>`_ and/or custom indices.
Credits: the Awesome Spectral Indices project provides a ready-to-use curated list of Spectral Indices for Remote Sensing applications, maintained by `David Montero Loaiza <https://github.com/davemlz>`_.

Note that the list of available indices was last updated on 2021-11-15. Should you need other indices added after this date, please file an issue.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Open the algorithm from the processing toolbox.

2. Select a raster layer and define the spectral index to be computed. Optionally, define the bands needed under :guilabel:`Advanced Parameters`. Then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/raster_analysis/img/spectral_index.png
       :align: center

3. The output raster can be found under :guilabel:`Rasters` in the :guilabel:`Data Source Panel`

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_.

:guilabel:`Indices` [string]
    The list of indices to be created. Usage examples:
    Create \(predefined\) NDVI: \<code\>NDVI\</code\>
    Create stack of NDVI and EVI: \<code\>NDVI, EVI\</code\>
    Create custom index: \<code\>MyNDVI = \(N - R\) / \(N + R\)\</code\>
    See the full list of predefined  `Awesome Spectral Indices <https://awesome-ee-spectral-indices.readthedocs.io/en/latest/list.html>`_.
    Default: *NDVI*

:guilabel:`Scale factor` [number]
    Spectral reflectance scale factor. Some indices require data to be scaled into the 0 to 1 range. If your data is scaled differently, specify an appropriate scale factor.E.g. for Int16 data scaled into the 0 to 10000 range, use a value of 10000.

:guilabel:`Formulars` [file]
    A JSON file with additional spectral index formulars to be used.
    See `createspectralindicesalgorithm.other.json <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/enmapboxprocessing/algorithm/createspectralindicesalgorithm.other.json>`_ for the expected format.

:guilabel:`Aerosols band` [band]

    Default: *-1*

:guilabel:`Blue band` [band]

    Default: *-1*

:guilabel:`Green band` [band]

    Default: *-1*

:guilabel:`Red band` [band]

    Default: *-1*

:guilabel:`Red Edge 1 band` [band]

    Default: *-1*

:guilabel:`Red Edge 2 band` [band]

    Default: *-1*

:guilabel:`Red Edge 3 band` [band]

    Default: *-1*

:guilabel:`Red Edge 4 band` [band]

    Default: *-1*

:guilabel:`NIR band` [band]

    Default: *-1*

:guilabel:`SWIR 1 band` [band]

    Default: *-1*

:guilabel:`SWIR 2 band` [band]

    Default: *-1*

:guilabel:`Thermal 1 band` [band]

    Default: *-1*

:guilabel:`Thermal 2 band` [band]

    Default: *-1*

:guilabel:`Canopy background adjustment` [number]

    Default: *1.0*

:guilabel:`Gain factor` [number]

    Default: *2.5*

:guilabel:`Coefficient 1 for the aerosol resistance term` [number]

    Default: *6.0*

:guilabel:`Coefficient 2 for the aerosol resistance term` [number]

    Default: *7.5*

:guilabel:`Exponent used for OCVI` [number]

    Default: *1.16*

:guilabel:`Exponent used for GDVI` [number]

    Default: *2.0*

:guilabel:`Weighting coefficient used for WDRVI` [number]

    Default: *0.1*

:guilabel:`Weighting coefficient used for ARVI` [number]

    Default: *1.0*

:guilabel:`Soil line slope` [number]

    Default: *1.0*

:guilabel:`Soil line intercept` [number]

    Default: *0.0*

**Outputs**

:guilabel:`Output VRT layer` [rasterDestination]
    VRT file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:CreateSpectralIndices``::

    ----------------
    Arguments
    ----------------

    raster: Raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    indices: Indices
        Default value:    NDVI
        Argument type:    string
        Acceptable values:
            - String value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    scale: Scale factor (optional)
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    formulars: Formulars (optional)
        Argument type:    file
        Acceptable values:
            - Path to a file
    A: Aerosols band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    B: Blue band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    G: Green band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    R: Red band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    RE1: Red Edge 1 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    RE2: Red Edge 2 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    RE3: Red Edge 3 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    RE4: Red Edge 4 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    N: NIR band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    S1: SWIR 1 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    S2: SWIR 2 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    T1: Thermal 1 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    T2: Thermal 2 band (optional)
        Default value:    -1
        Argument type:    band
        Acceptable values:
            - Integer value representing an existing raster band number
    L: Canopy background adjustment (optional)
        Default value:    1
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    g: Gain factor (optional)
        Default value:    2.5
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    C1: Coefficient 1 for the aerosol resistance term (optional)
        Default value:    6
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    C2: Coefficient 2 for the aerosol resistance term (optional)
        Default value:    7.5
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    cexp: Exponent used for OCVI (optional)
        Default value:    1.16
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    nexp: Exponent used for GDVI (optional)
        Default value:    2
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    alpha: Weighting coefficient used for WDRVI (optional)
        Default value:    0.1
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    gamma: Weighting coefficient used for ARVI (optional)
        Default value:    1
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    sla: Soil line slope (optional)
        Default value:    1
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    slb: Soil line intercept (optional)
        Default value:    0
        Argument type:    number
        Acceptable values:
            - A numeric value
            - field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
            - expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputVrt: Output VRT layer
        Argument type:    rasterDestination
        Acceptable values:
            - Path for new raster layer

    ----------------
    Outputs
    ----------------

    outputVrt: <outputRaster>
        Output VRT layer

..
  ## AUTOGENERATED COMMAND USAGE END

