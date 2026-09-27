.. _gui:

GUI
###

    .. figure:: /img/manual_gui.png
       :align: center
       :width: 100%

       Overview of the EnMAP-Box

.. _gui_toolbar:

Toolbar
=======

In the toolbar you can find the most common tasks. See table below for information on different buttons and their functionality.

* It is possible to enable and disable the different tools: Right-click |mouse_rightclick| on the toolbar and check or uncheck the desired
  toolbar.

    .. figure:: /img/toolbarView.png
       :align: center
       :width: 100%

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
       :width: 100%

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
       :width: 100%

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

Attribute Table View
--------------------

The *Attribute Table View* lists the attribute data of a vector layer feature by feature.
It can be opened in different ways, e.g., from the context menu of a vector data source
in the *Data Sources* panel or a vector layer in the layer tree of a *Data View*,
using the |mActionOpenTable| button, or via *Layer* | *Open Attribute Table* in QGIS.

The Attribute Table View offers two alternative presentations of the same data:
the **Table View**, which shows all features in a spreadsheet-like grid, and the
**Form View**, which shows the attributes of a single, selected feature in a structured form.

**Buttons of the Attribute Table**

.. csv-table::
   :header: "Button", "Description", "Button", "Description"
   :widths: auto
   :align: center

   |mActionCalculateField|, "Enable to calculate new attribute fields", |mActionToggleEditing|, "Toggle editing mode"
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

Table View
^^^^^^^^^^

In the *Table View* (|mActionOpenTable|), each row corresponds to a single feature and
each column to one of its attributes (fields). This is the best choice when you want to
inspect many features at once, sort or filter them, edit values in bulk, or select features
by an attribute query.

.. figure:: /img/attributetable_tableview.png
   :align: center
   :width: 40%

   Attribute Table View of the ``speclib_potsdam`` layer, shown in *Table View*.
   The selected feature (green) is also selected in the map and in the spectral library plot.

The toolbar at the top provides the usual editing and selection tools, e.g., toggle editing
(|mActionToggleEditing|), the field calculator (|mActionCalculateField|) and filtering (|mActionFilter2|). The bar at the bottom allows you
to filter the displayed features (e.g., *Show all features*, *Selected features*,
*Visible features*, *Edited features* or a custom expression).


Form View
^^^^^^^^^

In the *Form View* (|mActionFormView|), the attributes of the currently selected feature are
displayed one at a time, using a dedicated widget for each field. This is particularly useful
for attributes with a specialised widget, such as the *Spectral Profile* field of a spectral
library, which is rendered as an interactive plot rather than as plain text. The Form View is
the right choice when you want to inspect or edit a single feature in detail.

.. figure:: /img/attributetable_formview.png
   :align: center

   The same ``speclib_potsdam`` layer, shown in *Form View*. The left panel lists the
   features (here: 1 / 15) and the right panel shows the attributes of the selected feature,
   including the spectral profile plotted as a graph.

Use the navigation controls at the bottom of the feature list (first, previous, next, last)
to step through the features. The form updates automatically to the selected feature.


Table View vs. Form View
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Differences between the two presentations
   :header-rows: 1
   :align: center

   * - Aspect
     - Table View
     - Form View
   * - Layout
     - Grid of rows (features) and columns (fields)
     - One feature at a time, with labelled fields
   * - Best for
     - Overview, sorting, filtering, bulk edits
     - Detailed inspection and editing of a single feature
   * - Selection
     - Row selection highlights the feature in map/plot
     - Steps through features with navigation controls
   * - Special widgets
     - Not shown (values only)
     - Rendered, e.g. spectral profile as a plot


Optimizing the Form View with the Drag and Drop Designer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the Form View lists all attributes in the order they appear in the data source.
You can re-order and group the fields, and even organise them into tabs, using the
*Drag and Drop Designer* in the layer's *Attributes Form* settings.

#. Open the layer properties (e.g., right-click the layer |mActionOpenTable| in the layer tree
   and select *Properties*), then go to the *Attributes Form* tab.
#. At the top, switch the designer from *Autogenerate* to **Drag and Drop Designer**.
#. Drag the fields you want to group from the *Available Widgets* panel into the *Form Layout*
   panel. Use the green plus button to add a **Group** or **Tab** container and
   give it a title (e.g., ``My Attributes``).
#. Optionally set a user-friendly *Alias* or a dedicated *Widget Type* for individual fields.
#. Confirm with *OK*. The next time you open the attribute table in *Form View*, the fields
   appear in the optimised, grouped layout.

.. figure:: /img/atttributetab_drag&drop_attform.png
   :align: center

   *Layer Properties* | *Attributes Form* with the *Drag and Drop Designer* active.
   The fields ``level_1``, ``level_2`` and ``level_3`` are grouped under a tab named
   ``My Attributes``.

The optimised layout is also reflected when the attribute table is opened in *Form View*:

.. figure:: /img/atttributetab_drag&drop.png
   :align: center

   Resulting *Form View* of the ``landcover_potsdam`` layer, with the fields
   ``level_1``, ``level_2`` and ``level_3`` neatly grouped under the ``My Attributes`` tab.

Spectral Library View
---------------------

The **Spectral Library Viewer** displays and manages spectral profiles and connects them with map views and vector-layer attributes. Open it with the *Open a Spectral Library View* |viewlist_spectrumdock| button or from :menuselection:`View --> Add Spectral Library Window`.

The viewer combines a spectral profile plot with tools for adding, importing, saving, refreshing, and configuring profiles. The main toolbar and plot layout are shown below; the detailed operation of each feature is documented in :doc:`speclibs`.

    .. figure:: /img/SpecLib_overview.png
       :align: center
       :width: 100%

       Overview of the Spectral Library View with the profile plot, visualization settings, and main toolbar.

**Buttons of the Spectral Library Window**

.. csv-table::
   :header: "Button", "Description", "Button", "Description"
   :widths: auto
   :align: center

   |plus_green|, "Add currently overlaid profiles to the spectral library", |mActionRefresh|, "Refresh the Spectral Library Plot"
   |speclib_add|, "Import Spectral Library", |speclib_save|, "Save Spectral Library"
   |legend|, "Activate to change spectra representation", |profile_processing|, "Spectral Processing Dialog"
   |system|, "Enter the Spectral Library Layer Properties",|mActionOpenTable|, "Open Attribute Table"

.. _spectral_profile_sources:

The viewer supports collecting profiles from raster data, organizing and styling profile visualizations, inspecting and editing attributes, and importing or exporting spectral libraries. The dedicated :ref:`Spectral Library Viewer <spectral_library_viewer>` section in :doc:`speclibs` explains these workflows in detail, including:

* :ref:`viewer configuration and profile visualization <spectral_library_viewer>`
* :ref:`attribute tables and form views <attribute_table>`
* :ref:`profile fields and data formats <profile_fields>`
* :ref:`collecting profiles <speclib_collect_profiles>`
* :ref:`importing profiles <speclib_import_profiles>`
* :ref:`exporting profiles <speclib_export_profiles>`

For a general introduction to spectral libraries and their supported workflows, see :doc:`speclibs`.

Text View
---------

The text view provides a simple place to store metadata, notes, or other text alongside the project.

    .. figure:: /img/textWindow.png
       :align: center

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
