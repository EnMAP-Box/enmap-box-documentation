.. include:: /icon_links.rst

Spectral Libraries: An Introduction
###################################

**Author:** Klara Busse

**Publication date:** 09/04/2024

Getting Started
***************

Requirements
=============
This introduction is designed for EnMAP-Box 3, version 3.13.0 or higher. Minor changes may be present in subsequent versions, such as modified menu labels or added parameter options.


Start the EnMAP-Box
====================

* Launch QGIS and click the |enmapbox| icon in the toolbar to open the EnMAP-Box. The EnMAP-Box GUI comprises a **Menu** and a **Toolbar**, panels for **Data Sources** and **Data Views**, and the **QGIS Processing Toolbox**, which includes the **EnMAP-Box Processing Algorithms**.

    .. figure:: img/01_EnMap-Box_surface.png

        The EnMAP-Box main GUI.


Load the Example Data
=====================

For this introduction the Example Data of the EnMap-Box will be used.

* To load the Example Data, click on **Project** in the menu, then **Add Example Data**.
* If you never worked with the Example Data before, a window will appear and you have to download the test data to your explorer.
* After clicking **yes** the example data will be saved.

    .. figure:: img/02_add_expldt.gif

        Loading the EnMAP-Box example data.

* The example data will appear automatically in a new map window.
* Now, the example data is loaded and you can work with it.
* For clarity, close the map window by clicking on the (x) icon on the blue **Map #1** title bar. The data views panel will be empty afterwards.
* To load an (own) existing file, you can drag and drop the file from your explorer to the **Data Sources** panel.

Load a Spectral Library from the Example Data
=============================================

The EnMAP-Box saves spectral profiles in vector layers. You can use (almost) any vector data source as
backend for a spectral library.

* Open the spectral library  :file:`EnMAP Spectral Response Function (224 Bands)` from the Example Data, using drag and drop:

    .. figure:: img/03_load_spec_lib.gif

        Opening a spectral library with EnMAP spectral response functions.

The EnMAP Spectral Response Function Library is stored as GeoJSON file (``enmap_potsdam_srf.geojson``) that you
can inspect with a standard text editor.

Now let's open a spectral library that includes spatial coordinates for each profile:

* download the :download:`speclib_potsdam.gpkg <speclib_potsdam.zip>`
* Drag and drop the zip file to the EnMAP-Box Data Source Panel.
* Use the context menu **Open Spectral Library Viewer** to open the spectral library.
* Open a map view with the **enmap_potsdam** image and use the map view's context menu
  to add the speclib_potsdam vector layer, that
  is already used by the **Spectral Library Viewer**


    .. figure:: img/load_speclib_potsdam_with_map.gif

      Open the speclib_potsdam.gpkg library in a Spectral Library View and a Map View.


Import Spectral Profiles
========================

Depending on your file format there are multiple ways to import
spectral profiles into an existing spectral library.

The following formats will be explained below:

* Geopackage
* ASD Field Spectrometer
* Raster Layer
* Using the Field Calculator


Geopackage
----------

* Open a new **Spectral Library View**. It uses an empty and in-memory vector layer that
  which we can add spectral profiles to
* To import profiles from a spectral library with the data format **Geopackage**,
  open a spectral library window |speclib|
* Click on |speclib_add| to open the **Import Spectral Profiles** window.

    .. figure:: img/import_a_speclib.gif

        The dialog to import spectral profiles into a spectral library.

* Choose **Geopackage** and select the correct format and the directory.
* To import the columns of your choice, click on |mSourceFields| and select the columns.
* Click **OK**

ASD Field Spectrometer
----------------------

* Download and extract the :download:`asd_files.zip <asd_files.zip>`
* Click on |speclib_add| to open the **Import Spectral Profiles** window.
* The table allows you to define how attributes from the profile source - the ASD files - will be
  mapped to existing fields in your Spectral Library.
* Use the **Copy missing source fields** dialog to extend you spectral library by additional fields
* Map the ASDs "Spectrum" profile our Speclib's "profiles" column.
* Click **OK**

    .. figure:: img/import_asd_files.gif

        Importing spectral profiles (White Reference + Target) from an ASD Field Spectrometer into an empty Spectral Library.


Raster Layer
------------

* To import profiles from a **Raster Layer**, drag and drop your raster file and a vector file
  with locations to extract the raster profiles into a new map window.

* Open **Import Spectral Profiles** window and choose **Raster Layer**
* Select the raster layer from which you like to import profiles
* Select the vector layer that specifies the profile locations
* Specify which other raster and vector attributes will be written to the Spectral Library.
  To import the columns of your choice, click on |mSourceFields| and select the columns.
* To import a **Raster Layer**, drag and drop your raster file into a new map window.
* When you open the **Import Spectral Profiles** window and select **Raster Layer**, the Raster File will automatically appear in the **Options**. If multiple Raster Layers are open, you can choose one.
* To import the columns of your choice, click on |mSourceFields| and select the columns.
* Click **OK**

    .. figure:: img/import_rasterprofiles.gif

        Importing spectral profiles from a raster layer and a vector layer that specifies the profile locations.

Field Calculator
----------------

You probably already know the QGIS field calculator and how you can use it to
calculate vector layer attribute values.

We can use it to modify our spectral profiles as well,
for example to enhance an normal vector layer with a field that stores spectral profiles.

* Open the :file:`enmap_potsdam` raster layer and the :file:`landcover_potsdam_point` layer in a new map window.
* Click on the :file:`landcover_potsdam_point` with the right mouse button and select **Open Spectral Library Viewer**. A new spectral library window opens.
  The points are in the attribute table, but not yet associated with any spectral information.
* Open the Field Calculator and make the following settings to link the points to spectral profiles:
    * Check Create a new field
    * Set an Output field name ``profiles``
    * Output field type: Text(string), with Text length = 0 (unlimited)
    * In the expression field write: ``raster_profile('enmap_potsdam')``
    * Click **OK** to calculate your profiles and make them visible in the attribute table now.
* Click on the :file:`landcover_potsdam_point` with the right mouse button and select **Open Spectral Library Viewer**. A new spectral library window opens. The points are in the attribute table, but not yet associated with any spectral information.

    .. figure:: img/field_calculator.gif

        Any vector layer can be opened in a Spectral Library View and edited with the QGIS Field Calculator.

* To link the points to spectral profiles, follow these steps in the Field Calculator:

..

    * Tick **Create a new field**
    * Set an output field name
    * Output field type: Text(string)
    * In the expression field write the command: raster_profile('enmap_potsdam') to connect the points to the spectral information.
    * Click **OK** and your profiles are visible in the attribute table now.

    .. figure:: img/calculator_settings.png

        EnMAP-Box functions to manage spectral profiles with the QGIS Field Calculator

    .. figure:: img/field_calculator.gif

        Creating spectral profiles using the QGIS Field Calculator.

* To show the spectral profiles, click on **Update Profiles** on the left hand side of the toolbar.


Work with a Spectral Library
****************************
The following shows how to edit and export a spectral library

Instead of the *EnMAP Spectral Response* library from the EnMAP-Box example data you can also download the
:download:`speclib_potsdam.gpkg <speclib_potsdam.zip>` Library.

This zip file contains the :file:`speclib_potsdam.gpkg` and :file:`speclib_potsdam.qml` files, as well as the :file:`speclib_potsdam_style.qml` file that stores the style of the spectral library.

Basic Visualization Steps
===========================

* The spectral library viewer should look like this:

    .. figure:: img/04_spec_lib_window_explained.png

        Overview Spectral Library Viewer.

* There are various functions in the **toolbar** that can be used to create, edit and export a spectral library.
* The **spectral profiles window** shows the spectral profiles of the points, that are collected in the spectral library.
* The **attribute table** shows information for the different profiles.

..
* Let's have a closer look at the toolbar:

    .. image:: img/05_spec_lib_toolbar.png


* While being in the editing mode |mActionToggleEditing|, additional options are unlocked to modify your attribute table:

    .. image:: img/06_spec_lib_toolbar_more_options.png

* These are the tools you already know from the QGIS attribute table (`here is a link to the website  <https://docs.qgis.org/3.34/en/docs/user_manual/working_with_vector/attribute_table.html>`_)
* Some functions of the toolbar are shown below. There are multiple possibilities, to organize and edit the different profiles in the **Attribute Table**:

    .. figure:: img/07_functions_speclib_toolbar.gif

        Selecting spectral profiles from attribute table.

* Select every profile |mActionSelectAll|
* Deselect all profiles |mActionDeselectAll|
* You can highlight multiple profiles at once: Press the shift key and select 2 profiles - all profiles in between will also be selected.
* With |mActionInvertSelection| the opposite profiles can be highlighted.
* Delete selected profiles |mActionDeleteSelected|
* Save your changes |mActionSaveAllEdits| and turn off the toggle editing mode |mActionToggleEditing| afterwards.


Export the Spectral Library
============================
* To apply all changes, save the spectral profiles.
* The spectral profiles can be exported into different data formats (Geopackage, GeoJSON, ENVI spectral library).
* Click on the |speclib_save| symbol. The **Export Spectral Library** window will open.

    .. figure:: img/08_export_speclib.png

        Dialog to export spectral profiles into other formats.

* Choose between Geopackage, GeoJSON or ENVI spectral library.
* Choose a file name and path and click **OK**

Create a Spectral Library
***********************************
This introduction shows you how to create a spectral library by your own.

Load the Data
============================
* Open :file:`aerial_potsdam.tif` and :file:`enmap_potsdam.tif`, by drag and drop. It will automatically be displayed in a new map window.
* Make sure, that the :file:`aerial_potsdam.tif` is over the :file:`enmap_potsdam.tif`.

Add Profiles to a Spectral Library
====================================

* Zoom into the images and make yourself familiar with them.
* In this introduction points for each of the following classes will be collected:

  * Concrete
  * Cropland
  * Vegetation
  * Water

..
* Search for areas with that kind of surface coverage.
* Next, click on |select_location| then on |profile|. When you click on a point in the image, a **spectral library window** will open and show you the spectral profiles of that point. Simultaneously the **Spectral Profile Source Panel** opens on the right.


    .. figure:: img/open_at_spsp.gif

         Start collecting profiles and open Spectral Profile Source Panel.


* Profiles will be collected from the EnMap image. The aerial image will be used to make the classification easier.
* Right click on the images, then click on **Crosshair**, **Pixel Grid** and select :file:`enmap_potsdam`.
* Now you can see the pixel size of the EnMap image underneath.

    .. figure:: img/crosshair.gif

         Set Crosshair.

* In order to collect the pixels from the EnMap image, let's take a quick look at the **Spectral Profile Source Panel**. Additional functions will be explained in the following section "Spectral Profile Source Panel".
* Select :file:`enmap_potsdam` from profiles, to collect the profiles of the EnMap image.

    .. figure:: img/spec_prof_to_enmap.gif

       Select raster layer from which the profiles are collected.


* By clicking on |plus_green_icon| you can save a point with its spectral information into your spectral library.
* For a clearer organization you can add columns |mActionNewAttribute| to add information. Insert a column name and select a type (e.g. integer or string).

    .. figure:: img/add_profiles.gif

        Collecting and describing spectral profiles from image data.


* With |profile_add_auto| the spectral profiles can be collected automatically.

    .. figure:: img/add_profiles_automatically.gif

        Automatic profile collection.



Spectral Profile Source Panel
=============================
* The **Spectral Profile Source** panel allows you to specify how spectral profiles are collected from the raster data and what profile metadata is included in Spectral Libraries.
* It allows you to define the new values for each column of a Spectral Library Vector Layer, that will be added when a new feature is added.
* If you select |select_location| and |profile|, the **Spectral Profiles Source** panel will open automatically when you click on a pixel in the map for the first time.
* To open the **Spectral Profiles Source** panel manually, click on **View** in the menu, select **Panels**, and then choose **Spectral Profiles Source**.

    .. figure:: img/spec_profiles_source_panel.png

        The Spectral Profile Source panel (right) specifies how profiles are collected, described
        and displayed when overlaid in a linked Spectral Library View.

* To add a new relation that describes raster image sources and spectral library vector fields click on |plus_green_icon|.

..

First, let's focus on the definition of how spectral profiles are collected:

    .. image:: img/spec_prof_pan_prof.gif

* **Profiles** specifies how the profiles are stored in the Profiles field in the spectral library attribute table.
* You can specify the raster source from which the profile is sampled. Choose :file:`enmap_potsdam`.

    .. image:: img/spec_prof_pan_col.gif

* **Style** lets you specify how the sampled profiles are displayed when overlaid in the Spectral Library view.

    .. image:: img/spec_prof_pan_sampling.gif

* **Sample** can be used to define how the profiles are sampled around the mouse coordinate.

Now let's have a look at how other vector attributes are created:

* Make sure the first row is checked. Then you can write an expression for one of the columns in your spetral library.

    .. image:: img/oth_vec_attr.png

* Double Click to edit, or open the **Expression Builder** with ε
* With the **Expression Builder** you can design a field expression:

    .. image:: img/Expression_Builder.png



Change the Colours of the Spectra
=================================

* You can organize the points by color, for a better separation.
* Go to the **Layer Properties** of your spectral library in the **Data Views** panel. With **Symbology** you can set the colors.

    .. figure:: img/colors_symbology.gif

        The vector layer symbology panel defines the feature symbols...

* Choose **Categorized**, for **Value**, select the column according to which the classes are to be differentiated. Click **Classify**.
* You can change the colors by double-clicking on the color you want to change.
* Click **OK**. Now your spectra have different colors and your graph is more clear.

    .. figure:: img/graph_col.png

        ... whose colors can be used as profile color.

* It is also possible to change the style of all spectra in the **Spectral Library Window** based on their profile source. This is useful when collecting profiles from different sources and wanting to differentiate them.

    .. figure:: img/color_change_speclib.gif

       Change the style of the spectra based on their profile source.

Export the Spectral Library and its Style
==========================================

* Export the spectral library |speclib_save| as ``*.gpkg`` and choose a file path and name.
* The style can be saved at symbology. Click on **Style**, then on **Save Style**.
  Select the file path and save the style as ``*.qml`` file.

    .. figure:: img/13_save_style.gif

        Saving a layer style into a ``*.qml`` file

* You can import your spectral library by dragging and dropping the file from your data explorer into the **Data Sources** panel.
* To import the style you have to open the spectral library in a **Spectral Library Window** or **Map Canvas** (drag and drop).
  Then go to **Layer Properties**, **Style** and click on **Load Style**. Choose the file directory to your saved style and **Load Style**.

    .. image:: img/14_export_speclib.png

* Two files are saved: the geopackage file contains the points with their spectral information, and the QML file contains all layer information.