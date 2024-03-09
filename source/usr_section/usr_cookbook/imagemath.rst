.. include:: /icon_links.rst

Map Algebra with ImageMath
==========================

You can open the ImageMath raster calculator under :menuselection:`Raster analysis --> Raster math`

Calculate NDVI
~~~~~~~~~~~~~~

* Make sure to open the testdatasets for this example
* Under :guilabel:`Code Snippets --> Indices` select NDVI. Select :file:`enmap_potsdam.bsq` as your input.

  .. image:: ../../img/im_input_ndvi.png

* Alternatively, enter this code directly in the editor. Make sure to alter the names according to your raster. You do not need to alter :guilabel:`Output Grid` and :guilabel:`Processing` for now.

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
* Select :file:`enmap_potsdam.bsq` under :guilabel:`Inputs` and name it ``enmap``. Further select :file:`landcover_potsdam_polygon.gpkg` and name
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




