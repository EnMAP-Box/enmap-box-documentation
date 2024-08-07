Clustering (kmeans)
===================

Several clustering methods are available in the EnMAP-Box. You can find them in the Processing Toolbox under
:menuselection:`EnMAP-Box --> Clustering`. The usual way to apply these methods is to use a :guilabel:`Fit ...`
algorithm first and then apply it to an image with :guilabel:`Predict (unsupervised) classification layer`.

This recipe demonstrates the basic workflow of applying clusterers
using K-Means clustering (:ref:`Fit KMeans`) and the :ref:`example data <example_data>`.

.. seealso:: You can find all the available clustering algorithms :ref:`here <Clustering>`.

#. Open the test dataset
#. In the processing toolbox go to :menuselection:`EnMAP-Box --> Clustering --> Fit KMeans`

   * Specify :file:`enmap_potsdam.tif` under :guilabel:`Raster`
   * Under :guilabel:`Output Clusterer` specify an output file path and click :guilabel:`Run`

#. Now open :menuselection:`EnMAP-Box --> Clustering --> Predict (unsupervised) classification layer`

   * Select :file:`enmap_potsdam.tif` as input :guilabel:`Raster`
   * Under :guilabel:`Clusterer` click :guilabel:`...` and select the output :file:`.pkl` file from the Fit KMeans algorithm
   * Specify an output filepath for the transformed raster under :guilabel:`Clustering` and click :guilabel:`Run`

   .. figure:: /img/example_kmeans.png

      EnMAP true color image (left) and kmeans cluster result with 8 clusters (right)

.. tip::
   8 clusters is the default of the kmeans algorithm here, if you want to change the number of clusters, run the
   Fit Kmeans algorithm with a fewer number, by altering the ``KMeans()`` function in the :guilabel:`Code` window to ``KMeans(n_clusters=4)``.
   This will reduce the amount of clusters to 4.