.. _test_dataset:

Example Data
************

.. note::

   For opening the test dataset go to the menubar :menuselection:`Project --> Load Example Data`

   .. image:: /img/gui_loadexampledata.png

   If you try to open the test dataset for the first time, you will be asked to download the data from the repository:

   .. figure:: /img/gui_downloadtestdata.png

   After you downloaded the dataset, you can also use the processing algorithm *Open Test Maps* (in *Auxillary*) to open the dataset.

**EnMAP (30m; 177 bands):**

File name: :file:`enmap_berlin.bsq`

Simulated EnMAP data (based on 3.6m HyMap imagery) acquired in August 2009 over south eastern part of Berlin. It has a spectral resolution of 177 bands and a spatial resolution of 30m.


**HyMap (3.6m; Blue, Green, Red bands)**

File name: :file:`hires_berlin.bsq`

HyMap image acquired in August 2009 over south eastern part of Berlin. This dataset was reduced to 3 bands for true color display. The spatial resolution is 3.6m.


**LandCover Vector Layer (Polygon):**

File name: :file:`landcover_berlin_polygon.gpkg`

Polygon vector geopackage containing land cover information on three classification levels. Derived from very high resolution aerial imagery and cadastral datasets.

 * Level 1 classes: Impervious, Vegetation, Soil, Water
 * Level 2 classes: Impervious, Low Vegetation, Soil, Tree, Water
 * Level 3 classes: Roof, Pavement, Low Vegetation, Soil, Tree, Water

**LandCover Vector Layer (Point):**

File name: :file:`landcover_berlin_point.shp`

Point vector geopackage containing land cover information on two classification levels.

 * Level 1 classes: Impervious, Vegetation, Soil, Water
 * Level 2 classes: Impervious, Low Vegetation, Soil, Tree, Water


**Spectral Library:**

File name: :file:`library_berlin.sli`

Spectral library with 75 spectra (material level, level 2 and level 3 class information)

.. figure:: /img/testdata_speclib.png
   :width: 100%

   library_berlin.sli opened in the EnMAP-Box Spectral Library Window

