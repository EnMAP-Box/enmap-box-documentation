
..
  ## AUTOGENERATED TITLE START

.. _alg-enmapbox-SpectralResamplingToWavelength:

***********************************
Spectral resampling (to wavelength)
***********************************

..
  ## AUTOGENERATED TITLE END

..
  ## AUTOGENERATED DESCRIPTION START

Spectrally resample a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ by applying linear interpolation or nearest neighbour selection at given `wavelengths <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_.
See `Linear Interpolation Wikipedia Article <https://en.wikipedia.org/wiki/Linear_interpolation>`_ for more details.

..
  ## AUTOGENERATED DESCRIPTION END

Usage:

1. Start the algorithm from the Processing Toolbox panel.

2. Select a raster layer to process and a file containing wavelength data, then click :guilabel:`run`.

    .. figure:: ../../processing_algorithms/spectral_resampling/img/to_wavelenthonly.png
       :align: center

..
  ## AUTOGENERATED PARAMETERS START

**Parameters**

:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.

:guilabel:`File with wavelength` [file]
    A file with `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_ information defining the destination sensor. Possible inputs are i\) raster files, ii\) ENVI Spectral Library files, iii\) ENVI Header files, and iv\) CSV `table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ files with `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ column.

:guilabel:`Resample algorithm` [enum]
    Spectral resample algorithm.
    Default: *1*

**Outputs**

:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

..
  ## AUTOGENERATED PARAMETERS END

..
  ## AUTOGENERATED COMMAND USAGE START

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToWavelength``::

    ----------------
    Arguments
    ----------------

    raster: Spectral raster layer
        Argument type:    raster
        Acceptable values:
            - Path to a raster layer
    wavelengthFile: File with wavelength
        Argument type:    file
        Acceptable values:
            - Path to a file
    resampleAlg: Resample algorithm (optional)
        Default value:    1
        Argument type:    enum
        Available values:
            - 0: Nearest neighbour
            - 1: Linear
        Acceptable values:
            - Number of selected option, e.g. '1'
            - Comma separated list of options, e.g. '1,3'
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

