
.. _features:

========
Features
========

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

    .. tab:: Raster Rendering

        *Explore your raster data interactively*

        The EnMAP-Box provides new raster renderers that enhance the visualization of imaging spectroscopy data
        and other raster outputs, e.g.:


        .. list-table::
            :header-rows: 1

            *   - Renderer
                - Example

            *   - **Bivariate Color Renderer**

                  Visualize two bands using a 2d color ramp.
                - .. image:: /usr_section/usr_manual/img/BivariateColorRasterRenderer.png

            *   - **Class-fraction or probability rendering**

                  Visualizes multiple class factions/probabilities at the same time using the original class colors.
                - .. image:: /usr_section/usr_manual/img//ClassFractionRenderer.png

            *   - **HSV color rendering**

                  Visualizes 3 bands using the HSV (Hue, Saturation, Value/Black) color model
                - .. image:: /usr_section/usr_manual/img/HSVColorRasterRenderer.png


            *   - **CMYK Color Raster Renderer**

                  Visualizes 4 bands using the CMYK (Cyan, Magenta, Yellow, and Key/Black) color model
                - .. image:: /usr_section/usr_manual/img/CMYKColorRasterRenderer.png

            *   - **Decorelation Stretch Renderer**

                  Removing the high correlation between 3 band for a more colorful color composite image.
                - .. image:: /usr_section/usr_manual/img/DecorrelationStretchRenderer.png


Spectral Libraries
==================

*Your measurements, your data.*

The EnMAP box offers a wide range of options for creating spectral libraries and to describe and visualize their spectral profiles.

* Read spectral profiles measured with
  `ASD <https://www.malvernpanalytical.com/en/products/product-range/asd-range/fieldspec-range>`_,
  `SVC <https://spectravista.com/>`_ (\*.sig) or
  `Spectral Evolution <https://spectralevolution.com/remote-sensing-spectroradiometers/>`_ (\*.sed)
  field spectrometers
* Create profiles from raster images, e.g. for given vector locations (point or polygons)
* Save spectral profiles in vector datasets and show their coordinates, e.g. using
  GeoPackage, GeoJSON or DBMS like PostgreSQL or HANA DB
* Keep profiles together that belong together, e.g. reference and target radiances and reflectance derived from
* Annotate your profiles as needed, e.g. using text (String, Varchar), numeric (int, float) or binary (BLOB) datatypes
* Query your profiles using powerful SQL expressions
* Plot profiles from different instruments simultaneously against wavelength units, e.g. nanometers, micrometers

.. figure:: /usr_section/application_tutorials/spectral_library/img/add_profiles.gif

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
        - Danner et al. 2021, "Efficient RTM-based training of machine learning regression algorithms to quantify biophysical & biochemical traits of agricultural crops",
          ISPRS J Photogramm Remote Sens, 09242716, 173 (2021), pp. 278-296, doi: https://doi.org/10.1016/j.isprsjprs.2021.01.017

    *   - Interactive Visualization of Vegetation Reflectance Models (IVVRM)
        - vegetation, data visualization
        - Danner et al. 2018, "Developing a sandbox environment for prosail, suitable for education and research"
          IEEE international geoscience and remote sensing symposium (2018), pp. 783-786,
          doi: https://doi.org/10.1109/IGARSS.2018.8519378

    *   - Interactive Red-Edge Inflection Point (iREIP)
        - vegetation
        - Hank et al. 2021, "Introducing the potential of the EnMAP-box for agricultural applications using desis and prisma data",
          IEEE international geoscience and remote sensing symposium (2021), pp. 467-470,
          doi: https://doi.org/10.1109/IGARSS47720.2021.9554729

    *   - Vegetation Index Toolbox and Spectral Index Creator
        - spectral indices
        - Hank et al. 2021, "Introducing the potential of the EnMAP-box for agricultural applications using desis and prisma data",
          IEEE international geoscience and remote sensing symposium (2021), pp. 467-470,
          doi: https://doi.org/10.1109/IGARSS47720.2021.9554729

    *   - EnMAP Soil Mapper (EnSoMap)
        - soil
        - Mielke et al. 2018, “Engeomap and Ensomap: Software Interfaces for Mineral and Soil Mapping under Development
          in the Frame of the Enmap Mission,” in IGARSS 2018 - 2018 IEEE International Geoscience and Remote Sensing Symposium,
          IEEE, Jul. 2018, pp. 8369–8372.
          doi: https://doi.org/10.1109/igarss.2018.8517902

    *   - EnMAP Geological Mapper (EnGeoMap)
        - geology
        - Mielke et al. 2018, “Engeomap and Ensomap: Software Interfaces for Mineral and Soil Mapping under Development
          in the Frame of the Enmap Mission,” in IGARSS 2018 - 2018 IEEE International Geoscience and Remote Sensing Symposium,
          IEEE, Jul. 2018, pp. 8369–8372.
          doi: https://doi.org/10.1109/igarss.2018.8517902

    *   - EO Time Series Viewer
        - timeseries
        - Jakimow et al. 2020, "Visualizing and labeling dense multi-sensor earth observation time series: The EO time series viewer",
          Environ Model Softw, 13648152, 125 (2020),
          doi: https://doi.org/10.1016/j.envsoft.2020.104631

    *   - GEE Time Series Explorer
        - timeseries
        - Rufin Pet al. 2021, "GEE Timeseries Explorer for QGIS – Instant Access to Petabytes of Earth Observaton Data."
          Int Arch Photogramm Remote Sens Spatial Inf Sci, 2194-9034, XLVI-4/W2-2021 (2021), pp. 155-158,
          doi: https://doi.org/10.5194/isprs-archives-XLVI-4-W2-2021-155-2021

    *   - Scatter Plots
        - data visualization
        -

    *   - OLCI Neural Network Swarm (ONNS)
        - water
        - Ocean color analysis

          Hieronymi et al. 2017, "The OLCI neural network swarm (ONNS): A bio-geo-optical algorithm for open ocean and coastal waters"
          Front Mar Sci, 2296-7745, 4 (2017), p. 140,
          doi: https://doi.org/10.3389/fmars.2017.00140

    *   - OC-PFT
        - water
        - Retrieval of Phytoplankton Functional Types (PFTs) from satellite or in situ chlorophyll-a (Chl-a) measurements.

          Alvarado et al. 2022, "Retrievals of the main phytoplankton groups at Lake Constance using OLCI, DESIS, and evaluated with fieldobservations".
          12th EARSeL workshop. 2022.

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

