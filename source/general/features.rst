
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

    .. tab:: Hyperspectral Data

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

        .. list-table::

            *   - Bivariate Color rendering
                - Class-fraction or probability renderering
                - CMYK and HSV color rendering

            *   - Decorelation Stretch Renderer
                - Multisource Multiband color rendering
                -


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
Start them from the QGIS/EnMAP-Box GUI, from python, command line interfaces, or
connect them with algorithms from other plugins in the QGIS Model Builder.

.. tabs::

    .. tab:: GUI

        .. image:: /img/fit_classification.png

    .. tab:: Python

        .. code-block:: python

            <show python example>


    .. tab:: Windows (CLI)

        Open the OSGeo4W or conda shell and call:

        .. code-block:: batch

            qgis_process run enmapbox:PredictClassificationLayer ^
                  --raster="%data_dir%\enmap_potsdam.tif" ^
                  --classifier="%output_dir%\rfc_fit.pkl" ^
                  --matchByName=1 ^
                  --outputClassification="%output_dir%\classification.tif"
    .. tab::
        Linux (bash)

        .. code-block:: bash

            qgis_process run enmapbox:PredictClassificationLayer \
                  --raster="$data_dir/enmap_potsdam.tif" \
                  --classifier="$output_dir/rfc_fit.pkl" \
                  --matchByName=1 \
                  --outputClassification="$output_dir/classification.tif"

    .. tab:: Model Designer

        Using the `QGIS Model Designer <https://docs.qgis.org/3.34/en/docs/user_manual/processing/modeler.html>`_ you
        can connect EnMAP processing algorithms with others and create powerful processing models.

        .. image:: /img/graphical_model_classification.png

Applications
============

Various applications enhance the EnMAP-Box to make it ready
for different thematic uses, e.g.:

.. list-table::
    :header-rows: 1
    :class: sphinx-datatable

    *   - Application
        - Keywords
        - Description

    *   - `EnMAP Preprocessing Tools (EnPT) <https://enmap.git-pages.gfz-potsdam.de/GFZ_Tools_EnMAP_BOX/EnPT/doc/>`_
        - preprocessing
        - Scheffler et al. 2023, EnPT – an Alternative Pre-Processing Chain for Hyperspectral EnMAP Data,
          https://doi.org/10.1109/igarss52108.2023.10281805.

    *   - Regression-based unmixing
        - unmixing
        - Okujeni et al. 2017, Ensemble Learning From Synthetically Mixed Training
          Data for Quantifying Urban Land Cover With Support Vector Regression.
          https://doi.org/10.1109/jstars.2016.2634859

    *   - Plant Water Retrieval
        - vegetation
        - Wocher et al. 2018, Physically-Based Retrieval of Canopy Equivalent Water Thickness Using Hyperspectral Data, Remote Sensing
          https://doi.org/10.3390/rs10121924.

    *   - Analyze Spectral Integral (ASI)
        - vegetation
        - Wocher et al. 2020, RTM-based dynamic absorption integrals for the retrieval of biochemical vegetation traits,
          doi: https://doi.org/10.1016/j.jag.2020.102219.

    *   - Vegetation Processor
        - vegetation
        -

    *   - Interactive Visualization of Vegetation Reflectance Models (IVVRM)
        - vegetation, data visualization
        -

    *   - Interactive Red-Edge Inflection Point (iREIP)
        - vegetation
        -

    *   - Vegetation Index Toolbox and Spectral Index Creator
        - spectral indices
        -

    *   - EnMAP Soil Mapper (EnSoMap)
        - soil
        -

    *   - EnMAP Geological Mapper (EnGeoMap)
        - geology
        -

    *   - EO Time Series Viewer
        - timeseries
        -

    *   - GEE Time Series Explorer
        - timeseries
        -

    *   - Scatter Plots
        - data visualization
        -

    *   - OLCI Neural Network Swarm (ONNS)
        - water
        -

    *   - OC-PFT
        - water
        -

    *   - Image Cube
        - general, data visualization
        -

    *   - Raster Math
        - general
        -

    *   - Classification Workflow
        - general, classification
        -

    *   - Regression Workflow
        - general, regression
        -

