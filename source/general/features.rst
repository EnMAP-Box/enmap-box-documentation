
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

.. csv-table::
    :header-rows: 1
    :file: enmapboxapplications.csv
