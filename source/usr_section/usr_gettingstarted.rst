.. include:: /icon_links.rst

.. _getting_started:

###############
Getting Started
###############

.. admonition:: Info

    This section is aimed at users with no previous EnMAP-Box experience. You will get a brief introduction into the
    main functionalities:

    * Getting to know the Graphical User Interface
    * Use an EnMAP-Box Application (Classification Workflow)
    * Use a Processing Algorithm


Primer
######

The EnMAP-Box can be divided into several major components. The :ref:`Graphical User Interface (GUI) <gui>`
provides main access to all features and lets you manage and visualize raster and vector data as well as spectral libraries.
From here you can access further :ref:`Tools <tools>` and :ref:`Applications <applications>`, which can be regarded as additional plugins
that add specific functionalities such as plotting, metadata editing or raster algebra. Furthermore, the EnMAP-Box extents the QGIS
Processing Toolbox with a comprehensive collection of various :ref:`Processing Algorithms` for (raster) data manipulation. 'Underneath'
all this is the :ref:`EnMAP-Box API, HUB-Workflow API and HUB-Datacube API <dev_cookbook>`, which are high-level application programming interfaces that
allow more advanced users to operate EnMAP-Box functionalities directly from code or to build their own applications on top.

.. figure:: ../img/enmapbox_components.png



Launching the EnMAP-Box
#######################

Once you successfully :ref:`installed the EnMAP-Box <usr_installation>`, you can access the plugin via the |enmapbox| icon
in the QGIS toolbar. Furthermore, the EnMAP-Box :ref:`Processing Algorithms` should also appear in the QGIS Processing Toolbox.

.. figure:: ../img/manual_gui.png

    The Graphical User Interface (GUI) of the EnMAP-Box on first open

.. tip:: Have a look at the :ref:`User Manual <gui>` for a detailed description of the GUI.


Loading Testdata
################

* Go to :menuselection:`Project --> Load Example Data` to load example datasets into you project (on first open, you will be asked whether
  to download the dataset, confirm with :guilabel:`OK`). The following datasets
  will be added (now they are listed in the :guilabel:`Data Sources` window):

  * :file:`enmap_berlin.bsq`
  * :file:`hires_berlin.bsq`
  * :file:`landcover_berlin_point.gpkg`
  * :file:`landcover_berlin_polygon.gpkg`
  * :file:`library_berlin.sli`

.. tip::

   Have a look at the section :ref:`Test dataset <test_dataset>` for further information on the dataset. In this section we will
   mainly work with :file:`enmap_berlin.bsq` and :file:`landcover_berlin_point.gpkg`


First Steps in the GUI
######################

By default the example data is loaded into a single Map View. Let's rearrange those for better visualisation and in order
to get to know the GUI functionalities:

* Click the |viewlist_mapdock| :superscript:`Open a map window` button to add a second map view. The window appears
  below the first map window.
* We want to arrange the windows so that they are next to each other (horizontally). Click and hold on the blue area
  of :guilabel:`Map #2` and drag it to the right of :guilabel:`Map #1` (see figure below). The translucent blue rectangle indicates where the
  map window will be docked once you stop holding the left mouse button.

  .. image:: ../img/mapviewshift.png

* Now, in the :guilabel:`Data Views` window, expand the :guilabel:`Map #1` list, so that you can see the individual layers. Select
  :file:`hires_berlin.bsq` and drag the layer into :guilabel:`Map #2` (you can drag them directly into the map views or the respective menu item under :guilabel:`Data Views`).
  You can remove :file:`library_berlin.sli` and :file:`landcover_berlin_polygon.gpkg`, since they are not needed here. Right-click on the layer
  in the Data Views panel and select :guilabel:`Remove Layer`.
* In the next step we link both map views, so that zoom and center are synchronized between both. Go to :menuselection:`View --> Set Map Linking` and
  select |link_all_mapscale_center| :superscript:`Link map scale and center`.
* Move the map (using |mActionPan| or holding mouse wheel) and see how both map views are synchronized.


Use an Application
##################

In this section we will use the EnMAP-Box application **Classification Workflow** to classify the :file:`enmap_berlin.bsq`
image using a point vector dataset with the classes *impervious, low vegetation, tree, soil, water* and a random forest classifier.

* Go to :menuselection:`Applications --> Classification Workflow (Classic)` to open the Classification Workflow application.
* In the :guilabel:`Type` dropdown menu select ``Raster / Vector Classification``.
* Choose :file:`enmap_berlin.bsq` as :guilabel:`Raster` and :file:`landcover_berlin_point.gpkg` as :guilabel:`Reference`.
  Now the class names and colors become visible in the :guilabel:`Sampling` submenu.

  .. image:: ../img/classwf1.png

* Here you can alter the class colors and the class names or change the size of your sample. But for this tutorial use
  the default settings (sample size at 100%).

  .. tip::

     Find more information on the Classification Workflow application in the :ref:`User Manual <Classification Workflow>`.

* As :guilabel:`Classifier` choose RandomForestClassifier (which is the default setting).
* Under :guilabel:`Mapping` you have to specify the raster which will be classified. We will choose the same raster we took the samples from,
  so select :file:`enmap_berlin.bsq` as :guilabel:`Raster`.
* Make sure to check |cb1| the :guilabel:`Classification` output. Specify an output path and filename by pressing :guilabel:`...` or
  use the default, which will save the output to a temporary location.
* Also select |cb1| to perform a :guilabel:`Cross-validation with n-folds`. You can leave the number of folds at 3. Specify
  output path for the HTML report or use default (temporary directory).

  .. image:: ../img/classwf2.png

* Click the run button |action| to start the classification.
* Once the process has finished, the classification image will be listed in the :guilabel:`Data Sources` panel (if not, open it again via |add_datasource|).
  Also, the HTML report of the accuracy assessment will open automatically in the default web browser.

  .. figure:: ../img/screenshot_aareport.png

     Screenshot of the Classification Performance HTML report

* Now visualize the classification result side-by-side with the initial image. Therefore, right-click into :guilabel:`Map #2` and
  select :menuselection:`--> Clear`. Drag the classification image from the :guilabel:`Data Sources` panel into :guilabel:`Map #2`

  .. figure:: ../img/screenshot_class_result.png

     Screenshot of the Map Views: EnMAP image on the left and classification result on the right

* In the :guilabel:`Data Views` panel, right-click on the classification layer and select :guilabel:`Classification Statistics`.
  This will show you an interactive plot with the different class counts

  .. image:: /img/classification_statistics.png


Use a Processing Algorithm
##########################

In this section we will use a processing algorithm from the EnMAP-Box algorithm provider. More precise, we are converting a
polygon dataset holding information on different landcover types into a classification raster, i.e., we are going to
rasterize the vector dataset.

* First of all, make sure the :ref:`Processing Toolbox <processing_toolbox>` window is opened. If not,
  activate it via :menuselection:`View --> Panels --> Processing Toolbox`
* Open the :menuselection:`Rasterize categorized vector layer` algorithm under :menuselection:`EnMAP-Box --> Raster Creation`
* Use the following settings:

  * :guilabel:`Categorized vector layer`: :file:`landcover_berlin_polygon.gpkg`
  * :guilabel:`Grid`: :file:`enmap_berlin.bsq`

* Specify an output filepath under :guilabel:`Output Classification` and click :guilabel:`Run`

.. figure:: /img/example_rasterize_classification.png
   :width: 100%

   Result of the Classification from Vector algorithm (right) and the input grid (left) and polygon dataset (middle)

Use the Spectral Library
########################

In this section, we will use the spectral library to characterize and compare spectra of different surfaces.
In the following, the :file:`enmap_berlin.bsq` is used to explain how to collect spectra and edit their properties.

* Open the spectral library window via :menuselection:`View --> Add Spectral Library Window`
* Now you should see an empty window where all spectra can now be collected.

  .. image:: ../img/SpectralLibrary.png

* If not activated yet, enable the |profile| button in the menu bar and open a raster you want to collect spectra
  from in a Map Window.
* Now you can generate spectra from the image by using the left mouse button and clicking in the opened image.
* To display multiple spectra at the same time in the same spectral library, activate the *Add profiles automatically* |profile_add_auto|
  button in the |plus_green| drop-down list.

  .. image:: ../img/AddProfiles.png

**Add information to the attribute table:**

* You can manage your spectra and add information, e.g. class name or description of the property.
* Open the Attribute table view by clicking the |attributes| symbol, then enable the **Editing mode** by activating the |mActionToggleEditing|
* Add a new field via |mActionNewAttribute|

  .. figure:: ../img/Speclib_addNewField.png

     Example: Add a new text field (maximum 100 characters)

* After the new column is added, you can add information by double-clicking it.
* To delete a column, use the :guilabel:`Delete field button` |mActionDeleteAttribute|