.. include:: /icon_links.rst

Map Algebra with ImageMath
==========================

You can open the ImageMath raster calculator under :menuselection:`Applications --> ImageMath`

Calculate NDVI
~~~~~~~~~~~~~~

* Make sure to open the testdatasets for this example
* Specify the input and output parameters according to the screenshot below (you can of course alter the names, but make
  sure to also adapt them in the script)

  .. image:: ../../img/im_input_ndvi.png

* Enter this code in the editor on the right side. You do not need to alter :guilabel:`Output Grid` and :guilabel:`Processing` for now.

  .. code-block:: python

     # select the red band
     red = enmap[38]
     # select the nir band
     nir = enmap[64]
     # calculate ndvi
     ndvi = (nir-red)/(nir+red)

* Click the run button |action|. The result should be listed in the :guilabel:`Data Sources` panel.

....

Mask raster with vector
~~~~~~~~~~~~~~~~~~~~~~~

* Make sure to open the testdatasets for this example
* Select :file:`enmap_berlin.bsq` under :guilabel:`Inputs` and name it ``enmap``. Further select :file:`landcover_berlin_polygon.shp` and name
  it ``mask``.
* Under :guilabel:`Outputs` specify output path and file and name it ``result``


* Enter this code in the editor

  .. code-block:: python

     result = enmap
     # set all cells not covered by mask to nodata
     result[:, mask[0] == 0] = noDataValue(enmap)
     # specify nodata value
     setNoDataValue(result, noDataValue(enmap))
     # copy metadata to result raster
     setMetadata(result, metadata(enmap))

* Click the run button |action|. The result should be listed in the :guilabel:`Data Sources` panel.




