.. _Spectral resampling (to wavelength):

***********************************
Spectral resampling (to wavelength)
***********************************

Spectrally resample a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ by applying linear interpolation at given `wavelengths <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_.
See `Linear Interpolation Wikipedia Article <https://en.wikipedia.org/wiki/Linear_interpolation>`_ for more details.

.. include:: ../../processing_algorithms_includes/spectral_resampling/spectral_resampling__to_wavelength_.rst


**Parameters**


:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.


:guilabel:`File with wavelength` [file]
    A file with `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_ information defining the destination sensor. Possible inputs are i) raster files, ii) ENVI Spectral Library files, iii) ENVI Header files, and iv) CSV `table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ files with `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ column.

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToWavelength``::

    ----------------
    Arguments
    ----------------
    
    raster: Spectral raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    wavelengthFile: File with wavelength
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputResampledRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputResampledRaster: <outputRaster>
    	Output raster layer
    
    