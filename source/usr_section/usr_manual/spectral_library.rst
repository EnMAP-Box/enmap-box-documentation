.. include:: /icon_links.rst

.. _spectral_libraries:

==================
Spectral Libraries
==================
A *Spectral Library* is a library is a vector layer with a layer field designated to store spectral profiles.


Overview
========

Spectral Library Window |viewlist_spectrumdock|
-----------------------------------------------

The **Spectral Library Window** offers (almost) the same tools like the standard QGIS attribute table. In addition, it provides views and features specifically to visualize and manage spectral profiles.
It directly interacts with the Map View(s), which means spectra can be directly collected from an image. Furthermore, external libraries (e.g. ENVI Spectral Library) can be imported.

Add a new spectral library view by using the *Add Spectral Library Window* |viewlist_spectrumdock| button in the toolbar or open a new window from the menu :menuselection:`View --> Add Spectral Library Window`.

.. figure:: /img/SpecLib_overview.PNG
   :width: 100%
Overview of the Spectral Library view with several collected and labeled spectra and main tools

**Buttons of the Spectral Library Window**

.. csv-table::
   :header: "Button", "Description", "Button", "Description"
   :widths: auto

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
    :width: 100%

    *Overview of the Spectral Profile Sources Window with two labeled spectra and main functionalities*

**Buttons of the Profile Sources**

.. csv-table::
   :header-rows: 1
   :width: 50%

   Button, Description
   |plus_green|,  add a new profile source entry
   |cross_red|, remove selected entries

*Profiles*
 * Define the input data from where to take the spectral information from.

*Style*
 * Change style of displayed spectra, i.e. symbol and color

    .. figure:: /img/SpecProfile_style.png
       :width: 50%

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

   Option, Description
   SingleProfile, Extracts the spectral signature of the pixel at the selected location
   Sample3x3, Extracts spectral signatures of the pixel at the selected location and its adjacent pixels in a 3x3 neighborhood.
   Sample5x5, Extracts spectral signatures of the pixel at the selected location and its adjacent pixels in a 5x5 neighborhood.
   Sample3x3Mean, Extracts the mean spectral signature of the pixel at the selected location and its adjacent pixels in a 3x3 neighborhood.
   Sample5x5Mean, Extracts the mean spectral signature of the pixel at the selected location and its adjacent pixels in a 5x5 neighborhood.

Working with the Spectral Library
=================================

Collect profiles
-----------------

1. Make sure to enable the |profile| and |select_location| button in the menu bar and open a raster from which you want to collect spectra in a new **Map View**.

.. figure:: /img/collectProfiles.png
   :align: center
   :width: 60%

2. Click on a desired pixel position in the opened raster image and a new Spectral Library window opens with the spectral profile of the respective pixel.
3. Profiles obtained from pixel positions are considered as current or temporary profile candidates. The last profile candidate will be replaced by a new one each time you click on a new pixel position.
4. Click on *Add Profile(s)* |plus_green| to keep the candidate profile in the spectral library. Activate  *Add profiles automatically* |profile_add_auto| to collect multiple profiles and display them all in the same spectral library.

.. figure:: /img/profile_types.png
   :align: center
   :width: 100%

As an alternative to the mouse you can also identify and select pixel profiles using the shortcuts to change, select and add pixel profiles to the Spectral Library.

* First activate the crosshair for the respective image. Click with the right mouse button in the image. Select :guilabel:`Crosshair > Pixel Grid > desired raster image`.
* Now you should see a red square around your pixel and a red dot indicating the position of the pixel profile.

.. figure:: /img/crosshair.png
   :align: center
   :width: 100%

* To identify, select and add a pixel profile, use the following key combinations:

.. csv-table::
   :header: "Shortcut", "Action"
   :widths: auto

   Arrow, "Move the map"
   CTRL + Arrow, "Select next pixel in arrow direction"
   CTRL + S, "Add the selected pixel profile candidate"

**Add profiles from another raster image**

Sometimes, you want to compare spectral profiles from different raster sources. The **Spectral Profile Source** panel allows you to change the default settings of the
*Identify* tool so that you can select profiles from different images at the same time.

1. If the Spectral Profile Source Panel is not already visible, open it via :menuselection:`View --> Panels --> Spectral Profile Sources`.
2. Add another profile source relation with |plus_green| and change the :guilabel:`Source` to the desired raster images.
3. If you now collect new spectral information, two profiles will appear in the same Spectral Library Window.

.. figure:: /img/TwoProfileSources.png
   :align: center
   :width: 100%

.. tip::

        Change the color of one of the profile by changing the :guilabel:`Style` in the Spectral Profile Sources.

In a similar way you can compare profiles from the same raster image but using a different sampling methods.

1. In the second relation set the :guilabel:`Source` to the same image as the first relation.
2. Change the :guilabel:`Sampling` to e.g. a 3x3 Kernel mean profile.
3. Collect new pixel profiles.

.. figure:: /img/KernelProfile.png
   :align: center
   :width: 100%

Adding information
-------------------

The attribute table
~~~~~~~~~~~~~~~~~~~~~~

You can also add more information to your spectral library by using the attribute table.
Add additional fields to the table, e.g. in order to add information to every spectrum (id, name, classification label, ...).

1. Activate the *Table view* |mActionOpenTable| and enable the *Editing mode* |mActionToggleEditing|.
2. Now you can use the *Add Field* |mActionNewAttribute| dialog to add a new column.

.. figure:: /img/SpecLib_addNewField.png
    :width: 80%

3. Select a data type of your choice.
4. A new column is added to the attribute table, which you can edit with a double click.
5. To delete a column, use the *Delete field button* |mActionDeleteAttribute|.

.. tip::  When you add a new attribute to the table, you can also choose to use it to store new spectral profiles by checking the **Use to store spectral profiles** checkbox. String, text and binary format can be used to store spectral profiles.

**Add information in the layer properties window**

It is also possible to add new information to the attribute table in the **Layer Properties** of the Spectral Library.

* Click on |system| to open the spectral library properties.
* Navigate to the **Fields** tab and add a new field. *Note:* This view does not allow you to set the option *Use to store spectral profiles*.

.. figure:: /img/LayerProperties_addField.png
   :width: 100%

   *Overview of the Layer Properties / Fields section*

In addition, the Layer Properties panel allows you to set a certain widget for a specific column.

* Switch to the **Attributes Form** tab in the *Layer Properties*, select the desired column and choose a certain widget type, e.g. a default range, color, spectral profiles etc.

.. figure:: /img/SpecLib_AddWidget.png
   :width: 100%

   *Selecting widget types for specific columns*

**The field calculator**

The field calculator allows you to modify or assess spectra and calculate new columns or modify existing ones using an expression.

.. figure:: /img/fieldCalculator.png
   :width: 100%

   *Overview of the field calculator*

**Selecting spectra**

Spectra can be selected in the attribute table and in the plot window itself. Selected spectra will be highlighted (blue background in the table; thicker line in a different color in the plot window).

* Hold the :kbd:`Shift` key to select multiple spectra.
* A selection can be removed by clicking the |mActionDeselectAll| button.

.. figure:: /img/SpecLib_SelectSpectra.png
    :width: 100%

* Selected spectra can be removed by using the |mActionDeleteSelected| button.

.. tip:: You can inspect an individual value of a spectrum by holding the :kbd:`Alt` key and clicking some position along the spectrum


It is also possible to select and filter profiles with the common vector filter and selection tools, e.g. select spectra by expression:

.. figure:: /img/SpecLib_SelectByExpr.png
   :width: 100%
   *Select profiles using an expression*

Show coordinates of profiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Locations of spectra (if available) can be visualized as a point layer by right-clicking into the map window, and selecting :guilabel:`Add Spectral Library > SpectralLibrary #`

.. figure:: /img/SpecLib_AddCoords.png
   :align: center
   :width: 50%

Advanced options
----------------

Create / Modify profiles with the Field Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As already mentioned, the Field Calculator can modify attribute values of all or selected features.
In addition, the field calculator can be used to calculate spectral profiles.

1. Create a new Spectral Profile field based with *Add Field* |mActionNewAttribute|, use string, text or binary format and tick the *Ise to store Spectral Profiles* box.
2. Open the field calculator |mActionCalculateField| and search for *spectralData* or *spectralMath* in the Spectral Libraries tab.

**SpectralMath** allows you to modify spectral profiles with Python code.

* To use the SpectralMath function, select a field from which to take the spectral profiles, define an expression and the format.
*Note*: The last argument defines the output format. It must correspond to the type you assigned when creating the new column.

.. code-block:: python

   spectralMath("<profile field 1>", ..., "<profile field n>", '<python code>', '<output format>')


**SpectralData** returns spectral profile values.


.. csv-table::
   :header-rows: 1
   :width: auto

   Description, Example
   Multiply the existing profiles, *spectralMath("profiles", 'y *=2', 'text')*
   Create a new profile with x and y values, *spectralMath('x,y=[1,2,3],[20,30,25]')*
   Return spectral profile values from map with spectral data from spectral profiles in field column *profiles*, *spectralData("profiles")*
   Return xUnit string of the spectral profile e.g. 'nm' for wavelength unit, *spectralData("profiles")['xUnit']*


.. figure:: /img/SpecLib_FieldCalc.png
   :width: 100%

   *Example of calculating new spectral profiles*

Spectral Processing
~~~~~~~~~~~~~~~~~~~
The Spectral Processing framework allows you to use raster processing algorithms to create new profiles.
Field values of your spectral library will be converted into artificial one-line raster images.

.. figure:: /img/SpecLib_spectralProcessing.png
   :align: center
   :width: 80%

   *Overview of the spectral processing idea*

Each column of the spectral library attribute table is derived and translated into meaningful temporary raster image values, regardless of the column type.

.. figure:: /img/SpecLib_TypeMapping.png
   :align: center
   :width: 80%

   *Type mapping for the spectral processing*

These temporary raster images are input to standard QGIS processing algorithms or QGIS processing models.
If they generate raster outputs, these outputs can be converted back into field values of the spectral library:


.. csv-table::
   :header: "Raster Output", "Speclib Field Type"
   :width: auto

   (>1, 1, n) int/float, Spectral Profile
   (1, 1, n) int, int
   (1, 1, n) float, float

This allows you to use the same algorithms to modify spectral profiles as you may want to use to manipulate raster images.
Furthermore, you can make use the QGIS model builder to create (potentially very large and complex) models and use them for both,
spectral libraries and raster image processing.

* To use the :guilabel:`Spectral Processing` tool open |profile_processing| and choose the desired algorithm, e.g. **Spectral resampling**.
* Select the input profiles to be translated to the temporary raster layer and specify the outputs. Select an existing field or enter a name to create a new field.

.. figure:: /img/SpecLib_specProDialog.png
   :align: center
   :width: 80%

Visualization settings
=================================

General profile plot settings
-----------------------------
The Profile Plot displays spectral profiles. Toggling the Profile View icon |profile| shows or hides the plot panel.
This can be useful, for example to enlarge the attribute table and focus on attribute modifications.

You can adjust the extent of the visualized data range and units

* in the plot context menu
* using the mouse cursor while keeping the right mouse button pressed
* in the visualization settings view

.. figure:: /img/SpecLib_units.png
    :width: 100%

You can also export the entire plot scene or visible view box by clicking into the plot :menuselection:`Export`.

.. figure:: /img/SpecLib_export.png
   :align: center
   :width: 50%

Visualizing profiles
--------------------

The visualization settings of the spectral library allow you to customize the view according to your needs.
You can define multiple visualization groups that describe how profiles from a specific field and with specific attributes should be visualized.

.. figure:: /img/SpecLib_VisualSettings.png
   :width: 100%
   *Overview of the visualization settings in the Spectral Library window*

* It is also possible, to change the appearance of the Spectral Library window, i.e., bright or dark.
* Moreover, activate or deactivate the crosshair and choose a color.

.. figure:: /img/SpecLib_themes.png
   :align: center
   :width: 80%

* The **Current Profiles** section shows you all the spectra that have been collected but do not yet appear in the attribute table. Change the color and symbol, or add a line between the points by double clicking the profile below the *Current Profile* section and adjust the style settings.

**Working with multiple visualization groups**

The spectral library visualization settings also allow you to add several profile *Groups* with different style settings.

* Add a second visualization group with |plus_green|.
* If you want rename *Group "profiles"*.
* Change the color for both groups in the :guilabel:`Color`.
* Under :guilabel:`Field` you can specify which spectral profile column of the attribute table you want to use.
If you have more than one column that stores spectral information, you can have different visualization groups using different profiles.

.. figure:: /img/SpecLib_visualization1.png
   :width: 100%

If you have only one column where spectral information is stored, but you have another column storing e.g. class names,
you can use the :guilabel:`Filter` field to define an expression and select only specific class names, e.g. *Impervious* and *Vegetation* and visualize these profiles in different colors.

.. figure:: /img/SpecLib_visualization2.png
   :width: 100%

Colorize spectra by attribute
-----------------------------

Spectra can be colorized according to their attributes, e.g. their class name.

1. In the :guilabel:`Data Views` panel on the left, right click on the spectral library that we are currently using and select the **Layer Properties**.
2. Switch to the :guilabel:`Symbology` |symbology| tab and select the **Categorized** renderer at the top.
3. In the **Column** droplist select the desired column and click *Classify*.
4. Confirm with :guilabel:`Ok` and close the window.

..  image:: /img/SpecLib_visualization.gif
    :width: 100%

5. In the :guilabel:`Spectral Library` Window activate the visualization settings with the |mActionAddLegend| button.
6. Right-click on **Color** and select *Use vector symbol colors* |speclib_usevectorrenderer|.


Loading, Saving and Importing / Exporting
====================================================

Load and Save Spectral Libraries
---------------------------------

Loading or Saving a spectral library means to load or save vector files.

* You can load any vector source in the :guilabel:`Data Source Panel` into a :guilabel:`Spectral Library Viewer.
* The vector layer does not need to contain any Spectral Profile fields. You can add or define them afterwards.

.. figure:: /img/Load_SpecLib.png
   :align: center
   :width: 60%

If your spectral library uses an in-memory vector layer backend, all data will be lost if the layer is closed.
This is the case if the Spectral Library Viewer was opened from scratch with an empty spectral library.
In this case, don’t forget to export collected profiles before closing the Spectral Library Viewer.

If your spectral library already uses a file backend (e.g. *.gpkg, *.geojson), Style and other layer specific information
are not saved in the data source file, but the QGIS project or a QGIS specific sidecar .qml file.

* Open :menuselection:`Layer properties > *ymbology > Style > Save Default` to create or update the .qml file and ensure that the *Spectral Profile* fields will be restored when re-opening the data set.

.. figure:: /img/SpecLib_defaultStyle.png
   :align: center
   :width: 40%

Exporting Profiles
------------------
The Export dialog |speclib_save| allows you to export all or selected profiles as Geopackage (.gpkg), GeoJSON (.geoson) or ENVI Spectral Library (*.sli).

.. figure:: /img/SpecLib_exportProfiles.png
   :align: center
   :width: 60%

The ENVI Spectral Library does not allow saving profiles with different spectral settings (number of bands, wavelength units, FWHM, …)
in the same file. Therefore, you need to select one (out of multiple) profile fields.
Profiles with different spectral settings will be exported into different ENVI files.

Importing Profiles
------------------
* To import none-vector files into an existing spectral librar use the *Import Spectral Library* |speclib_add| button.
* Possible formats to be imported: *ENVI Spectral Library, Geopackage, ASD Field Spectrometer measurements, Raster Layer.*

.. figure:: /img/SpecLib_ImportFormts.png
   :align: center
   :width: 60%

* You can also import ASD Field Spectrometer measurements and map and modify the imported profiles and attributes accordingly.

.. figure:: /img/SpecLib_addASDProfiles.png
   :align: center
   :width: 60%

Spectral Profile JSON format
=============================
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
   :width: auto

   y, An array with n profile values
   x, "An array with n profile value locations, e.g. the band wavelength"
   yUnit, "String that describes the unit of y values, e.g. "Reflectance""
   xUnit, "String that describes the x value unit, e.g. “nm” or "Nanometers""
   bbl, "A “bad band list”, i.e. a vector with n bad-band multipliers. 0 = masked, > 0 = not masked"

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