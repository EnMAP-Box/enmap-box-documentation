
.. _speclib:

Spectral Libraries
##################

Spectral Libraries are collections of spectral profiles and attribute to describe these profiles.
The EnMAP-Box stores spectral profile in vector layers. Compared with *"traditional"*
spectral library formats, this offers several advantages:

* we can link spectral profiles to spatial geometries (points, lines, polygons) and display them in GIS maps

* we can use existing QGIS functionality to ensure data integrity and avoid incorrect or inconsistent attribute values by design.
  For example, QGIS can ensures that values of a categorical attribute "material_type" need to exist in a
  list of predefined material names.

* we can store spectral profiles in a wide range of data backends, ranging from local file types like
  `GeoJSON <https://geojson.org/>`_ or `GeoPackage <https://www.geopackage.org/>`_ to remote server hosted databases like `PostgreSQL. <https://www.postgresql.org/>`_

.. figure:: img/speclib_overview.png
    :width: 60%


Spectral Profile
----------------

A single spectral profile contains the minimum information that is required to draw a profile.
This information is stored in a JSON dictionary that contains at least a list `y` with profile values:

.. code-block:: text

    {
        "y": [0.1011, 0.1018, ... , 0.1080]
    }

Optionally, we can specify the position of the spectral values (`y`) along the x-axis, axis units (`yUnit`, 'xUnit'), and a
list of bad band multipliers (`bbl`):

.. code-block:: text

    {
        "y": [0.1011, 0.1018, ... , 0.1080],
        "x": [418.24, 423.874, ... , 2445.53],
        "xUnit" : "nanometers",
        "yUnit" : "reflectance",
        "bbl" : [1, 0, ... , 1]
    }

The EnMAP-Box reads and writes these dictionaries of spectral profiles
from or to any vector layer that supports on of the following data types:

.. list-table:: Datatypes to store spectral profiles
    :header-rows: 1

    * - Data Type
      - SQL
      - GDAL/OGR
      - Qt/QGIS
      - Notes
    * - Text, Strings
      - TEXT, VARCHAR
      -
      -
      - arbitrary or at least sufficient length
    * - JavaScript Object Notation
      - `JSON, JSONB <https://www.postgresql.org/docs/current/datatype-json.html>`_
      -
      - `QVariantMap <https://qthub.com/static/doc/qt5/qtcore/qmetatype.html#details>`_
      -
    * - [deprectated] Binary Large Objects
      - BLOB
      -
      - `QByteArray <https://qthub.com/static/doc/qt5/qtcore/qmetatype.html#details>`_
      -


Any other metadata to describe spectral profiles should be stored in different fields.
This way we can use standard QGIS/GDAL functions to filter spectral profile based on their attributes.

Import and Export Profiles
--------------------------

Attribute Table
---------------

The QGIS attribute can be switched into the editor view mode.


Spectral Library Viewer
-----------------------

The Spectral Library viewer combines a QGIS attribute table with a plot view that vizualizes the spectral profiles of
the loaded vector layer. The plot view offers various way to customize the profile display.



Spectral Library API
--------------------

