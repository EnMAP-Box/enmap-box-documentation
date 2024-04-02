Transformation (PCA)
====================

Several transformation methods are available in the EnMAP-Box. You can find them in the Processing Toolbox under
:menuselection:`EnMAP-Box --> Transformation`. The usual way to apply these methods is to use a :guilabel:`Fit ...`
algorithm first and then apply it to an image with :guilabel:`Transform raster layer`.

This recipe demonstrates the basic workflow of applying transformations
using a principle component analysis (:ref:`Fit PCA`) and the :ref:`test dataset <test_dataset>`.

.. seealso:: You can find all the available transformation algorithms :ref:`here <Transformation>`.


#. Open the test dataset
#. In the processing toolbox go to :menuselection:`EnMAP-Box --> Transformation --> Fit PCA`

   * Specify :file:`enmap_potsdam.tif` under :guilabel:`Raster`
   * Under :guilabel:`Output Transformer` specify an output file path and click :guilabel:`Run`

#. Now open :menuselection:`EnMAP-Box --> Transformation --> Transform raster layer`

   * Select :file:`enmap_potsdam.tif` as input :guilabel:`Raster`
   * Under :guilabel:`Transformer` click :guilabel:`...` and select the output :file:`.pkl` file from the Fit PCA algorithm
   * Specify an output filepath for the transformed raster under :guilabel:`Transformation` and click :guilabel:`Run`

   .. figure:: /img/example_pca.png
      :width: 100%

      Results of a PCA transformation: input image on the upper left, RGB representation of the first 3 components on the
      upper right and singleband pseudocolor visualisation of the same components on the bottom.

