
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-SpectralResamplingToSentinel2AMsi:

****************************************
Spectral resampling (to Sentinel-2A MSI)
****************************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Spectral resampling to the Sentinel-2A MultiSpectral Instrument \(MSI\) \(Sentinel-2A MSI\) sensor.
For more information see the `mission website <https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2>`_.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select a raster layer to process and click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/spectral_resampling/img/sentinel2AMSI.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.

**Outputs**

:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToSentinel2AMsi``::

    ----------------
    Arguments
    ----------------

    raster: Spectral raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    outputResampledRaster: Output raster layer
        Argument type:    rasterDestination
        Acceptable values:
            - Path for new raster layer

    ----------------
    Outputs
    ----------------

    outputResampledRaster: <outputRaster>
        Output raster layer

..
  ## AUTOGENERATED COMMAND USAGE END

