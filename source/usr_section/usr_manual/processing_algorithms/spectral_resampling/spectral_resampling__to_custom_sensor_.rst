.. _Spectral resampling (to custom sensor):

**************************************
Spectral resampling (to custom sensor)
**************************************

Spectrally resample a `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ by applying `spectral response function <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-response-function>`_ convolution.

.. include:: ../../processing_algorithms_includes/spectral_resampling/spectral_resampling__to_custom_sensor_.rst

**Parameters**


:guilabel:`Spectral raster layer` [raster]
    A `spectral raster layer <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-raster-layer>`_ to be resampled.


:guilabel:`Spectral response function` [string]
    Python code specifying the `spectral response function <https://enmap-box.readthedocs.io/en/latest/general/glossary.html#term-spectral-response-function>`_.

    Default::

        from collections import OrderedDict
        
        # Place response function definition here. Should look something like this:
        responses = OrderedDict()
        
        # Option 1: Use band name as dict-key,
        #           together with fully defined list of (<wavelength>, <response>) tuples as dict-value.
        #           Define <response> as values between 0 and 1 for each whole nanometer <wavelength>.
        responses['Blue'] = [(443, 0.001), (444, 0.002), ..., (509, 1.0), ..., (518, 0.002), (519, 0.001)]
        responses['Green'] = [(519, 0.001), (520, 0.002), ..., (550, 1.0), ..., (597, 0.003), (598, 0.001)]
        ...
        # Option 2: Use band center wavelength as dict-key,
        #           together with band full width at half maximum (FWHM) as dict-value.
        #           The response function is modelled as an RBF around the center wavelength with a width of FWHM / 2.355.
        #           See https://en.wikipedia.org/wiki/Full_width_at_half_maximum for details.
        responses[460] = 5.8
        ...
        responses[2409] = 9.1
        
**Outputs**


:guilabel:`Output spectral response function library` [fileDestination]
    GEOJSON file destination.


:guilabel:`Output raster layer` [rasterDestination]
    Raster file destination.

**Command-line usage**

``>qgis_process help enmapbox:SpectralResamplingToCustomSensor``::

    ----------------
    Arguments
    ----------------
    
    raster: Spectral raster layer
    	Argument type:	raster
    	Acceptable values:
    		- Path to a raster layer
    response: Spectral response function
    	Default value:	from collections import OrderedDict
    
    # Place response function definition here. Should look something like this:
    responses = OrderedDict()
    
    # Option 1: Use band name as dict-key,
    #           together with fully defined list of (<wavelength>, <response>) tuples as dict-value.
    #           Define <response> as values between 0 and 1 for each whole nanometer <wavelength>.
    responses['Blue'] = [(443, 0.001), (444, 0.002), ..., (509, 1.0), ..., (518, 0.002), (519, 0.001)]
    responses['Green'] = [(519, 0.001), (520, 0.002), ..., (550, 1.0), ..., (597, 0.003), (598, 0.001)]
    ...
    # Option 2: Use band center wavelength as dict-key,
    #           together with band full width at half maximum (FWHM) as dict-value.
    #           The response function is modelled as an RBF around the center wavelength with a width of FWHM / 2.355.
    #           See https://en.wikipedia.org/wiki/Full_width_at_half_maximum for details.
    responses[460] = 5.8
    ...
    responses[2409] = 9.1
    
    	Argument type:	string
    	Acceptable values:
    		- String value
    		- field:FIELD_NAME to use a data defined value taken from the FIELD_NAME field
    		- expression:SOME EXPRESSION to use a data defined value calculated using a custom QGIS expression
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
    
    