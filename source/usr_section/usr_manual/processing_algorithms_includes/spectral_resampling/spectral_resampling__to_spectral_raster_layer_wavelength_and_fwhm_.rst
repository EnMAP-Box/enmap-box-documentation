.. _Spectral resampling (to spectral raster layer wavelength and FWHM):

******************************************************************
Spectral resampling (to spectral raster layer wavelength and FWHM)
******************************************************************

Spectrally resample a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ by applying `spectral response function <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-response-function>`_ convolution, with spectral response function derived from `wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-wavelength>`_ and FWHM information stored inside a spectral `raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-raster-layer>`_.

**Parameters**


:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.


:guilabel:`Spectral raster layer with wavelength and FWHM` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ with `center wavelength <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-center-wavelength>`_ and FWHM information defining the destination sensor.


:guilabel:`Save spectral response function` [boolean]
    Whether to save the `spectral response function library <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-response-function-library>`_ as *.srf.gpkg* sidecar file.

    Default: *False*

**Outputs**


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToSpectralRasterLayerWavelengthAndFwhm``::

    ----------------
    Arguments
    ----------------
    
    raster: Spectral raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    responseRaster: Spectral raster layer with wavelength and FWHM
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    saveResponseFunction: Save spectral response function (optional)
    	Default value:	false
    	Argument type:	boolean
    	Acceptable values:
    		- 1 for true/yes
    		- 0 for false/no
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
    outputResampledRaster: Output raster layer
    	Argument type:	rasterDestination
    	Acceptable values:
    		- Path for new raster layer
    
    ----------------
    Outputs
    ----------------
    
    outputResampledRaster: <outputRaster>
    	Output raster layer
    
    