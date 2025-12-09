
.. _speclib:

Spectral Libraries
##################

Spectral Libraries are collections of (i) spectral profiles and (ii) attributes to describe these profiles.

The EnMAP-Box stores spectral profile in vector layers, i.e. a single spectral profile is one of many other attributes
related to a vector feature. Compared with *"traditional"* spectral library formats, this offers a couple of advantages:

* Spectral profiles can easily linked with spatial coordinates or more general, geometries (points, lines, polygons)

* QGIS functionality can be used to ensure data integrity of profile attribute values by design. This reduces the risk of
  incorrect or inconsistent information.
  For example, QGIS can ensures that values of a categorical attribute "material_type" need to be taken from a
  list of defined material names.

* User can store spectral profiles in a wide range of data backends, ranging from local file types like
  `GeoJSON <https://geojson.org/>`_ or `GeoPackage <https://www.geopackage.org/>`_ to remote server hosted databases like `PostgreSQL. <https://www.postgresql.org/>`_

.. figure:: img/speclib_overview.png
    :width: 60%


Spectral Profile
----------------

A single spectral profile consists of a minimum information required to draw a profile.
For that we use a dictionary, that contains a list `y` with profile values:

.. code-block:: json

    {
        "y": [0.1011, 0.1018, ... , 0.1080]
    }

Optionally, we can specify the position of the spectral values (`y`) along the x-axis, axis units (`yUnit`, 'xUnit'), and a
list of bad band multipliers (`bbl`):

.. code-block:: json

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


Any other information to describe the spectral profile (`y`) should be stored on other layer fields, as
QGIS already provided adequate support for them. The observation time, for example,
could be stored in a text field with activate Date/Time widget, and filepaths in a field with attachments widget.

Attribute Table
---------------

The QGIS attribute can be switched into the editor view mode.


Spectral Library Viewer
-----------------------

The Spectral Library viewer combines a QGIS attribute table with a plot view that vizualizes the spectral profiles of
the loaded vector layer. The plot view offers various way to customize the profile display.



Spectral Library API
--------------------

