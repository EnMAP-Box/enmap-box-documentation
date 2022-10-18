.. include:: /icon_links.rst

.. _eo4q:

Earth Observation for QGIS (EO4Q)
*********************************

Earth Observation for QGIS (EO4Q) is a collection of EnMAP-Box tools and applications designed to integrate well in both,
EnMAP-Box and QGIS environments.
In both environments, EO4Q applications can be started from the :guilabel:`Earth Observation for QGIS (EO4Q) Toolbar`:

    .. figure:: ./img/EO4QToolbar.png
            :align: center


GEE Time Series Explorer
========================

todo: integrate docs from https://geetimeseriesexplorer.readthedocs.io

Location Browser
================

The :guilabel:`Location Browser` panel allows to
a) navigate to a map location directly, or to
b) send a request to the Nominatim geocoding service.

Usage
    1. Start the tool from the :guilabel:`View > Panels > Location Browser` menu or from the
       :guilabel:`Earth Observation for QGIS (EO4Q) Toolbar`.

    2. Go to locations directly by entering the coordinates in one of the following formats:

        - 53.07478793449, 13.895089018465338  *# longitude, latitude in decimal format*

        - 53°04'29.2"N, 13°53'42.3"E  *# longitude, latitude in GPS format*

        - 13.895089018465338, 53.07478793449, [EPSG:4326]  *# east, north, epsgID*

    3. Send a request to the Nominatim geocoding service and explore the results.

GUI
    .. figure:: ./img/LocationBrowser.png
        :align: center

    |

    .. figure:: ./img/LocationBrowser_2.png
        :align: center

Live demonstration
    ..  youtube:: 2mgx4_pIHqg
        :width: 100%
        :privacy_mode:

Profile Analytics
=================

The :guilabel:`Profile Analytics` panel allows to visualize various types of spectral, temporal and spatial profiles.
Additionally, profile data can be analysed by user-defined function (e.g. fit the data using a regressor).
The ufunc has access to the plot widget and can draw additional plot items.

Live demonstration
    ..  youtube:: 5Un7lxw-PN8
        :width: 100%
        :privacy_mode:

Raster Band Stacking
====================

The :guilabel:`Raster Band Stacking` panel allows to stack bands into a new VRT :term:`raster layer`.
Raster bands can be selected inside the panel or added via drag&drop in various ways.

Usage
    1. Start the tool from the :guilabel:`View > Panels > Raster Band Stacking` menu or from the
       :guilabel:`Earth Observation for QGIS (EO4Q) Toolbar`.

    2. Add raster sources and select bands:

       - add a new raster source via the "+" button

       - select raster(s)  inside the :guilabel:`Data Sources` panel and drag&drop the selection into the table

       - select band(s) inside the :guilabel:`Data Sources` panel and drag&drop the selection into the table

       - select raster layer(s) inside the :guilabel:`Data Views` panel and drag&drop the selection into the table

       - select raster files inside the file explorer (e.g. Windows Explorer) and drag&drop the selection into the table

    3. Prepare the final band stack inside the table by:

       - changing individual band selections

       - removing rows

       - moving rows up and down

    4. Choose an output filename and create the band stack.
       By default, the output pixel grid (i.e. extent, resolution, crs) is derived automatically (i.e. *gdal.BuildVrt* defaults).
       To use a custom pixel grid, switch to the :guilabel:`Raster` option and select a raster.

GUI
    .. figure:: ./img/RasterBandStacking.png
        :align: center

Live demonstration
    ..  youtube:: KGKVvBwz2S0
        :width: 100%
        :privacy_mode:
