.. include:: /icon_links.rst

.. |reset_plot| image:: ../../img/pyqtgraph_reset.png
   :width: 15px

.. _tools:

Tools
*****

Add Product
===========

The :guilabel:`Add Product` menu allows to import satellite products into the EnMAP-Box.
It is also possible to drag&drop products from the file explorer (e.g. Windows Explorer).
The different import algorithms assign proper metadata like wavelength, band names and data offset and scale, resulting in analysis ready raster data.

Usage
    1. Choose the product type from the :guilabel:`Project > Add Product` menu.

    .. figure:: ./img/AddProduct.png
       :align: center

    2. Select the associated (metadata) file.

    .. figure:: ./img/AddProduct_2.png
       :align: center



Live demonstration
    ..  youtube:: G7UE-DIhXi8
        :width: 100%
        :privacy_mode:

Add Web Map Services (WMS)
==========================

The :guilabel:`Add Web Map Services (WMS)` menu allows to add predefined WMS to the :guilabel:`Data Sources` panel:

Usage
    1. Choose a WMS from the :guilabel:`Project > Add Web Map Services (WMS)` menu.

    .. figure:: ./img/AddWebMapServices.png
       :align: center

    2. Add the WMS to a Map View.

Live demonstration
    ..  youtube:: SRJPh4bxcnw
        :width: 100%
        :privacy_mode:

Band Statistics
===============

The :guilabel:`Band Statistics` tool reports band histograms and basic statistics like min, max, mean and standard deviation.

Usage
    1. Start the tool from the :guilabel:`Tools > Band Statistics` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer`.

    3. Add some bands.

    3. Interactively explore the map.

    .. figure:: ./img/BandStatistics.png
       :align: center

Live demonstration
    ..  youtube:: tS2B9EsHutY
        :width: 100%
        :privacy_mode:

Bivariate Color Raster Renderer
===============================

The :guilabel:`Bivariate Color Raster Renderer` allows to visualize two bands using a 2d color ramp.
Find a mapping example here: https://www.joshuastevens.net/cartography/make-a-bivariate-choropleth-map/

Usage
    1. Start the tool from the :guilabel:`Tools > Bivariate Color Raster Renderer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer`.

    3. Select two bands.

    4. Select or define a color plane.

    5. Interactively explore the map.

    .. figure:: ./img/BivariateColorRasterRenderer.png
       :align: center

Live demonstration
    ..  youtube:: TW3hrWKLpbs
        :width: 100%
        :privacy_mode:

Class Fraction/Probability Renderer and Statistics
==================================================

The :guilabel:`Class Fraction/Probability Renderer and Statistics` tool allows to visualize arbitrary many fraction/probability bands
at the same time, using a weighted average of the original class colors, where the weights are given by the
class fractions/probabilities.

Usage
    1. Start the tool from the :guilabel:`Tools > Class Fraction/Probability Renderer and Statistics` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`class fraction layer` or a :term:`class probability layer`.

    3. Select approriate class colors or paste a matching style from another layer.

    4. Interactively explore the map.

    .. figure:: ./img/ClassFractionRenderer.png
       :align: center

    Note that the visibility of individual classes can be turned on and off.

Live demonstration
    ..  youtube:: fflhmRl_Npw
        :width: 100%
        :privacy_mode:

Classification Statistics
=========================

The :guilabel:`Classification Statistics` tool reports class histograms and area covered in percentage, pixel and map units.

Usage
    1. Start the tool from the :guilabel:`Tools > Class Fraction/Probability Renderer and Statistics` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`categorized raster layer`.

    3. Interactively explore the map.

    .. figure:: ./img/ClassificationStatistics.png
       :align: center

Live demonstration
    ..  youtube:: Go7tRzwKPvs
        :width: 100%
        :privacy_mode:

CMYK Color Raster Renderer
==========================

The :guilabel:`CMYK Color Raster Renderer` allows to visualize 4 bands using the CMYK (Cyan, Magenta, Yellow, and Key/Black)
color model. Find a mapping example here: https://adventuresinmapping.com/2018/10/31/cmyk-vice/

Usage
    1. Start the tool from the :guilabel:`Tools > CMYK Color Raster Renderer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer`.

    3. Select CMYK bands.

    4. Interactively explore the map.

    .. figure:: ./img/CMYKColorRasterRenderer.png
       :align: center

Live demonstration
    ..  youtube:: aVy9WXM3Q84
        :width: 100%
        :privacy_mode:

Color Space Explorer
====================

The :guilabel:`Color Space Explorer` allows
a) to select random and predefined RBG band combinations, and
b) to animate RGB bands.

Usage
    1. Start the tool from the :guilabel:`Tools > Color Space Explorer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer`.

    3. Select RGB bands:

        a. manually

        b. randomly

        c. from predefined list of RGB band combinations

    4. Animate bands using the :guilabel:`Color Space Gradient Step Size` settings.

    5. Interactively explore the map.

GUI
    .. figure:: ./img/ColorSpaceExplorer.png
       :align: center

Live demonstration
    ..  youtube:: e5SLW1pB06A
        :width: 100%
        :privacy_mode:


Decorrelation Stretch Renderer
==============================

The :guilabel:`Decorrelation Stretch Renderer` allows to visualize 3 band. It removes the high correlation commonly found in
optical bands to produce a more colorful color composite image.

Usage
    1. Start the tool from the :guilabel:`Tools > Decorrelation Stretch Renderer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer`.

    3. Select RGB bands.

    4. Interactively explore the map.

GUI
    .. figure:: ./img/DecorrelationStretchRenderer.png
       :align: center

Enhanced Multiband Color Renderer
=================================

The :guilabel:`Ehanced Multiband Color Renderer` allows to visualize arbitrary many bands at the same time using individual
color canons for each band.

Usage
    1. Start the tool from the :guilabel:`Tools > Enhanced Multiband Color Renderer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a color for each band.

    3. Interactively explore the map.

GUI
    .. figure:: ./img/EnhancedMultibandColorRenderer.png
       :align: center

HSV Color Raster Renderer
=========================

The :guilabel:`HSV Color Raster Renderer` allows to visualize 3 bands using the HSV (Hue, Saturation, Value/Black) color model.
Find a mapping example here: https://landmonitoring.earth/portal/ ; select Maps > Global Landcover Dynamics 2016-2020

Usage
    1. Start the tool from the :guilabel:`Tools > HSV Color Raster Renderer` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select HSV bands.

    3. Interactively explore the map.

GUI
    .. figure:: ./img/HSVColorRasterRenderer.png
       :align: center

.. todo::

    Find a good dataset, that is comparable to the *Global Landcover Dynamics 2016-2020* from GeoVille.


Image Cube
==========

The :guilabel:`Image Cube` tool visualizes a raster image in an interactive 3D view:

.. image:: /img/imagecube_animation.gif

1.  Select the raster image.

2.  Specify the:

    * **Top Plane** renderer. It can be any raster renderer known from QIGS, e.g. a Multiband
        color renderer that shows the true color bands

    * **Cube & Slice** renderer. This must be a render that uses a single band only, e.g. a
      *Singleband grey* or *Pseudocolor renderer*. It will colorize the band-related pixel values
      of the 3D image cube and planes relating to the X, Y or Z slice.

3.  Press **Load Data** to (re)load and render the raster image values.

.. image:: /img/imagecube_gui.png


The 3D scene contains the following elements:

* Top Plane - a raster layer for spatial orientation
* Image Cube - a volumetric representation of the raster image, showing the raster bands on the z axis
* X Slice - a slice along the raster's X / column / sample dimension
* Y Slice - a slice along the raster's Y / row / line dimension
* Z Slice - a slice along the raster's Z / band dimension
* Box (Image) - a 3D bounding box along the maximum image extent
* Box (Subset) - a 3D bounding box to show the extent of the spatial subset that migh be used to focus on specific
  image areas

.. image:: /img/imagecube_gui_slices.png

Metadata Viewer
===============

The :guilabel:`Metadata Viewer` allows to view and edit `GDAL metadata <https://gdal.org/doxygen/classGDALPamDataset.html>`_ of a raster source.

Usage
    1. Start the tool from the :guilabel:`Tools > Metadata Viewer` menu.

    2. Select a raster source.

    3. View and edit metadata.

GUI
    .. figure:: ./img/MetadataViewer.png
       :align: center

Multisource Multiband Color Raster Renderer
===========================================

.. todo:: WriteTheDocs (use FORCE TSI stacks with TCB/G/W)

Raster Layer Styling
====================

The :guilabel:`Raster Layer Styling` panel allows to quickly select a RGB, Gray or Pseudocolor visualizations.

Usage
    1. Show the panel via the :guilabel:`View > Panels > Raster Layer Styling` menu or click |symbology| :sup:`Open Raster Layer Styling panel` in the :guilabel:`Data Views` panel.

    2. Select a raster source.

    3. View and edit metadata.

GUI
    .. figure:: ./img/MetadataViewer.png
       :align: center

Live demonstration
    ..  youtube:: ImO8BzHNjlk
        :width: 100%
        :privacy_mode:

It also supports the linking of the style between multiple  :term:`raster layer`.

GUI
    .. figure:: ./img/RasterLayerStyling_2.png
       :align: center

Live demonstration
    ..  youtube:: HJSNhG7vKKg
        :width: 100%
        :privacy_mode:

Raster Source Band Properties Editor
====================================

The :guilabel:`Raster Source Band Properties Editor` allows to view and edit band properties of GDAL raster sources,
with special support for ENVI metadata.

Usage
    1. Start the tool from the :guilabel:`Tools > Raster Source Band Properties Editor` menu.

    2. Select a raster source.

    3. View and edit metadata.

GUI
    .. figure:: ./img/RasterSourceBandPropertiesEditor.png
       :align: center

Reclassify
==========

The :guilabel:`Reclassify` tool is a convenient graphical user interface for reclassifying classification rasters.

Specify the file you want to reclassify under :guilabel:`Input File`. Either use the dropdown menu to select one of the
layers which are already loaded or use the |mActionAddRasterLayer| button to open the file selection dialog.

Under :guilabel:`Output Classification` you can specify the classification scheme of the output classification which
will be created.

* You can import schemes from existing rasters or text files by clicking the |plus_green| button.
* Use the |classinfo_add| button to manually add classes.
* To remove entries select the respective rows and click the |classinfo_remove| button.
* So save a classification scheme select the desired classes (or use :kbd:`Crtl + A` to select all) and click on the
  |mActionFileSaveAs| button.
* Likewise, you can copy and paste classes by selecting them and clicking the |mActionEditCopy| :sup:`Copy Classes`
  |mActionEditPaste| :sup:`Paste Classes` buttons.

.. image:: /img/reclassifytool1.png

* The table is sorted by the **Label** field in ascending order. The value in **Label** will become the pixel value
  of this class and can not be altered.
* Double-click into the **Name** field in order to edit the class name.
* Double-click into the **Color** field to pick a color.

Under :guilabel:`Class Mapping` you can reassign the old classes (**From**) to values of the new classification scheme (**To**)

.. image:: /img/reclassifytool2.png

Specify the output path for the reclassified image under :guilabel:`Output File`

Click :guilabel:`OK` to run the tool.

Scatter Plot
============

The :guilabel:`Scatter Plot` allows to plot two raster bands, or a raster band and a vector field against each other.
The visualization of both, denstity and scatter is supported.

Plotting Raster Band vs. Raster Band
------------------------------------

When plotting raster data against each other, we usually want to display the bin counts as colorized density.

Usage
    1. Start the tool from the :guilabel:`Tools > Scatter Plot` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select two :term:`raster layer` bands used for x and y values.

    3. Select `Density` option for :guilabel:`Coloring` and choose a color ramp.

    4. Interactively explore the map.

GUI
    .. figure:: ./img/ScatterPlot.png
       :align: center

Live demonstration:
    ..  youtube:: bMfklHoEqJc
        :width: 100%
        :privacy_mode:

Plotting Raster Band vs. Vector Field
-------------------------------------

The tool can also be used to plot raster data versus vector attribute values, e.g. for accuracy assessment of quantitative maps.

Usage
    1. Start the tool from the :guilabel:`Tools > Scatter Plot` menu or from the layer context menu inside the :guilabel:`Data Views` panel.

    2. Select a :term:`raster layer` band used as x values, and :term:`vector layer` field used as y values.

    3. Select `Scatter` option for :guilabel:`Coloring`, choose a color and a symbol.

    4. Active :guilabel:`1:1 line` and :guilabel:`Fitted line` in the :guilabel:`Analytics` section.

GUI
    .. figure:: ./img/ScatterPlot_2.png
       :align: center

Virtual Raster Builder
======================

See https://virtual-raster-builder.readthedocs.io/en/latest/
