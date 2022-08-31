Create Map Predictions from ARTMO table
=======================================

This recipe demonstrates how look-up tables generated with the `ARTMO toolbox <https://artmotoolbox.com/>`_ can be
used to create spatially explicit maps of the parameters derived in the radiative transfer model.

This will include the following steps:
 * Import the ARTMO look-up table into the EnMAP-Box
 * Spectrally resample the wavelength information to the target sensor/image
 * Fit a Regressor
 * Apply the model to the image

This example uses the ARTMO table provided with the :ref:`EnMAP-Box test dataset <test_dataset>`. You can find the
look-up table and the metadata in the EnMAP-Box plugin folder::

 enmapboxplugin\enmapboxtestdata\artmo

Also open the other datasets from the test data (in the processing toolbox :menuselection:`Auxilliary --> Open Test Maps`).

First, lets have a look at the metadata (:file:`directional_reflectance_meta.txt`)::

 CLASS:  Generic class
 PROJECT:  PROSAIL1000fcover
 COMMENT:
 DATE:  2019-08-05
 SENSOR:  NO SENSOR
 # BANDS:  2101.000000
 # SAMPLES:  1000.000000
 File created for ARTMO. Date: 2019/8/5 Time: 9:12:50
 Line 1, Column 8 ... end: Wavelength
 Column 1: Cab	min: 0.0550	 max: 79.9352	 count: 1000
 Column 2: Cw	min: 0.0020	 max: 0.0500	 count: 1000
 Column 3: Cm	min: 0.0020	 max: 0.0500	 count: 1000
 Column 4: lai	min: 0.0001	 max: 7.9968	 count: 1000
 Column 5: angle	min: 0.0264	 max: 89.9445	 count: 1000
 Column 6: psoil	min: 0.0000	 max: 0.9996	 count: 1000
 Column 7: vCover	min: 0.0001	 max: 0.9995	 count: 1000
 Line 2, Column 8 ... end: Directional_reflectance
 Fixed variables:
 Model: Prospect 4
 N:Leaf Structural Parameter:	1.5000
 Model: 4SAIL
 skyl:Diffuse/Direct light:	10.0000
 hspot:Hot spot:	0.0100
 tts:Solar Zenith Angle [deg]:	30.0000
 tto:View zenith Angle [deg]:	0.0000
 psi:Relative Azimuth Angle [deg]:	0.0000

As we can see, the first line in the :file:`directional_reflectance.txt` file stores the wavelength information (starting at column 8, column 1-7 are set to 0).
Column 1-7 store the values of the different indicators (Cab, Cw, Cm, lai, angle, psoil, vCover) which we are going to use
as response variables. Starting in line 2 and column 8 we have the directional reflectance values.

Importing the ARTMO table
-------------------------

First we have to import the ARTMO table. Go to the Processing toolbox and start the algorithm
:menuselection:`Auxilliary --> Import ARTMO lookup table`. This algorithm will convert the ARTMO table into two (pseudo) images with
the dimensions *n_samples* x 1. This is necessary as the subsequent processing steps are based on the raster format as input.

* In the algorithm dialog under :guilabel:`ARTMO lookup table` navigate to the file :file:`directional_reflectance.txt`
* The :guilabel:`Reflectance scale factor` allows rescaling the reflectance values in the ARTMO table on-the-fly. This
  might be necessary if the values of the target image have a different scaling. Here in the cookbook example this is the case, as the
  reflectance values of the EnMAP test image are scaled between 0-10000, but the ARTMO reflectance is in floating point between 0 and 1.
  Therefore set the value to ``10000``.
* Now you just need to specify the output paths. :guilabel:`Output Raster` stores the directional reflectance values.
  :guilabel:`Regression Output` stores the corresponding indicator values (Cab, Cw, Cm, lai, angle, psoil, vCover),
  where every indicator is stored in a separate band.
* Click :guilabel:`Run` to start the processing.

Spectral Resampling
-------------------

Since the ARTMO data and the EnMAP image have different spectral resolutions we have to align them before we can fit a
machine learning regression. Therefore the higher resolved ARTMO data will be resampled to EnMAP resolution. Open the
processing algorithm :menuselection:`Resampling and Subsetting --> Spectral Resampling`.

* Under :guilabel:`Raster` select the file with the ARTMO reflectance values (:guilabel:`Output Raster` from previous step).
* Under :guilabel:`[Option 1]` choose ``select sensor``
* Under :guilabel:`[Option 2]` select :file:`enmap_berlin.bsq` (i.e., the file with the desired target resolution)
* Leave the :guilabel:`Resampling Algorithm` at ``Linear Interpolation``
* Specify output path under :guilabel:`Output Raster`
* Click :guilabel:`Run`

Fit a regressor
---------------

In this step we will train a regressor where we, based on the ARTMO data, regress the (resampled) spectral reflectances
against the indicators.

* Open the algorithm :menuselection:`Regression --> RandomForestRegressor`

  .. tip:: You can also choose different machine learners here, the following steps will be identical.

* Choose the resampled ARTMO raster as :guilabel:`Raster` (predictors) and the image containing the indicator values as :guilabel:`Regression` (response).
  Leave the :guilabel:`Mask` field empty.
* You can leave the regressor parameters in the :guilabel:`Code` window at default.
* Specify a output path for the :guilabel:`Output Regressor`. This is an intermediate :file:`.pkl` file which will be needed in a subsequent step.
* Click :guilabel:`Run`

Predict Regression
------------------

In this final step we will apply the model we fit in the previous step to the EnMAP image in order to receive a pixel wise
prediction of the ARTMO indicators.

* Open the algorithm :menuselection:`Regression --> Predict Regression`
* Select :file:`enmap_berlin.bsq` as :guilabel:`Raster`
* Under :guilabel:`Regressor` specify the :file:`.pkl` file from the previous step
* Specify an output path (:guilabel:`Output Regression`)
* Click :guilabel:`Run`

The result is a 7 band raster, where each band corresponds to one indicator:

.. image:: /img/artmo_predictions.png




