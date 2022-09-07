.. include:: /icon_links.rst

.. _spectral_libraries:

==================
Spectral Libraries
==================
A *Spectral Library* is a library is a vector layer with a layer field designated to store spectral profiles.


Spectral Library View |viewlist_spectrumdock|
=============================================

The *Spectral Library View* can be used to visualize, collect and label spectra. It directly interacts with the Map View(s), which
means spectra can be directly collected from an image. Furthermore, external libraries (ENVI Spectral Library) can be imported.

*Add a new spectral library view by using the *Add Spectral Library View* |viewlist_spectrumdock| button in the toolbar or open a new window from the menu bar :menuselection:`View --> Add Spectral Library Window`.

A new view appears where you can start to collect spectra.

.. figure:: /img/SpecLib_overview.PNG
   :width: 100%

   Overview of the Spectral Library view with several collected and labeled spectra and main tools

**Buttons of the Spectral Library Window:**

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
========================

This menu manages the connection between raster sources and spectral library windows.

.. figure:: /img/SpectralProfileSources.png
    :width: 60%

    Overview of the Spectral Profile Sources Window with two labeled spectra and main functionalities

**Buttons of the Profile Sources**
----------------------------------

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

        ..

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

**Calculating profiles**
------------------------

Different spectral profiles can be calculated in the **Spectral Profile Sources** window.

* Add a new column in the attribute table with a meaningful name and select **Type** *Spectral Profile*
* In the Spectral Profile Sources window navigate to the newly created attribute, select the **Source** and switch from *Single Profile* to *Kernel*.
* Choose the **Kernel** you want to use and the **Aggregation** method.

.. figure:: /img/SpecLib_CalculateSpectra.png
    :width: 80%

    ..

* Collect spectra in the image and visualize the profiles in different colors using the visualization settings.
* Change the color of the different profiles (see also section **Colorize spectra by attribute**).

.. figure:: /img/SpecLib_CalculateSpectraVisualization.png
    :width: 100%

    ..

Working with the Spectral Library
=================================

Collecting spectra
------------------

* Make sure to enable the |profile| button in the menu bar and open a raster from which you want to collect spectra in a new *Map Window*.
* Click on a desired location in the *Map Window*. The pixels spectral profile at this location will now be shown in
  the plot in the *Library Window*. Mind that this will only visualize the spectrum, but nothing is saved at this point.
* To add/save a selected spectrum to the library, click the |plus_green| button: A new table entry on the right of the window is added.
* If spectra should be added automatically to the library while a pixel is selected or clicked, enable the |profile_add_auto| button.

.. tip::

   Have a look at the :ref:`Spectral Profile Sources <spectral_profile_sources>` window for more advanced settings
   collecting spectra.

If you want to only collect spectra for one class, e.g. water, define the class in the *Spectral Profile Source* view under the desired column name, e.g. **level_1**.
If you now click into the image, the spectra is automatically added and named as water in the previously specified column.

.. figure:: /img/SpecLib_collectProfilesByName.gif
    :width: 100%

    ..

The attribute table
-------------------

**Adding information**
~~~~~~~~~~~~~~~~~~~~~~

Add additional fields to the table, e.g. in order to add information to every spectrum (id, name, classification label, ...).

1. Enable the *Editing mode* by activating  |mActionToggleEditing|.
2. Now you can use the |mActionNewAttribute| button to add a new field (mind the type!).

.. figure:: /img/SpecLib_addNewField.png
    :width: 80%

    ..

3.  Add information to the new column by double-clicking it.
4.  Delete a column, by using the *Delete field button* |mActionDeleteAttribute|

.. tip::  When you add a new attribute to the table, you can also choose to use it to store new spectral profiles by checking the **Use to store spectral profiles** checkbox. String, text and binary format can be used to store spectral profiles.

*Adding information through layer properties window*

It is also possible to add new information to the attribute table in the **Layer Properties** of the Spectral Library.

* Click on |mActionToggleEditing| to open the spectral library properties.
* Navigate to the **Fields** tab and add a new field.

Furthermore, you can define a default widget for the different columns in the attribute table.

* Switch to the **Attributes Form** tab, select the desired column and choose a certain widget type, e.g. a default range, color, spectral profiles etc.

.. figure:: /img/SpecLib_AddWidget.png
    :width: 100%

    ..

*The field calculator*

The field calculator allows you to modify or assess spectra and calculate new columns or modify existing ones.

* Open the field calculator |mActionCalculateField| and search for *spectralData* or *spectralMath* in the Spectral Libraries tab.

**SpectralMath** allows you to modify spectral profiles with Python code.

* To use the SpectralMath function, select a field from which the spectral profiles are to be taken, define an expression and the format, e.g. *text* or *binary*, in which the new profile is to be saved.

**SpectralData** returns spectral profile values.

.. list-table::
   :widths: auto
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


.. figure:: /img/SpecLib_FieldCalc.png
    :width: 100%

    ..

**Selecting spectra**
~~~~~~~~~~~~~~~~~~~~~

Spectra can be selected in the attribute table and in the plot window itself. Selected spectra will be highlighted (blue background in the table; thicker line in a different color in the plot window).

* Hold the :kbd:`Shift` key to select multiple spectra.
* A selection can be removed by clicking the |mActionDeselectAll| button.

.. figure:: /img/SpecLib_SelectSpectra.png
    :width: 100%

    ..

* Selected spectra can be removed by using the |mActionDeleteSelected| button.
* Save the collected spectra with the *Save Profiles in Spectral Library* |speclib_save| button.

.. tip:: You can inspect an individual value of a spectrum by holding the :kbd:`Alt` key and clicking some position along the spectrum


You can also select and filter spectra with the common vector filter and selection tools, e.g. select spectra by expression:

.. figure:: /img/SpecLib_SelectByExpr.png
    :width: 100%

    ..

**Show coordinates of collected spectra in map view**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Locations of spectra (if available) can be visualized as a point layer by right-clicking into the map window, and selecting :guilabel:`Add Spectral Library`

.. figure:: /img/SpecLib_AddCoords.png
    :width: 50%

    ..

Visualization settings
----------------------

.. figure:: /img/SpecLib_VisualSettings.png
    :width: 100%

    Overview of the visualization settings in the Spectral Library window

The visualization settings of the spectral library allow you to customize the view according to your needs. You can either choose predefined themes, e.g. dark or bright. Or select the color that you want.

.. figure:: /img/SpecLib_themes.png
    :width: 80%

    ..

* Moreover, activate or deactivate the crosshair and choose a color.
* Once the crosshair ist activated and colored, you can move the crosshair via the control and arrow buttons on your keyboard and save a profile to the speclib with :kbd:`Ctrl + S`.

* The *Current Profiles* section shows you all the spectra that have been collected but do not yet appear in the attribute table. To add the spectra to the attribute table, first activate the |plus_green| button.

**Changing the units**
~~~~~~~~~~~~~~~~~~~~~~

You can change the units of the axis by either right-clicking into the spectral library and navigating to the respective option. Or in the visualization settings |legend| under *General Settings*

.. figure:: /img/SpecLib_units.png
    :width: 80%

    ..

**Colorize spectra by attribute**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spectra can be colorized according to their attributes, e.g. their class name.

* In the *Data Views* section on the left, right click on the spectral library data that we are currently using and select the *Layer Properties*
* Switch to the |symbology| :guilabel:`Symbology` tab and select the :guilabel:`Categorized` renderer at the top
* In the :guilabel:`Column` droplist select the desired column and click :guilabel:`Classify`
* Confirm with :guilabel:`Ok` and close the window.

..  image:: /img/SpecLib_visualization.gif
    :width: 100%

* In the Spectral Library Window activate the visualization settings with the |mActionAddLegend| button.
* Right-click on **Color** and select *Use vector symbol colors* |speclib_usevectorrenderer|.

..  image:: /img/SpecLib_ColorizeSpectra.png
    :width: 100%

Spectral Processing
===================

The idea of spectral processing is to use the spectral profiles obtained from a raster image to test and modify raster algorithms, i.e. the spectral profiles are transferred to a temporary raster image and thus different algorithms can be calculated.

.. figure:: /img/SpecLib_spectralProcessing.png
   :width: 80%

Each column of the spectral library attribute table is derived and translated into meaningful temporary raster image values, regardless of the column type.

.. figure:: /img/SpecLib_TypeMapping.png
   :width: 80%

Text fields (strings) are converted to a one-band classification grid, profile fields are translated to a multi-band grid, and numeric fields are converted to a 1-band grid.

.. figure::/img/SpecLib_SpecProc_transer.png
   :width: 80%

* To use the *Spectral Processing* tool open |profile_processing| and choose the desired algorithm, e.g. **Spectral resampling**.
* Select the input profiles to be translated to the temporary raster layer and specify the outputs. Select an existing field or enter a name to create a new field.

.. figure:: /img/SpecLib_specProDialog.png
   :width: 80%

Importing and Exporting a Spectral Library
==========================================

* To import an existing library use the *Import Spectral Library* |speclib_add| button.
* Possible formats to be imported: *ENVI Spectral Library, Geopackage, ASD Field Spectrometer measurements, Raster Layer.*

.. figure:: /img/SpecLib_ImportFormts.png
   :width: 60%

* You can also import ASD Field Spectrometer measurements and map and modify the imported profiles and attributes accordingly.

.. figure:: /img/SpecLib_addASDProfiles.png
   :width: 60%