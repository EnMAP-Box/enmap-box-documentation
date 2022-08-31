Regression
==========

This section will demonstrate a case of image regression using the :ref:`test dataset <test_dataset>`.
We will regress the sub-pixel fractions of impervious, vegetation, soil and water, derived from a high resolution land cover
polygon vector dataset, against the spectral signature of an EnMAP image. So in this case we are performing a multi target
regression (more than one response variable), but mind that single target regression works in the same way.

#. In a preliminary step we are going to convert the polygon dataset to a fraction raster dataset which fits the resolution of the EnMAP
   raster. This raster will be the regression target, where each band corresponds to the fraction of a landcover class from
   the polygon dataset inside an EnMAP pixel (so percentage of impervious, vegetation, soil and water, respectively).

   In the processing toolbox go to :menuselection:`EnMAP-Box --> Create Raster --> Fraction from Vector`. Enter the
   following settings:

   * :guilabel:`Pixel Grid`: :file:`enmap_berlin.bsq`
   * :guilabel:`Vector`: :file:`landcover_berlin_polygon.shp`
   * :guilabel:`Class id attribute`: ``level_1_id``
   * :guilabel:`Minimal overall coverage`: 0.7
   * :guilabel:`Oversampling factor`: 5
   * :guilabel:`Output Fraction`: Click on :guilabel:`...` and specify an output file path.

   Click :guilabel:`Run`.

   .. figure:: /img/example_regression.png
      :width: 100%

      EnMAP-Box project showing the input EnMAP image and vector dataset (upper map panel) and the respective fraction
      bands for impervious, vegetation and soil (water is not shown here)

#. Now that we have a regression target raster we are going to fit a regression model. In the processing toolbox go
   to :menuselection:`EnMAP-Box --> Regression --> Fit RandomForestRegressor`.

   * Select :file:`enmap_berlin.bsq` as :guilabel:`Raster` and under :guilabel:`Regression` specify the output raster
     from step 1 (the regression target).
   * Leave the rest at default and under :guilabel:`Output Regressor` specify an output file path and click :guilabel:`Run`

#. In the next step we will apply the regression to the image. Go to :menuselection:`EnMAP-Box --> Regression --> Predict Regression`.
   Select :file:`enmap_berlin.bsq` as input :guilabel:`Raster` and under
   :guilabel:`Regressor` click :guilabel:`...` and select the output :file:`.pkl` file from the Fit RandomForestRegressor algorithm.
   Specify an output path (:guilabel:`Output Regression`) and click :guilabel:`Run`.

   .. figure:: /img/example_regression2.png

      EnMAP image in true colors (left) and RGB visualisation of the regression result (right) where red=impervious, green=vegetation,
      blue=soil


