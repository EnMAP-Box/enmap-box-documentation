.. _gui:

GUI
###

    .. figure:: /img/manual_gui.png
       :align: center

       Overview of the EnMAP-Box

.. _gui_toolbar:

Toolbar
=======

In the toolbar you can find the most common tasks. See table below for information on different buttons and their functionality.

* It is possible to enable and disable the different tools: Right-click |mouse_rightclick| on the toolbar and check or uncheck the desired
  toolbar.

    .. figure:: /img/toolbarView.png
       :align: center

       Enable and disable different toolbars

.. _gui_datasources:

Data Sources
------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Button
     - Button Name
     - Description
   * - |mActionDataSourceManager|
     - Adds a data source
     - Here you can add data from different sources, e.g. raster and vector

.. _gui_maps_and_views:

Maps and Views
--------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Button
     - Button Name
     - Description
   * - |viewlist_mapdock|
     - Open a map view
     - Opens a new Map View
   * - |viewlist_spectrumdock|
     - Open a Spectral Library View
     - Opens a new Spectral Library View
   * - |viewlist_textview|
     - Open a text window
     - Opens a new text window, you can for example use it to store metadata, take notes etc.


.. _gui_map_tools:

Map Tools
---------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Button
     - Button Name
     - Description
   * - |mActionPan|
     - Pan Map
     - Moves the map. Can also be achieved by holding the mouse wheel |mouse_wheel|
   * - |mActionZoomIn|
     - Zoom In
     - Increases the zoom level. You can also scroll the mouse wheel |mouse_wheel| forward.
   * - |mActionZoomOut|
     - Zoom Out
     - Decreases the zoom level. You can also scroll the mouse wheel |mouse_wheel| backwards.
   * - |mActionZoomActual|
     - Zoom to native resolution
     - Zoom to the native resolution
   * - |mActionZoomFullExtent|
     - Zoom to full extent
     - Changes the zoom level of the map you click to show the full extent of all layers visualized in it
   * - |select_location|
     - Identify
     - Identify locations on the map where you click with the cursor. Use the two options on the right to specify what to identify
   * - |metadata|
     - *option:* Location value
     - Shows pixel values of all layers at the selected position
   * - |profile|
     - *option:* Pixel profile
     - Opens Spectral Library View (if not opened yet) and plots the spectral profile of the selected pixel
   * - |pan_center|
     - *option:* Center map
     - Moves the map center to the selected cursor location
   * - |link_basic|
     - Specify the linking between different maps
     - Opens the Map Linking Dialog
   * - |processingAlgorithm|
     - Toggle processing toolbox visibility
     - Opens the Processing toolbox panel


.. _gui_vector_tools:

Vector Tools
------------


.. list-table::
   :widths: auto
   :header-rows: 1

   * - Button
     - Button Name
     - Description
   * - |mActionSelectRectangle|
     - Select features
     - Click in the image to select different features. Use the dropdown menu to choose what kind of feature to select, e.g., by polygon, freehand or radius.
   * - |mActionDeselectAll|
     - Deselect selected features
     - Click to delete selection.
   * - |mActionToggleEditing|
     - Toggle editing
     - Activate to be able to work with vector data, e.g. to edit or save features
   * - |mActionSaveEdits|
     - Save Edits
     - Hit button to save changes.
   * - |mActionCapturePoint|
     - Draw a new feature (point)
     - Add a point feature to existing data.
   * - |mActionCapturePolygon|
     - Draw a new feature (polygon)
     - Add a polygon feature to existing data.


Earth Observation for QGIS (EO4Q)
---------------------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Button
     - Button Name
     - Description
   * - |GEE|
     - GEE Time Series Explorer
     - Opens the GEE Time Series Explorer in a new view.
   * - |locationbrowser|
     - Location Browser
     - Use point location or geometry formats to navigate to a specific location or send a request to the `Nominatim Geocoding service <https://wiki.openstreetmap.org/wiki/Nominatim>`_ of OpenStreetMap.
   * - |profileanalytics|
     - Profile Analytics
     - Opens the Profile Analytics in a new view.
   * - |rasterbandstacking|
     - Raster Band Stacking
     - Stack different raster bands individually.
   * - |sensorimport|
     - Sensor Product Import
     - Import different sensor products by drag & drop.

Panels
=======

.. _gui_panels_data_sources:

Data Sources
------------

The **Data Sources** panel lists the data in your current project, comparable to the Layers panel in QGIS. The following data types and their
corresponding metadata are available:

* |mIconRasterLayer| Raster Data

  * **File size**: Metadata on resolution and extent of the raster
  * **CRS**: Shows Coordinate Reference System (CRS) information
  * **Bands**: Information on overall number of bands as well as band-wise metadata such as name, class or wavelength (if available)

    .. note::

       Depending on the type, raster layers will be listed with different icons:

       * |mIconRasterImage| for default raster layers (continuous value range)
       * |mIconRasterMask| for mask raster layers
       * |mIconRasterClassification| for classification raster layers



* |mIconLineLayer| Vector Data

  * **File size**: Shows the file size and extent of the vector layer
  * **CRS**: Shows Coordinate Reference System (CRS) information
  * **Features**: Information on number of features and geometry types
  * **Fields**: Attribute information, number of fields as well as field names and corresponding datatype


* |speclib| Spectral Libraries

  * **File size**: Size of the file on hard disk
  * **Profiles**: Shows the number of spectra in the library


* |processingAlgorithm| Models


**Buttons of the Data Sources panel:**

.. csv-table::
   :widths: auto
   :header: "Button", "Description"

   |mActionDataSourceManager|, "This button lets you add data from different sources, e.g. raster and vector. Same function as |add_datasource|."
   |mActionRemove|, "Remove layers from the Data Sources panel. First select one or more and then click the remove button."
   |mActionCollapseTree|, "Collapses the whole menu tree, so that only layer type groups are shown."
   |mActionExpandTree|, "Expands menu tree to show all branches."
   |qgis_icon|, "Synchronizes Data Sources with QGIS."


.. tip::
   * If you want to remove all layers at once, right-click |mouse_rightclick| in the Data Sources panel and and select :guilabel:`Remove all DataSources`
   * The EnMAP-Box also supports Tile-/Web Map Services (e.g. Google Satellite or OpenStreetMap) as a raster layer. Just add them to
     your QGIS project as you normally would, and then click the |qgis_icon| :superscript:`Synchronize Data Sources with QGIS`
     button. Now they should appear in the data source panel and can be added to a Map View.

.. _gui_panels_data_views:


Data Views
----------

The Data Views panel organizes the different windows and their content.
You may change the name of a Window by double-clicking onto the name in the list.

**Buttons of the Data Views panel:**

.. csv-table::
   :header-rows: 1
   :widths: auto
   :delim: ;

   Button; Description
   |symbology|; Open the Raster Layer Styling panel
   |mActionRemove|; Remove layers from the Data Views panel. First select one or more and then click the remove button.
   |mActionCollapseTree|;  Collapses the whole menu tree, so that only layer type groups are shown.
   |mActionExpandTree|; Expands menu tree to show all branches.


**Organization of the Data Views panel:**

    .. figure:: ../../img/example_data_views.png
       :align: center

Example of how different window types and their contents are organized in the Data Views panel. In this case there
are two Map Views and one Spectral Library View in the project.


.. _gui_spectra_profile_source:

Spectral Profile Sources
------------------------

This menu manages the connection between raster sources and spectral library windows.
When collecting profiles, the *Identify* tool |select_location| selects profiles from the top-most raster layer by default. The Profile Source panel allows to change this behaviour
and to control:

* the profile source, i.e., the raster layer to collect profiles from,
* the style how they appear in the profile plot as profile candidate,
* the sampling method, for example to aggregate multiple pixel into a single profile first,
* the scaling of profile value.

    .. figure:: /img/SpectralProfileSources.png
       :align: center
       :width: 800

*Overview of the Spectral Profile Sources Window with two labeled spectra and main functionalities*

**Buttons of the Profile Sources**

.. csv-table::
   :header-rows: 1
   :align: center

   Button, Description
   |plus_green|,  add a new profile source entry
   |cross_red|, remove selected entries

*Profiles*
 * Define the input data from where to take the spectral information from.

*Style*
 * Change style of displayed spectra, i.e. symbol and color

    .. figure:: /img/SpecProfile_style.png
       :align: center
       :width: 300

*Source*
 * Specify a source raster dataset
 * Double-clicking in the cell will open up a dropdown menu where you can select from all loaded raster datasets.

*Sampling*
 * Select *Single Profile* or *Kernel* by double-clicking into the cell.

*Scaling*
 * Choose how spectra are sampled.
 * Define the scaling factors by setting the *Offset* and *Scale* value.

.. csv-table::
   :header-rows: 1
   :widths: auto
   :align: center

   Option, Description
   SingleProfile, Extracts the spectral signature of the pixel at the selected location
   Sample3x3, Extracts spectral signatures of the pixel at the selected location and its adjacent pixels in a 3x3 neighborhood.
   Sample5x5, Extracts spectral signatures of the pixel at the selected location and its adjacent pixels in a 5x5 neighborhood.
   Sample3x3Mean, Extracts the mean spectral signature of the pixel at the selected location and its adjacent pixels in a 3x3 neighborhood.
   Sample5x5Mean, Extracts the mean spectral signature of the pixel at the selected location and its adjacent pixels in a 5x5 neighborhood.


.. _processing_toolbox:

Processing Toolbox
------------------

The processing toolbox is basically the same panel as in QGIS. Here you can find all EnMAP-Box processing algorithms
listed under *EnMAP-Box*. In case it is closed/not visible you can open it by clicking the |processingAlgorithm|
button in the menubar or :menuselection:`View --> Panels --> QGIS Processing Toolbox`.

    .. figure:: /img/processing_toolbox.png
       :align: center
       :width: 300

See `QGIS Documentation - The toolbox <https://docs.qgis.org/latest/en/docs/user_manual/processing/toolbox.html>`_ for further information.

Cursor Location Values
----------------------

This tools lets you inspect the values of a layer or multiple layers at the location where you click in the map view. To select a location (e.g. pixel or feature)
use the |select_location| :superscript:`Select Cursor Location` button together with the |cursorlocationinfo| :sup:`Identify cursor location value` option activated and click somewhere in the map view.

* The Cursor Location Value panel should open automatically and list the information for a selected location. The layers will be listed in the order they appear in the Map View.
  In case you do not see the panel, you can open it via :menuselection:`View --> Panels --> Cursor Location Values`.

    .. figure:: /img/cursorlocationvalues.png
       :align: center
       :width: 300


* By default, raster layer information will only be shown for the bands which are mapped to RGB. If you want to view all bands, change the :guilabel:`Visible` setting
  to :guilabel:`All` (right dropdown menu). Also, the first information is always the pixel coordinate (column, row).
* You can select whether location information should be gathered for :guilabel:`All layers` or only the :guilabel:`Top layer`. You can further
  define whether you want to consider :guilabel:`Raster and Vector` layers, or :guilabel:`Vector only` and :guilabel:`Raster only`, respectively.
* Coordinates of the selected location are shown in the :guilabel:`x` and :guilabel:`y` fields. You may change the coordinate system of the displayed
  coordinates via the |mActionSetProjection| :superscript:`Select CRS` button (e.g. for switching to lat/long coordinates).

Views
======

.. _gui_map_view:

Map View
-----------

The map view allows you to visualize raster and vector data. It is interactive, which means you can move the content or
zoom in/out.

* In order to add a new Map View click the |viewlist_mapdock| :superscript:`Open a Map View` button. Once you added a
  Map View, it will be listed in the ``Data Views`` panel.
* Add layers by either drag-and-dropping them into the Map View (from the Data Sources list) or right-click |mouse_rightclick| onto
  the layer :menuselection:`--> Open in existing map...`
* You can also directly create a new Map View and open a layer by right-clicking |mouse_rightclick| the layer :menuselection:`--> Open in new map`

    .. figure:: /img/mapWindow.png
       :align: center

Linking
^^^^^^^

You can link multiple Map View with each other, so that the contents are synchronized. The following options are
available:

* |link_mapscale_center| Link map scale and center
* |link_mapscale| Link map scale
* |link_center| Link map center

In order to link Map View, go to :menuselection:`View --> Set Map Linking` in the menu bar, which will open the following dialog:

    .. figure:: /img/map_linking.png
       :align: center
       :width: 200

Here you can specify the above mentioned link options between the Map Views. You may either specify linkages between pairs
or link all canvases at once (the :guilabel:`All Canvases` option is only specifiable when the number of Map Views is > 2). Remove
created links by clicking |link_open|.

.. raw:: html

   <div><video width="100%" controls><source src="../../_static/videos/maplinking.webm" type="video/webm">Your browser does not support HTML5 video.</video>
   <p><i>Demonstration of linking two Map Views</i></p></div>

Crosshair
^^^^^^^^^

* Activate the crosshair by right-clicking |mouse_rightclick| into a Map View and select :menuselection:`Crosshair --> Show`
* You can alter the style of the crosshair by right-clicking into a Map View and select :menuselection:`Crosshair --> Style`

    .. figure:: /img/crosshair_style.png
       :align: center
       :width: 300



.. _gui_spectral_library_view:

Spectral Library View
---------------------

The **Spectral Library Window** offers (almost) the same tools like the standard QGIS attribute table. In addition, it provides views and features specifically to visualize and manage spectral profiles.
It directly interacts with the Map View(s), which means spectra can be directly collected from an image. Furthermore, external libraries (e.g. ENVI Spectral Library) can be imported.

Add a new spectral library view by using the *Add Spectral Library Window* |viewlist_spectrumdock| button in the toolbar or open a new window from the menu :menuselection:`View --> Add Spectral Library Window`.

    .. figure:: /img/SpecLib_overview.PNG
       :align: center

*Overview of the Spectral Library view with several collected and labeled spectra and main tools*

**Buttons of the Spectral Library Window**

.. csv-table::
   :header: "Button", "Description", "Button", "Description"
   :widths: auto
   :align: center

   |plus_green|, "Add currently overlaid profiles to the spectral library", |profile_add_auto|, "Activate to add profiles automatically into the spectral library"
   |speclib_add|, "Import Spectral Library", |speclib_save|, "Save Spectral Library"
   |legend|, "Activate to change spectra representation", |speclib_usevectorrenderer|, "Activate to use colors from map vector symbology"
   |system|, "Enter the Spectral Library Layer Properties", |mActionToggleEditing|, "Toggle editing mode"
   |mActionMultiEdit|, "Toggle multi editing mode", |mActionSaveAllEdits|, "Save edits"
   |mActionRefresh|, "Reload the table", |mActionNewTableRow|, "Add feature"
   |mActionDeleteSelected|, "Delete selected features", |mActionEditCut|, "Cut selected rows to clipboard"
   |mActionEditCopy|, "Copy selected rows to clipboard", |mActionEditPaste|, "Paste features from clipboard"
   |mIconExpressionSelect|, "Select by Expression", |mActionSelectAll|, "Select all elements in the spectral library"
   |mActionInvertSelection|, "Invert the current selection", |mActionDeselectAll|, "Remove selection (deselect everything)"
   |mActionSelectedToTop|, "Move selection to the top", |mActionFilter2|, "Select / filter features using form"
   |mActionPanToSelected|, "Pan map to selected rows", |mActionZoomToSelected|, "Zoom map to selected rows"
   |mActionNewAttribute|, "Add New field", |mActionDeleteAttribute|, "Delete field"
   |mActionConditionalFormatting|, "Conditional formatting", |mAction|, "Actions"
   |mActionFormView|, "Switch to form view", |mActionOpenTable|, "Switch to table view"
   |profile_processing|, "Spectral Processing Dialog", |mActionCalculateField|, "Enable to calculate new attribute fields"

.. _spectral_profile_sources:


Collect profiles
^^^^^^^^^^^^^^^^

1. Make sure to enable the |profile| and |select_location| button in the menu bar and open a raster from which you want to collect spectra in a new **Map View**.

    .. figure:: /img/collectProfiles.png
       :align: center
       :width: 400

2. Click on a desired pixel position in the opened raster image and a new Spectral Library window opens with the spectral profile of the respective pixel.
3. Profiles obtained from pixel positions are considered as current or temporary profile candidates. The last profile candidate will be replaced by a new one each time you click on a new pixel position.
4. Click on *Add Profile(s)* |plus_green| to keep the candidate profile in the spectral library. Activate  *Add profiles automatically* |profile_add_auto| to collect multiple profiles and display them all in the same spectral library.

    .. figure:: /img/profile_types.png
       :align: center
       :width: 800

As an alternative to the mouse you can also identify and select pixel profiles using the shortcuts to change, select and add pixel profiles to the Spectral Library.

* First activate the crosshair for the respective image. Click with the right mouse button in the image. Select :guilabel:`Crosshair > Pixel Grid > desired raster image`.
* Now you should see a red square around your pixel and a red dot indicating the position of the pixel profile.

   .. figure:: /img/crosshair.png
      :align: center

* To identify, select and add a pixel profile, use the following key combinations:

.. csv-table::
   :header: "Shortcut", "Action"
   :align: center

   :kbd:`←`/:kbd:`↑`/:kbd:`↓`/:kbd:`→`, "Move the map"
   :kbd:`Ctrl` + :kbd:`←`/:kbd:`↑`/:kbd:`↓`/:kbd:`→`, "Select next pixel in arrow direction"
   :kbd:`Ctrl` + :kbd:`S`, "Add the selected pixel profile candidate"

**Add profiles from another raster image**

Sometimes, you want to compare spectral profiles from different raster sources. The **Spectral Profile Source** panel allows you to change the default settings of the
*Identify* tool so that you can select profiles from different images at the same time.

1. If the Spectral Profile Source Panel is not already visible, open it via :menuselection:`View --> Panels --> Spectral Profile Sources`.
2. Add another profile source relation with |plus_green| and change the :guilabel:`Source` to the desired raster images.
3. If you now collect new spectral information, two profiles will appear in the same Spectral Library Window.

    .. figure:: /img/TwoProfileSources.png
       :align: center
       :width: 800

.. tip::

        Change the color of one of the profile by changing the :guilabel:`Style` in the Spectral Profile Sources.

In a similar way you can compare profiles from the same raster image but using a different sampling methods.

1. In the second relation set the :guilabel:`Source` to the same image as the first relation.
2. Change the :guilabel:`Sampling` to e.g. a 3x3 Kernel mean profile.
3. Collect new pixel profiles.

    .. figure:: /img/KernelProfile.png
       :align: center
       :width: 800

*Spectral Profile Sources Sampling Example*

Adding information
""""""""""""""""""

The attribute table
...................

You can also add more information to your spectral library by using the attribute table.
Add additional fields to the table, e.g. in order to add information to every spectrum (id, name, classification label, ...).

1. Activate the *Table view* |mActionOpenTable| and enable the *Editing mode* |mActionToggleEditing|.
2. Now you can use the *Add Field* |mActionNewAttribute| dialog to add a new column.

    .. figure:: /img/SpecLib_addNewField.png
       :align: center

3. Select a data type of your choice.
4. A new column is added to the attribute table, which you can edit with a double click.
5. To delete a column, use the *Delete field button* |mActionDeleteAttribute|.

.. tip::  When you add a new attribute to the table, you can also choose to use it to store new spectral profiles by checking the **Use to store spectral profiles** checkbox. String, text and binary format can be used to store spectral profiles.

**Add information in the layer properties window**

It is also possible to add new information to the attribute table in the **Layer Properties** of the Spectral Library.

* Click on |system| to open the spectral library properties.
* Navigate to the **Fields** tab and add a new field. *Note:* This view does not allow you to set the option *Use to store spectral profiles*.

    .. figure:: /img/LayerProperties_addField.png
       :align: center

*Overview of the Layer Properties / Fields section*

In addition, the Layer Properties panel allows you to set a certain widget for a specific column.

* Switch to the **Attributes Form** tab in the *Layer Properties*, select the desired column and choose a certain widget type, e.g. a default range, color, spectral profiles etc.

    .. figure:: /img/SpecLib_AddWidget.png
       :align: center

*Selecting widget types for specific columns*

**The field calculator**

The field calculator allows you to modify or assess spectra and calculate new columns or modify existing ones using an expression.

    .. figure:: /img/fieldCalculator.png
      :align: center

*Overview of the Field Calculator*

**Selecting spectra**

Spectra can be selected in the attribute table and in the plot window itself. Selected spectra will be highlighted (blue background in the table; thicker line in a different color in the plot window).

* Hold the :kbd:`Shift` key to select multiple spectra.
* A selection can be removed by clicking the |mActionDeselectAll| button.

    .. figure:: /img/SpecLib_SelectSpectra.png
       :align: center

* Selected spectra can be removed by using the |mActionDeleteSelected| button.

.. tip:: You can inspect an individual value of a spectrum by holding the :kbd:`Alt` key and clicking some position along the spectrum


It is also possible to select and filter profiles with the common vector filter and selection tools, e.g. select spectra by expression:

    .. figure:: /img/SpecLib_SelectByExpr.png
       :align: center

*Select profiles using an expression*

Show coordinates of profiles
............................

Locations of spectra (if available) can be visualized as a point layer by right-clicking |mouse_rightclick| into the map window, and selecting :guilabel:`Add Spectral Library > SpectralLibrary #`

    .. figure:: /img/SpecLib_AddCoords.png
       :align: center
       :width: 400

Advanced options
^^^^^^^^^^^^^^^^

Create / Modify profiles with the Field Calculator
""""""""""""""""""""""""""""""""""""""""""""""""""

As already mentioned, the Field Calculator can modify attribute values of all or selected features.
In addition, the field calculator can be used to calculate spectral profiles.

1. Create a new Spectral Profile field based with *Add Field* |mActionNewAttribute|, use string, text or binary format and tick the *Ise to store Spectral Profiles* box.
2. Open the field calculator |mActionCalculateField| and search for *spectralData* or *spectralMath* in the Spectral Libraries tab.

**SpectralMath** allows you to modify spectral profiles with Python code.

* To use the SpectralMath function, select a field from which to take the spectral profiles, define an expression and the format.

.. code-block:: python

   spectralMath("<profile field 1>", ..., "<profile field n>", '<python code>', '<output format>')


*Note*: The last argument defines the output format. It must correspond to the type you assigned when creating the new column.

    .. figure:: /img/SpecLib_FieldCalc.png
       :align: center

*Example of calculating new spectral profiles*

**SpectralData** returns spectral profile values.

The following table shows some examples of how *spectralMath* and *spectralData* can be used.

.. list-table::
   :widths: 50,50
   :header-rows: 1

   * - Description
     - Example
   * - Multiply the existing profiles
     - *spectralMath("profiles", 'y *=2', 'text')*
   * - Create a new profile with x and y values
     - *spectralMath('x,y=[1,2,3],[20,30,25]')*
   * - Return spectral profile values from map with spectral data from spectral profiles in field column "profiles"
     - *spectralData("profiles")*
   * - Return xUnit string of the spectral profile e.g. 'nm' for wavelength unit
     - *spectralData("profiles")['xUnit']*

.. _gui_spectral_processing:

Spectral Processing
"""""""""""""""""""

    .. figure:: /img/SpecLib_spectralProcessing.png
       :align: center

*Overview of the spectral processing idea*

The Spectral Processing framework allows you to use raster processing algorithms to create new profiles.
Field values of your spectral library will be converted into artificial one-line raster images. In principally, this can be done with most of the field types:

.. list-table::
   :align: center
   :widths: auto
   :header-rows: 1

   * - Field Type
     - Raster Size (band, height, n)
     - type
   * - Spectral Profile
     - nb, 1, n
     - int/float
   * - integer
     - 1, 1, n
     - integer
   * - float
     - 1, 1, n
     - float
   * - text
     - 1, 1, n
     - int (classification)

These temporary raster images are input to standard QGIS processing algorithms or QGIS processing models.
If they generate raster outputs, these outputs can be converted back into field values of the spectral library:

.. list-table::
   :align: center
   :widths: auto
   :header-rows: 1

   * - Raster Output
     - Spectral library Field Type
   * - (>1, 1, n) int/float
     - Spectral Profile
   * - (1, 1, n) int
     - integer
   * - (1, 1, n) float
     - float


This allows you to use the same algorithms to modify spectral profiles as you may want to use to manipulate raster images.
Furthermore, you can make use the QGIS model builder to create (potentially very large and complex) models and use them for both,
spectral libraries and raster image processing.

* To use the :guilabel:`Spectral Processing` tool open |profile_processing| and choose the desired algorithm, e.g. **Spectral resampling**.
* Select the input profiles to be translated to the temporary raster layer and specify the outputs. Select an existing field or enter a name to create a new field.

    .. figure:: /img/SpecLib_specProDialog.png
       :align: center

*Spectral Processing Example*


Visualization settings
^^^^^^^^^^^^^^^^^^^^^^

General profile plot settings
"""""""""""""""""""""""""""""

The Profile Plot displays spectral profiles. Toggling the Profile View icon |profile| shows or hides the plot panel.
This can be useful, for example to enlarge the attribute table and focus on attribute modifications.

You can adjust the extent of the visualized data range and units

* in the plot context menu
* using the mouse cursor while keeping the right mouse button pressed
* in the visualization settings view

    .. figure:: /img/SpecLib_units.png
       :align: center

You can also export the entire plot scene or visible view box by clicking into the plot and select :menuselection:`Export`.

    .. figure:: /img/SpecLib_export.png
       :align: center
       :width: 500

*Export options of the spectral library*

Visualizing profiles
""""""""""""""""""""

The visualization settings of the spectral library allow you to customize the view according to your needs.
You can define multiple visualization groups that describe how profiles from a specific field and with specific attributes should be visualized.

    .. figure:: /img/SpecLib_VisualSettings.png
       :align: center

*Overview of the visualization settings in the Spectral Library window*

* It is also possible, to change the appearance of the Spectral Library window, i.e., bright or dark.
* Moreover, activate or deactivate the crosshair and choose a color.

    .. figure:: /img/SpecLib_themes.png
       :align: center


* The **Current Profiles** section shows you all the spectra that have been collected but do not yet appear in the attribute table. Change the color and symbol, or add a line between the points by double clicking the profile below the *Current Profile* section and adjust the style settings.

**Working with multiple visualization groups**

The spectral library visualization settings also allow you to add several profile *Groups* with different style settings.

* Add a second visualization group with |plus_green|.
* If you want rename *Group "profiles"*.
* Change the color for both groups in the :guilabel:`Color`.
* Under :guilabel:`Field` you can specify which spectral profile column of the attribute table you want to use.

If you have more than one column that stores spectral information, you can have different visualization groups using different profiles.

    .. figure:: /img/SpecLib_visualization1.png
       :align: center

If you have only one column where spectral information is stored, but you have another column storing e.g. class names,
you can use the :guilabel:`Filter` field to define an expression and select only specific class names, e.g. *Impervious* and *Vegetation* and visualize these profiles in different colors.

    .. figure:: /img/SpecLib_visualization2.PNG
       :align: center

Colorize spectra by attribute
"""""""""""""""""""""""""""""

Spectra can be colorized according to their attributes, e.g. their class name.

1. In the :guilabel:`Data Views` panel on the left, right click |mouse_rightclick| on the spectral library that we are currently using and select the **Layer Properties**.
2. Switch to the :guilabel:`Symbology` |symbology| tab and select the **Categorized** renderer at the top.
3. In the **Column** droplist select the desired column and click *Classify*.
4. Confirm with :guilabel:`Ok` and close the window.

    ..  image:: /img/SpecLib_visualization.gif
        :align: center

5. In the :guilabel:`Spectral Library` Window activate the visualization settings with the |mActionAddLegend| button.
6. Right-click on **Color** and select *Use vector symbol colors* |speclib_usevectorrenderer|.


Loading, Saving and Importing / Exporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Load and Save Spectral Libraries
""""""""""""""""""""""""""""""""

Loading or Saving a spectral library means to load or save vector files.

* Load any vector source in the :guilabel:`Data Source Panel` into a :guilabel:`Spectral Library Viewer`.
* The vector layer does not need to contain any Spectral Profile fields. You can add or define them afterwards.

    .. figure:: /img/Load_SpecLib.png
       :align: center
       :width: 300

If your spectral library uses an in-memory vector layer backend, all data will be lost if the layer is closed.
This is the case if the Spectral Library Viewer was opened from scratch with an empty spectral library.
In this case, don’t forget to export collected profiles before closing the Spectral Library Viewer.

If your spectral library already uses a file backend (e.g. .gpkg, .geojson), Style and other layer specific information
are not saved in the data source file, but the QGIS project or a QGIS specific sidecar .qml file.

* Open :menuselection:`Layer properties > Symbology > Style > Save Default` to create or update the .qml file and ensure that the *Spectral Profile* fields will be restored when re-opening the data set.

    .. figure:: /img/SpecLib_defaultStyle.png
       :align: center

Exporting Profiles
""""""""""""""""""

The Export dialog |speclib_save| allows you to export all or selected profiles as Geopackage (.gpkg), GeoJSON (.geoson) or ENVI Spectral Library (.sli).

    .. figure:: /img/SpecLib_exportProfiles.png
       :align: center

The ENVI Spectral Library does not allow saving profiles with different spectral settings (number of bands, wavelength units, FWHM, …)
in the same file. Therefore, you need to select one (out of multiple) profile fields.
Profiles with different spectral settings will be exported into different ENVI files.

Importing Profiles
""""""""""""""""""

* To import none-vector files into an existing spectral librar use the *Import Spectral Library* |speclib_add| button.
* Possible formats to be imported: *ENVI Spectral Library, Geopackage, ASD Field Spectrometer measurements, Raster Layer.*

    .. figure:: /img/SpecLib_ImportFormts.png
       :align: center
       :width: 500

* You can also import ASD Field Spectrometer measurements and map and modify the imported profiles and attributes accordingly.

    .. figure:: /img/SpecLib_addASDProfiles.png
       :align: center
       :width: 500


Spectral Profile JSON format
""""""""""""""""""""""""""""

The EnMAP-Box stores the minimum data to plot a single profile in a JSON object. In its most simple way, this JSON object
contains a single array “y” of length n, with n = number of spectral profile values:

.. code-block:: python

   {
        "y": [43, 23, 45, 63,45]
   }

In this case it can be assumed that the corresponding 'x' values are an increasing band index "x": [0, 1, 2, 3, 4].

The JSON object can describe the "x", the axis units and a vector of bad band values explicitly:

.. csv-table::
   :header: "Member", "Content"
   :align: center

   "y", "An array with n profile values"
   "x", "An array with n profile value locations"
   "yUnit", "String that describes the unit of y values"
   "xUnit", "String that describes the x value unit"
   "bbl", "A bad band list"

Other metadata to describe spectra profiles are stored in additional vector layer fields.

As JSON object, a single hyperspectral EnMAP profile may therefore look like:


.. code-block:: python

   {
      "bbl":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      "x":[0.46,0.465,0.47,0.475,0.479,0.484,0.489,0.494,0.499,0.503,0.508,0.513,0.518,0.523,0.528,0.533,0.538,0.543,0.549,0.554,0.559,0.565,0.57,0.575,0.581,0.587,0.592,0.598,0.604,0.61,0.616,0.622,0.628,0.634,0.64,0.646,0.653,0.659,0.665,0.672,0.679,0.685,0.692,0.699,0.706,0.713,0.72,0.727,0.734,0.741,0.749,0.756,0.763,0.771,0.778,0.786,0.793,0.801,0.809,0.817,0.824,0.832,0.84,0.848,0.856,0.864,0.872,0.88,0.888,0.896,0.915,0.924,0.934,0.944,0.955,0.965,0.975,0.986,0.997,1.007,1.018,1.029,1.04,1.051,1.063,1.074,1.086,1.097,1.109,1.12,1.132,1.144,1.155,1.167,1.179,1.191,1.203,1.215,1.227,1.239,1.251,1.263,1.275,1.287,1.299,1.311,1.323,1.522,1.534,1.545,1.557,1.568,1.579,1.59,1.601,1.612,1.624,1.634,1.645,1.656,1.667,1.678,1.689,1.699,1.71,1.721,1.731,1.742,1.752,1.763,1.773,1.783,2.044,2.053,2.062,2.071,2.08,2.089,2.098,2.107,2.115,2.124,2.133,2.141,2.15,2.159,2.167,2.176,2.184,2.193,2.201,2.21,2.218,2.226,2.234,2.243,2.251,2.259,2.267,2.275,2.283,2.292,2.3,2.308,2.315,2.323,2.331,2.339,2.347,2.355,2.363,2.37,2.378,2.386,2.393,2.401,2.409],
      "xUnit":"Micrometers",
      "y":[405,397,412,410,402,413,421,427,444,446,445,445,476,491,495,504,504,519,532,530,536,539,533,527,529,527,529,526,530,524,520,521,522,523,507,514,505,502,494,497,543,603,703,769,845,930,1007,1096,1178,1249,1314,1359,1388,1386,1419,1432,1432,1435,1471,1498,1479,1487,1482,1499,1507,1517,1509,1534,1532,1507,1557,1527,1552,1605,1534,1555,1577,1564,1582,1600,1611,1643,1659,1678,1684,1672,1687,1659,1697,1624,1612,1602,1576,1515,1508,1513,1522,1542,1575,1602,1632,1649,1663,1639,1602,1587,1530,977,996,1026,1063,1086,1108,1123,1169,1177,1191,1194,1210,1222,1208,1201,1187,1182,1146,1157,1112,1093,1085,1096,1058,1041,754,781,804,796,780,792,812,825,851,803,812,836,834,818,823,842,842,860,851,880,844,856,847,846,819,842,820,754,768,731,728,750,695,735,675,718,640,601,684,744,635,568,696,637,592]}
   }

Note that conceptually profile objects can differ in its wavelength etc.

Text View
---------

    .. figure:: /img/textWindow.png
       :align: center

Attribute Table View
--------------------

.. todo:: ...


.. AUTOGENERATED SUBSTITUTIONS - DO NOT EDIT PAST THIS LINE

.. |GEE| image:: /img/icons/GEE.svg
   :width: 28px
.. |add_datasource| image:: /img/icons/add_datasource.svg
   :width: 28px
.. |cross_red| image:: /img/icons/cross_red.svg
   :width: 28px
.. |cursorlocationinfo| image:: /img/icons/cursorlocationinfo.svg
   :width: 28px
.. |legend| image:: /img/icons/legend.svg
   :width: 28px
.. |link_basic| image:: /img/icons/link_basic.svg
   :width: 28px
.. |link_center| image:: /img/icons/link_center.svg
   :width: 28px
.. |link_mapscale| image:: /img/icons/link_mapscale.svg
   :width: 28px
.. |link_mapscale_center| image:: /img/icons/link_mapscale_center.svg
   :width: 28px
.. |link_open| image:: /img/icons/link_open.svg
   :width: 28px
.. |locationbrowser| image:: /img/icons/locationbrowser.svg
   :width: 28px
.. |mAction| image:: /img/icons/mAction.svg
   :width: 28px
.. |mActionAddLegend| image:: /img/icons/mActionAddLegend.svg
   :width: 28px
.. |mActionCalculateField| image:: /img/icons/mActionCalculateField.svg
   :width: 28px
.. |mActionCapturePoint| image:: /img/icons/mActionCapturePoint.svg
   :width: 28px
.. |mActionCapturePolygon| image:: /img/icons/mActionCapturePolygon.svg
   :width: 28px
.. |mActionCollapseTree| image:: /img/icons/mActionCollapseTree.svg
   :width: 28px
.. |mActionConditionalFormatting| image:: /img/icons/mActionConditionalFormatting.svg
   :width: 28px
.. |mActionDataSourceManager| image:: /img/icons/mActionDataSourceManager.svg
   :width: 28px
.. |mActionDeleteAttribute| image:: /img/icons/mActionDeleteAttribute.svg
   :width: 28px
.. |mActionDeleteSelected| image:: /img/icons/mActionDeleteSelected.svg
   :width: 28px
.. |mActionDeselectAll| image:: /img/icons/mActionDeselectAll.svg
   :width: 28px
.. |mActionEditCopy| image:: /img/icons/mActionEditCopy.svg
   :width: 28px
.. |mActionEditCut| image:: /img/icons/mActionEditCut.svg
   :width: 28px
.. |mActionEditPaste| image:: /img/icons/mActionEditPaste.svg
   :width: 28px
.. |mActionExpandTree| image:: /img/icons/mActionExpandTree.svg
   :width: 28px
.. |mActionFilter2| image:: /img/icons/mActionFilter2.svg
   :width: 28px
.. |mActionFormView| image:: /img/icons/mActionFormView.svg
   :width: 28px
.. |mActionInvertSelection| image:: /img/icons/mActionInvertSelection.svg
   :width: 28px
.. |mActionMultiEdit| image:: /img/icons/mActionMultiEdit.svg
   :width: 28px
.. |mActionNewAttribute| image:: /img/icons/mActionNewAttribute.svg
   :width: 28px
.. |mActionNewTableRow| image:: /img/icons/mActionNewTableRow.svg
   :width: 28px
.. |mActionOpenTable| image:: /img/icons/mActionOpenTable.svg
   :width: 28px
.. |mActionPan| image:: /img/icons/mActionPan.svg
   :width: 28px
.. |mActionPanToSelected| image:: /img/icons/mActionPanToSelected.svg
   :width: 28px
.. |mActionRefresh| image:: /img/icons/mActionRefresh.svg
   :width: 28px
.. |mActionRemove| image:: /img/icons/mActionRemove.svg
   :width: 28px
.. |mActionSaveAllEdits| image:: /img/icons/mActionSaveAllEdits.svg
   :width: 28px
.. |mActionSaveEdits| image:: /img/icons/mActionSaveEdits.svg
   :width: 28px
.. |mActionSelectAll| image:: /img/icons/mActionSelectAll.svg
   :width: 28px
.. |mActionSelectRectangle| image:: /img/icons/mActionSelectRectangle.svg
   :width: 28px
.. |mActionSelectedToTop| image:: /img/icons/mActionSelectedToTop.svg
   :width: 28px
.. |mActionSetProjection| image:: /img/icons/mActionSetProjection.svg
   :width: 28px
.. |mActionToggleEditing| image:: /img/icons/mActionToggleEditing.svg
   :width: 28px
.. |mActionZoomActual| image:: /img/icons/mActionZoomActual.svg
   :width: 28px
.. |mActionZoomFullExtent| image:: /img/icons/mActionZoomFullExtent.svg
   :width: 28px
.. |mActionZoomIn| image:: /img/icons/mActionZoomIn.svg
   :width: 28px
.. |mActionZoomOut| image:: /img/icons/mActionZoomOut.svg
   :width: 28px
.. |mActionZoomToSelected| image:: /img/icons/mActionZoomToSelected.svg
   :width: 28px
.. |mIconExpressionSelect| image:: /img/icons/mIconExpressionSelect.svg
   :width: 28px
.. |mIconLineLayer| image:: /img/icons/mIconLineLayer.svg
   :width: 28px
.. |mIconRasterClassification| image:: /img/icons/mIconRasterClassification.svg
   :width: 28px
.. |mIconRasterImage| image:: /img/icons/mIconRasterImage.svg
   :width: 28px
.. |mIconRasterLayer| image:: /img/icons/mIconRasterLayer.svg
   :width: 28px
.. |mIconRasterMask| image:: /img/icons/mIconRasterMask.svg
   :width: 28px
.. |metadata| image:: /img/icons/metadata.svg
   :width: 28px
.. |mouse_rightclick| image:: /img/icons/mouse_rightclick.svg
   :width: 28px
.. |mouse_wheel| image:: /img/icons/mouse_wheel.svg
   :width: 28px
.. |pan_center| image:: /img/icons/pan_center.svg
   :width: 28px
.. |plus_green| image:: /img/icons/plus_green.svg
   :width: 28px
.. |processingAlgorithm| image:: /img/icons/processingAlgorithm.svg
   :width: 28px
.. |profile| image:: /img/icons/profile.svg
   :width: 28px
.. |profile_add_auto| image:: /img/icons/profile_add_auto.svg
   :width: 28px
.. |profile_processing| image:: /img/icons/profile_processing.svg
   :width: 28px
.. |profileanalytics| image:: /img/icons/profileanalytics.svg
   :width: 28px
.. |qgis_icon| image:: /img/icons/qgis_icon.svg
   :width: 28px
.. |rasterbandstacking| image:: /img/icons/rasterbandstacking.svg
   :width: 28px
.. |select_location| image:: /img/icons/select_location.svg
   :width: 28px
.. |sensorimport| image:: /img/icons/sensorimport.svg
   :width: 28px
.. |speclib| image:: /img/icons/speclib.svg
   :width: 28px
.. |speclib_add| image:: /img/icons/speclib_add.svg
   :width: 28px
.. |speclib_save| image:: /img/icons/speclib_save.svg
   :width: 28px
.. |speclib_usevectorrenderer| image:: /img/icons/speclib_usevectorrenderer.svg
   :width: 28px
.. |symbology| image:: /img/icons/symbology.svg
   :width: 28px
.. |system| image:: /img/icons/system.svg
   :width: 28px
.. |viewlist_mapdock| image:: /img/icons/viewlist_mapdock.svg
   :width: 28px
.. |viewlist_spectrumdock| image:: /img/icons/viewlist_spectrumdock.svg
   :width: 28px
.. |viewlist_textview| image:: /img/icons/viewlist_textview.svg
   :width: 28px
