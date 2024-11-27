
.. _features:

============
Key Features
============

Visualization
=============

.. tabs::

    .. tab:: Maps

        *Like QGIS, just more maps*

        * visualize raster and vector data *interactively* and in *multiple maps*, e.g. to compare different
          band combinations or satellite observations.
        * each map has it's individual and fully customizable layer-tree
        * free arrangement of maps, e.g. side-by-side, horizontally, vertically or in nested-layouts
        * maps can be linked spatially, e.g. to always have the same map scale, show the same map-center, or both
        * raster layers can be linked spectrally to always show band combinations with similar wavelengths

    .. tab:: Spectral Dimension

        *Think in wavelengths, not band numbers*

        * fast-selection of raster bands and band combination based on wavelength regions
        * fast-selection of RGB rendering presets based on well-known wavelength combinations,
          e.g. True Color, NIR-SWIR-Red, ...
        * link raster visualization spectrally to  always show similar wavelength combinations,
          no-matter how many bands your raster sources have

    .. tab:: Data Rendering

        *Explore your raster data interactively*

        New raster renderers enhance the visualization of imaging spectroscopy data and outputs
        of state-of-the art approaches, e.g.:

        * Bivariate Color rendering
        * Class-fraction or probability renderering
        * CMYK and HSV color rendering
        * Decorelation Stretch Renderer
        * Multisource Multiband color rendering


Spectral Libraries
==================

*Your measurements, your data*

The EnMAP-Box makes it possible to build and visualize spectral libraries in QGIS.

* Read spectral profiles measured with ASD, SVC (*.sig) or Spectral Evolution (*.sed) field spectrometers
* Create profiles from raster images, e.g. for given vector locations (point or polygons)
* Save spectral profiles in vector datasets and show their coordinates, e.g. using
  GeoPackage, GeoJSON or DBMS like PostgreSQL or HANA DB
* Keep profiles together that belong together, e.g. reference and target radiances and reflectance derived from
* Annotate your profiles as needed, e.g. using text (String, Varchar), numeric (int, float) or binary (BLOB) datatypes
* Query your profiles using powerful SQL expressions
* Plot profiles from different instruments simultaneously against wavelength units, e.g. nanometers, micrometers


Algorithms
==========

The EnMAP-Box adds more that 190 :ref:`processing algorithms <Processing Algorithms>` to the QGIS Processing Framework.
Start them from the QGIS/EnMAP-Box GUI, in python or the command line, and
connect them with algorithms from other plugins in the QGIS Model Builder.

.. tabs::

    .. tab:: GUI

        .. image:: /img/fit_classification.png

    .. tab:: Python

        .. code-block:: python

            <show python example>


    .. tab:: CLI

        Windows (OSGeo4W shell)

        .. code-block:: batch

            qgis_process run enmapbox:PredictClassificationLayer ^
                  --raster="%data_dir%\enmap_potsdam.tif" ^
                  --classifier="%output_dir%\rfc_fit.pkl" ^
                  --matchByName=1 ^
                  --outputClassification="%output_dir%\classification.tif"

        Linux (bash shell)

        .. code-block:: bash

            qgis_process run enmapbox:PredictClassificationLayer \
                  --raster="$data_dir/enmap_potsdam.tif" \
                  --classifier="$output_dir/rfc_fit.pkl" \
                  --matchByName=1 \
                  --outputClassification="$output_dir/classification.tif"


    .. tab:: Model Builder

        .. image:: /img/graphical_model_classification.png

Applications
============

Various applications enhance the EnMAP-Box to make it ready
for different thematic uses, e.g.:

.. list-table::

    *   - Application
        - What is does
        - Reference

    *   - `EnMAP Preprocessing Tools (EnPT) <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/>`_
        - pre-processing pipeline for EnMAP data
        -

    *   - Regression-based unmixing
        -
        - Okujeni et al. 2017. Ensemble Learning From Synthetically Mixed Training
          Data for Quantifying Urban Land Cover With Support Vector Regression.
          https://doi.org/10.1109/jstars.2016.2634859
    *   - tbc.
        -
        -

