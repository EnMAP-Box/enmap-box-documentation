.. _getting_started:

###############
Getting Started
###############

EnMAP-Box Introduction and basic features:

.. raw:: html

   <div style="text-align: center;">
   <iframe width="100%" height="380" src="https://www.youtube-nocookie.com/embed/31FQ5zXl2Rw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   </div>

|

1. Launching the EnMAP-Box
##########################

Once you successfully :ref:`installed the EnMAP-Box <usr_installation>`, you can access the plugin via the |enmapbox| icon
in the QGIS toolbar or via :menuselection:`Raster --> EnMAP-Box` from the menubar.
Furthermore, the EnMAP-Box :ref:`Processing Algorithms` provider is available in the Processing Toolbox.

    .. figure:: ../img/manual_gui.png
        :width: 100%
        :align: center

        The Graphical User Interface (GUI) of the EnMAP-Box on first open

.. tip:: Have a look at the :ref:`User Manual <gui>` for a detailed description of the GUI.


2. Loading data
###############

You can load an :ref:`example dataset <example_data>` into your project by selecting :menuselection:`Project --> Add Example Data` in the menu bar.
On a fresh installation you will be asked to download the dataset, confirm with :guilabel:`OK`.
The data will be added automatically into a single map view and will be listed in the :guilabel:`Data Sources` panel as well.


3. First steps in the GUI
#########################

By default the example data is loaded into a single map view. Let's rearrange those for better visualisation and in order
to get to know the GUI functionalities:

1. Click the |viewlist_mapdock| :sup:`Open a map view` button to add a second map view. This view will appear below the
   first map view (:guilabel:`Map #1`).
2. We want to arrange the windows so that they are next to each other (horizontally): Click and hold on to the blue area of
   :guilabel:`Map #2` and drag it to the right of :guilabel:`Map #1` (see figure below). The translucent blue rectangle
   indicates where the map window will be docked once you stop holding the left mouse button.

    .. figure:: ../img/mapviewshift.png
       :align: center
       :width: 800

3. In the :guilabel:`Map #1` list in the :guilabel:`Data Views` panel, select :file:`aerial_potsdam.tif` and drag the
   layer into :guilabel:`Map #2` (you can drag them directly into the map view or the respective menu item under :guilabel:`Data Views`).
4. In the next step we link both map views, so that zoom and center are synchronized between both:
   Click the |link_basic| button or go to :menuselection:`View --> Set Map Linking` and select
   |link_all_mapscale_center| :sup:`Link map scale and center`.
5. Move the map (using |mActionPan| or holding the mouse wheel |mouse_wheel|) and notice how both map views are synchronized now.

Now we want to change the RGB representation of the :file:`enmap_potsdam.tif` image:

6. In the :guilabel:`Data Views` panel click the |symbology| :sup:`Open Raster Layer Styling` button, which will open
   a new panel. Here you can quickly change the renderer (e.g., singleband gray, RGB) and the band(s) visualized. You can
   do so manually using the slider or by selecting the buttons with predefined wavelength regions based on Sentinel-2 (e.g.
   :guilabel:`G` = *Green*, :guilabel:`N` = *Near infrared*).
   The raster layer needs to have :term:`wavelength` information for the latter to work!
7. In the RGB tab, look for :guilabel:`Predefined` and click on the dropdown menu |combo|. You will find several band
   combination presets. Select `Colour infrared`.

  .. figure:: /img/rasterlayerstyling.png
     :align: center
     :width: 100%

     Raster Layer Styling panel with selected Color infrared preset

8. Try out other renderers and band combinations!

.. tip::

   Once you selected/activated the slider (i.e., clicked |mouse_leftclick| on it) you can use the arrow keys :kbd:`←`/:kbd:`→` to
   switch back and forth between bands!

4. Use a Processing Algorithm
#############################

In this section we will use a processing algorithm from the EnMAP-Box algorithm provider. The EnMAP-Box adds more than
180 Processing Algorithms to the QGIS processing framework. Their scope ranges from general tasks, e.g. file type
conversions or data import to specific applications like machine learning.
In this example we are converting a polygon dataset with information on different landcover types into a
classification raster, i.e., we are going to rasterize the vector dataset.

1. First of all, make sure the :ref:`Processing Toolbox <processing_toolbox>` window is opened. If not, activate it via
   :menuselection:`View --> Panels --> Processing Toolbox`
2. Open the :guilabel:`Rasterize categorized vector layer` algorithm under :menuselection:`EnMAP-Box --> Vector conversion`
3. Use the following settings:

  * :guilabel:`Categorized vector layer`: :file:`landcover_potsdam_polygon.gpkg`
  * :guilabel:`Grid`: :file:`enmap_potsdam.tif`

4. Specify an output filepath under :guilabel:`Output Classification` and click :guilabel:`Run`.

    .. figure:: /img/example_rasterize_classification.png
       :align: center
       :width: 100%

       Result of the Classification from Vector algorithm (right) and the input grid (left) and polygon dataset (middle)


5. What's next?
###############

* `Introduction to spectral libraries (video) <https://www.youtube.com/watch?v=qVoi0CoJheI>`_
* :ref:`Download EnMAP data <data_access>`
* :ref:`Classification <classification_workflow_app>`

.. seealso::

   If you face issues or have questions, head over to the `GitHub Discussions page <https://github.com/EnMAP-Box/enmap-box/discussions>`_
   and start a new discussion.


.. AUTOGENERATED SUBSTITUTIONS - DO NOT EDIT PAST THIS LINE

.. |combo| image:: /img/icons/combo.png
   :width: 28px
.. |enmapbox| image:: /img/icons/enmapbox.svg
   :width: 28px
.. |link_all_mapscale_center| image:: /img/icons/link_all_mapscale_center.svg
   :width: 28px
.. |link_basic| image:: /img/icons/link_basic.svg
   :width: 28px
.. |mActionPan| image:: /img/icons/mActionPan.svg
   :width: 28px
.. |mouse_leftclick| image:: /img/icons/mouse_leftclick.svg
   :width: 28px
.. |mouse_wheel| image:: /img/icons/mouse_wheel.svg
   :width: 28px
.. |symbology| image:: /img/icons/symbology.svg
   :width: 28px
.. |viewlist_mapdock| image:: /img/icons/viewlist_mapdock.svg
   :width: 28px
