.. _Spectral resampling (to wavelength and FWHM):

********************************************
Spectral resampling (to wavelength and FWHM)
********************************************

Spectrally resample a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ by applying `spectral response function <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-response-function>`_ convolution, with spectral response function derived from `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information.

**Parameters**


:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.


:guilabel:`File with wavelength and FWHM` [file]
    A file with `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_ and FWHM information defining the destination sensor. Possible inputs are i) raster files, ii) ENVI Spectral Library files, iii) ENVI Header files, and iv) CSV `table <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-table>`_ files with `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and `fwhm <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-fwhm>`_ columns.

**Outputs**


:guilabel:`Output spectral response function library` [fileDestination]
    GEOJSON file destination.


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToWavelengthAndFwhm``::

    ----------------
    Arguments
    ----------------
    
    raster: Spectral raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    responseFile: File with wavelength and FWHM
    	Argument type:	file
    	Acceptable values:
    		- Path to a file
    outputResponseFunctionLibrary: Output spectral response function library (optional)
    	Argument type:	fileDestination
    	Acceptable values:
    		- Path for new file
    outputResampledRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputResponseFunctionLibrary: <outputFile>
    	Output spectral response function library
    outputResampledRaster: <outputRaster>
    	Output raster layer
    
    