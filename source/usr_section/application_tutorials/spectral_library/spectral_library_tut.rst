

Spectral Libraries: An Introduction
###################################

**Authors:** Klara Busse & Benjamin Jakimow

**Publication date:** 19/04/2024

This tutorial give an introduction into the use of spectral libraries in the EnMAP-Box.
It is designed for EnMAP-Box 3.14 or higher. Minor changes may be present in subsequent versions, such as modified menu labels or added parameter options.

Getting Started
***************

Start the EnMAP-Box
====================

* Launch QGIS and click the |enmapbox| icon in the toolbar to open the EnMAP-Box. The EnMAP-Box GUI comprises a **Menu** and a **Toolbar**, panels for **Data Sources** and **Data Views**, and the **QGIS Processing Toolbox**, which includes the **EnMAP-Box Processing Algorithms**.

    .. figure:: img/01_enmapbox_surface.png

        The EnMAP-Box main GUI.


Load the Example Data
=====================

For this introduction the Example Data of the EnMAP-Box will be used.

* To load the Example Data, click on **Project** in the menu, then **Add Example Data**.
* If you never worked with the Example Data before, a window will appear and you have
  to download the data.
* After clicking **yes** the example data will be saved into the plugin installation folder.

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

The spectral response functions are stored in as GeoJSON file ``enmap_potsdam_srf.geojson``.
You may inspect it with a standard text editor.

Basic Visualization Steps
=========================

* The spectral library viewer should look like this:

    .. figure:: img/04_spec_lib_window_explained.png

        Overview Spectral Library Viewer.

* Most function in **toolbar** you already know from the normal `QGIS attribute table <https://docs.qgis.org/3.34/en/docs/user_manual/working_with_vector/attribute_table.html#introducing-the-attribute-table-interface>`_.
  The Spectral Library viewer just adds extra tools to create, edit and export profiles.
* The **spectral profiles window** shows the spectral profiles of the features, in our case points with attributes,
  that are collected in the spectral library.
* There is a button to show or hide the properties of the spectral profile window.
* The **attribute table** shows the none-spatial information for each feature in a row.

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
* You can delete selected profiles |mActionDeleteSelected| (please don't do now)
  and save or reject your changes |mActionSaveAllEdits| before turning off the editing
  mode |mActionToggleEditing| afterwards.



Working with Spectral Libraries
*******************************

Profiles with Coordinates
=========================

Let's open a spectral library that provides coordinates for each spectral profile:

* Open a new map view with the **enmap_potsdam** image.
* Download and extract the :download:`speclib_potsdam.zip <speclib_potsdam.zip>`.
  The zip file contains the :file:`speclib_potsdam.gpkg` with the data and a :file:`speclib_potsdam.qml` style file
  that tells QGIS and the EnMAP-Box how to visualize it.
* Drag and drop the ``speclib_potsdam.gpkg`` to the EnMAP-Box Data Source Panel.
* Use the context menu **Open Spectral Library Viewer** to visualize the spectral profiles.
* Use the **Map View** context menu to add the speclib_potsdam vector layer

    .. figure:: img/load_speclib_potsdam_with_map.gif

      Opening the speclib_potsdam.gpkg library in a Spectral Library View and a Map View.



Collect profiles from images
============================

In this introduction we like to collect additional profiles for the following classes:

  * Concrete
  * Cropland
  * Vegetation
  * Water

* Add the ``areal_potsdam`` DOP image to the Map View. It gives us a better understanding
  which classes are covered by a single EnMAP pixel
* Search for areas with that kind of surface coverage.
* Next, click on |select_location| then on |profile|. When you click on a point in the image,
  a spectral profile will be shown on top of the other profiles in the Spectral Library View.
  Simultaneously the **Spectral Profile Source Panel** opens on the right.
* By default, profiles are collected from the top-most raster layer.
  The **Spectral Profile Source Panel** allows to change this and control how profiles are collected.
  It will be explained in more detail below.

* In order to collect profiles from the EnMAP image only, select :file:`enmap_potsdam` as profile source .

    .. figure:: img/spec_prof_to_enmap.gif

       Collecting spectral profiles from an EnMAP image.

* Profiles will now be collected from the EnMAP image and the aerial image
  will make the classification easier.

* To see the EnMAP pixel size underneath, open the Map View context menu, then click on **Crosshair**, **Pixel Grid** and select :file:`enmap_potsdam`.

    .. figure:: img/crosshair.gif

         Showing underneath pixel borders.

* So far, collected profiles are stored temporarily only. We can call them *profile candidates*. By clicking on |plus_green_icon| you can add them to the spectral library.

* With |profile_add_auto| the new spectral profiles candidates are added automatically.

    .. figure:: img/add_profiles_automatically.gif

        Automatic profile collection.

* You may also use

    * CTRL + S to save profiles
    * CTRL + <arrow key> to navigate by 1 EnMAP Pixel
    * <arrow key> to pan the map extent

* For a clearer organization you can add columns |mActionNewAttribute| to add information.
  Insert a column name and select a type (e.g. integer or string).

    .. figure:: img/add_profiles.gif

        Collecting and describing spectral profiles from image data.


Spectral Profile Source Panel
=============================
* The **Spectral Profile Source** panel allows you to (i) specify how spectral profiles are collected from the raster data, (ii) how these profiles can be described in other attribute fields, and how temporary profiles will be displayed.
* If you select |select_location| and |profile| without having a Spectral Library View opened, the **Spectral Profiles Source** panel will open one automatically when you click on a pixel in the map for the first time.
* To open the **Spectral Profiles Source** panel manually, click on **View** in the menu, select **Panels**, and then choose **Spectral Profiles Source**.

    .. figure:: img/spec_profiles_source_panel.png

        The Spectral Profile Source panel (right) specifies how profiles are collected, described
        and displayed when overlaid in a linked Spectral Library View.

* To add a new relation that describes raster image sources and spectral library vector fields, click on |plus_green_icon|.

First, let's focus on the definition of how spectral profiles are collected:

    .. image:: img/spec_prof_pan_prof.gif

* **Profiles** specifies how the profiles are stored in the Profiles field in the spectral library attribute table.
* You can specify the raster source from which the profile is sampled. Choose :file:`enmap_potsdam`.

    .. image:: img/spec_prof_pan_col.gif

* **Style** lets you specify how the sampled profiles are displayed when overlaid in the Spectral Library view.

    .. image:: img/spec_prof_pan_sampling.gif

* **Sampling** can be used to define how the profiles are sampled around the mouse coordinate.

* **Scaling** allows to account for scaling differences between the profile source and profiles in your spectral library.

Now let's look at how other attributes, e.g. integer, float or text values, can be created.
We like to generate a profile name automatically.

* Ensure that the *notes* row is checked.
* Double Click to edit, or open the **Expression Builder** with ε
* With the **Expression Builder** you can create expressions that dynamically generate attributes.
* Write ``'' + format('Px %1,%2', @px_x, @px_y)`` to generate a string that includes the pixel position, as in ``Px 23, 24``.

    .. image:: img/Expression_Builder.png


Changing Profile Styles
=======================

The *profile visualization settings* allow you to change profile color, line- and symbole styles.

* by default, *profiles in the spectral library* use the ``@symbol_color`` that is used in the map visualization.
* In that case you can use the layer legend to show or hide groups of profiles. Changing the layer rendering in the map will change the profile colors too.
* You can define your own colors and even use the expression builder to generate colors based profile attributes
* *temporarily profile candidates* use the style that is defined in the *Spectra Profile Source Panel*.

  .. figure:: img/profile_vis_speclib_legend.gif

    Profile visualization

* Go to the **Layer Properties** of your spectral library in the **Data Views** panel. With **Symbology** you can set the colors.

    .. figure:: img/colors_symbology.gif

        The vector layer symbology panel defines the feature symbols...

* Choose **Categorized**, for **Value**, select the column according to which the classes are to be differentiated. Click **Classify**.
* You can change the colors by double-clicking on the color you want to change.
* Click **OK**. Now your spectra have different colors and your graph is more clear.

    .. figure:: img/graph_col.png

        ... whose colors can be used as profile color.

* Click the "+" button to create a new profile visualization.
  This way you can differentiate profiles by other means than the vector layer map symbology.
* Create a group for *vegetation* that uses the filter expression `"name" = 'vegetation'`. Double click on entries in the *Value* column to edit the visualization name or define filter expressions.
* Create a group for *Other* profiles with filter expression `"name" != 'vegetation'`
* Style both groups differently, e.g. by showing none-vegetation in dotted lines

    .. figure:: img/profile_vis_groups.png

        Using multiple visualization groups allows for fine-tuned profiles styles


Save or reject modifications
****************************

QGIS uses a transaction model to save changes. Modification are saved in an edit-buffer.
To save changes permanently to the data source requires to:

a) click the *save edits* button |mActionSaveEdits|, or

b) disable the edit mode |mActionToggleEditing|. If changes are available, this opens the *Stop Editing* dialog

    .. image:: img/stop_editing_dialog.png

    * Press *Yes* to save your edits, or
    * Press *No* to rollback all modifications.


.. warning::
    Be aware that savings may be made to in-memory data sources. These data sources are lost when closing the EnMAP-Box or QGIS. For example a new (and empty) Spectral Library Viewer |viewlist_spectrumdock| uses an in-memory as data source.

    To save such spectral libraries permanently requires to export them into persistant data formats, like a GeoPackage file (see below *Export Spectral Profiles*)


Import Spectral Profiles
************************

Depending on your file format there are multiple ways to import
spectral profiles from other sources into an existing spectral library.

* Geopackage
* ASD Field Spectrometer
* Raster Layer
* Using the Field Calculator


Geopackage
==========

* Open a new **Spectral Library View**. It uses an empty and in-memory vector layer that
  we can add spectral profiles to.
* Click on |speclib_add| to open the **Import Spectral Profiles** window.

    .. figure:: img/import_a_speclib.gif

        The dialog to import spectral profiles into a spectral library.

* Choose **Geopackage** and set the path to the downloaded ``speclib_potsdam.gpkg`` filename.
* The *Field Value Import* table specifies which attribute we like to import into our speclib.
* Use the *Copy missing source fields* dialog to create a new *notes* field in our in-memory speclib

    .. figure:: img/import_gpkg.png

        Import of profiles from a GeoPackage library.

* Click **OK**


ASD Field Spectrometer
======================

* Open a new **Spectral Library View**.
* Download and extract the :download:`asd_files.zip <asd_files.zip>`
* Click on |speclib_add| to open the **Import Spectral Profiles** window.
* The table allows you to define how attributes from the profile source - the ASD files - will be
  mapped to existing fields in your Spectral Library.
* Use the **Copy missing source fields** dialog to extend you spectral library by additional fields
* Map the ASDs "Spectrum" profile to the "profiles" column.
* Click **OK**
* Select some of the new imported features in the attribute table and zoom to.

    .. figure:: img/import_asd_files.gif

        Importing spectral profiles (White Reference + Target) from an ASD Field Spectrometer into an empty Spectral Library.



Raster Layer
============

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
================

You might already know the QGIS field calculator and have used it to calculate values of vector layer attributes. We can use it to extract or modify spectral profiles as well:

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



Export Spectral Profiles
************************

Spectral profiles can be exported as GeoPackage, GeoJSON or ENVI spectral libraries.

GeoPackage / GeoJSON
====================

* Click on the |speclib_save| symbol. The **Export Spectral Library** window will open.

    .. figure:: img/08_export_speclib_gpkg.png

        Dialog to export spectral profiles into a new GeoPackage file.

* Export the spectral library |speclib_save| as ``*.gpkg`` and choose a file path and layer name.
* Two files are saved: the geopackage file which contains the points and attributes, including the spectral profiles, and an QML file with styling information.

    .. image:: img/exported_gpkg_qml.png

* The new speclib data source is automatically added to the EnMAP-Box data sources and can be opened in QGIS as well

ENVI Spectral Library
=====================

* Now export the spectral library |speclib_save| a *ENVI Spectral Library* ``*.sli``.
  Choose a field from which to export the profiles and a field that contains the profile names.


  .. figure:: img/exported_gpkg_qml.png

    Dialog to export spectral profiles as ENVI Spectral Library.

* The new ENVI Spectral Library (``*.sli``) is accompanied by a ``.csv`` file that lists additional values from, like the point coordinates in WKT notation.

    .. image:: img/exported_envi_files.png

.. note::

    Our spectral library could contain profiles from different sensors in the same field, but
    the ENVI spectral library format does not allow to save profiles with a differing number of bands. In that case the EnMAP-Box will create multiple ``*.sli`` file, one for each set of profiles that are similar in the number of bands and wavelengths.










.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |enmapbox| image:: /img/icons/enmapbox.png
   :width: 28px
.. |mActionDeleteSelected| image:: /img/icons/mActionDeleteSelected.svg
   :width: 28px
.. |mActionDeselectAll| image:: /img/icons/mActionDeselectAll.svg
   :width: 28px
.. |mActionInvertSelection| image:: /img/icons/mActionInvertSelection.svg
   :width: 28px
.. |mActionNewAttribute| image:: /img/icons/mActionNewAttribute.svg
   :width: 28px
.. |mActionSaveAllEdits| image:: /img/icons/mActionSaveAllEdits.svg
   :width: 28px
.. |mActionSaveEdits| image:: /img/icons/mActionSaveEdits.svg
   :width: 28px
.. |mActionSelectAll| image:: /img/icons/mActionSelectAll.svg
   :width: 28px
.. |mActionToggleEditing| image:: /img/icons/mActionToggleEditing.svg
   :width: 28px
.. |mSourceFields| image:: /img/icons/mSourceFields.svg
   :width: 28px
.. |plus_green_icon| image:: /img/icons/plus_green_icon.svg
   :width: 28px
.. |profile| image:: /img/icons/profile.svg
   :width: 28px
.. |profile_add_auto| image:: /img/icons/profile_add_auto.svg
   :width: 28px
.. |select_location| image:: /img/icons/select_location.svg
   :width: 28px
.. |speclib_add| image:: /img/icons/speclib_add.svg
   :width: 28px
.. |speclib_save| image:: /img/icons/speclib_save.svg
   :width: 28px
.. |viewlist_spectrumdock| image:: /img/icons/viewlist_spectrumdock.svg
   :width: 28px
