
.. _features:

========
Features
========

GUI Overview
============

The EnMAP-Box offers a graphical user interface (GUI) with which raster, vector and spectral library sources can
be displayed together in different views. Move the mouse over the GUI areas for further information.

.. raw:: html

    <svg
      width="1085"
      height="682"
      viewBox="0 15 385.22895 202.58583"
      style="display: block; margin: auto; font-family: Arial, sans-serif;">

      <style>
        rect {
          fill: transparent;
          stroke: none;
          pointer-events: all;
          transition: stroke 0.3s ease, fill-opacity 0.3s ease;
        }
        rect:hover {
          stroke: red;
          stroke-width: 1;
          fill-opacity: 0.1;
          cursor: pointer;
        }
        text.label {
          font-size: 8px;
          fill: red;
          pointer-events: none;
          opacity: 0;
          transition: opacity 0.3s ease;
          font-weight: normal;
          user-select: none;
        }
        rect.bg {
          fill: beige;
          opacity: 0;
          pointer-events: none;
          transition: opacity 0.3s ease;
          rx: 2;
          ry: 2;
        }
        rect:hover + rect.bg {
          opacity: 1;
        }
        rect:hover + rect.bg + text.label {
          opacity: 1;
        }
      </style>

      <!-- Base image -->
      <image
        href="../_static/img/enmap_gui_base.png"
        x="0" y="0"
        width="385.22895"
        height="202.58583"
        preserveAspectRatio="none" />

      <a href="/usr_section/usr_manual/gui.html#the-gui" target="_self">
        <rect x="0.2717" y="5.977" width="65.747" height="4.8903" />
        <rect class="bg" x="8" y="12" width="45" height="12" />
        <text class="label" x="10" y="20">Menu</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#toolbar" target="_self">
        <rect x="0.5434" y="11.4107" width="236.092" height="9.2372" />
        <rect class="bg" x="95" y="22" width="40" height="12" />
        <text class="label" x="100" y="30">Toolbar</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#gui-panels-data-sources" target="_self">
        <rect x="0.5434" y="21.4629" width="53.521" height="77.1579" />
        <rect class="bg" x="10" y="58" width="75" height="14" />
        <text class="label" x="12" y="70">Data Sources Panel</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#data-views" target="_self">
        <rect x="0.5434" y="99.4359" width="53.25" height="99.1642" />
        <rect class="bg" x="10" y="158" width="68" height="14" />
        <text class="label" x="12" y="170">Data Views Panel</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#map-view" target="_self">
        <rect x="54.0649" y="20.3762" width="265.706" height="89.927" />
        <rect class="bg" x="145" y="58" width="50" height="14" />
        <text class="label" x="147" y="70">Map Viewer</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#spectral-library-view" target="_self">
        <rect x="54.0649" y="109.7598" width="265.977" height="88.8402" />
        <rect class="bg" x="145" y="158" width="90" height="14" />
        <text class="label" x="147" y="170">Spectral Library Viewer</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#processing-toolbox" target="_self">
        <rect x="320.0422" y="20.6479" width="65.204" height="118.454" />
        <rect class="bg" x="255" y="58" width="75" height="14" />
        <text class="label" x="257" y="70">Processing Toolbox</text>
      </a>

      <a href="/usr_section/usr_manual/gui.html#collect-profiles" target="_self">
        <rect x="320.0422" y="139.1015" width="65.747" height="59.4985" />
        <rect class="bg" x="255" y="183" width="90" height="14" />
        <text class="label" x="257" y="190">Spectral Profile Sources</text>
      </a>

    </svg>

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
