
.. _features:

============
Key Features
============

Map Visualization
=================

*Like QGIS, just more maps*

* visualize raster and vector data *interactively* and in *multiple maps*, e.g. to compare different
  band combinations or satellite observations.
* each map has it's individual and fully customizable layer-tree
* free arrangement of maps, e.g. side-by-side, horizontally, vertically or in nested-layouts
* maps can be linked spatially, e.g. to always have the same map scale, show the same map-center, or both
* imager raster layers in maps can be linked spectrally, with on the fly nearest-neighbor resampling of wavelength

*Think in wavelengths, not band numbers*

* fast-selection of raster bands and band combination based on wavelength regions
* fast-selection of RGB rendering presets based on well-known wavelength combinations,
  e.g. True Color, NIR-SWIR-Red, ...
* link raster visualization spectrally to  always show similar wavelength combinations,
  no-matter how many bands your raster sources have

*Explore your raster data interactively*

New raster renderers enhance the visualization of imaging spectroscopy data and outputs
of state-of-the art approaches, e.g.:

* Bivariate Color rendering
* Class-fraction or probability renderering
* CMYK and HSV color rendering
* Decorelation Stretch Renderer
* Multisource Multiband color rendering

Spectral Profiles and Spectral Libraries
========================================

*Your measurements, your data*

* Read spectral profiles measured with ASD, SVC (*.sig) or Spectral Evolution (*.sed) field spectrometers
* Create profiles from raster images, e.g. for given vector locations (point or polygons)
* Save spectral profiles in vector datasets and show their coordinates, e.g. using
  GeoPackage, GeoJSON or DBMS like PostgreSQL or HANA DB
* Keep profiles together that belong together, e.g. reference and target radiances and reflectance derived from
* Annotate your profiles as needed, e.g. using text (String, Varchar), numeric (int, float) or binary (BLOB) datatypes
* Query your profiles using powerful SQL expressions
* Plot profiles from different instruments simultaneously against wavelength units, e.g. nanometers, micrometers

QGIS Processing Algorithms
==========================

* The EnMAP-Box adds more that 190 algorithms to the QGIS Processing Framework.
* it's QGIS, you can call them from the GUI, from python and even the command line interface

EnMAP-Box Applications
======================

Our partners created various applications that enhance the EnMAP-Box for different thematic uses, e.g.:

.. list-table::

    *   - Application
        - What is does
        - Reference

    *   - `EnMAP Preprocessing Tools (EnPT) <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/>`_
        - pre-processing pipeline for EnMAP data
        -
