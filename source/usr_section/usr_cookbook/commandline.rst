Command line (qgis_process)
===========================

Similar to QGIS processing algorithms you can also run EnMAP-Box algorithms directly from the command line using the
`QGIS Processing Executor <https://docs.qgis.org/3.28/en/docs/user_manual/processing/standalone.html#using-processing-from-the-command-line>`_ ,
i.e., the ``qgis_process`` command. This can be especially useful to automate repetitive tasks (batch processing) and/or
when deploying EnMAP-Box workflows on server environments.

.. note:: Depending on your installation the command might also be named ``qgis_process-qgis`` or ``qgis_process-qgis-ltr``

|

Basics
------

On systems without window manager (e.g. servers) set the environment variable ``QT_QPA_PLATFORM`` before using ``qgis_process``

.. code-block:: bash

   export QT_QPA_PLATFORM=offscreen

Make sure to activate the EnMAP-Box plugin first via

.. code-block:: bash

   qgis_process plugins enable enmapboxplugin

To show all available processing algorithms, run

.. code-block:: bash

   qgis_process list

For information on a specific algorithm and its parameters, use the ``help`` command with the corresponding algorithm name, e.g.:

.. code-block:: bash

   qgis_process help enmapbox:ImportEnmapL2AProduct

Finally, to run an algorithm, use the ``run`` command followed by the algorithm name and its parameters, e.g.:

.. code-block:: bash

   qgis_process run enmapbox:ImportEnmapL2AProduct --file="ENMAP01-____L2A-DT0000001280_20220627T104500Z_001_V010301_20230517T020623Z-METADATA.XML" --outputEnmapL2ARaster="output.vrt"

|

Example 1: Bulk import of L2A scenes
------------------------------------

In this example we import multiple EnMAP L2A scenes (all located inside a folder ``$DATA_DIR``) and save them as a GeoTiff to another folder ``$OUTPUT_DIR``.
The ``ImportEnmapL2AProduct`` algorithm only outputs virtual rasters (:file:`.vrt`), so we add the ``SaveRasterLayerAs`` algorithm as a second step and
handle intermediate outputs as temporary data.

.. code-block:: bash

   DATA_DIR="somepath/data"
   OUTPUT_DIR="somepath/output"

   for f in $(find $DATA_DIR -name "*METADATA.XML")
     do
     OUTPUT=$(basename $f | sed "s/\-METADATA.XML/.tif/")
     TMP_DIR=$(mktemp -d)

     qgis_process run enmapbox:ImportEnmapL2AProduct \
       --file=$f \
       --outputEnmapL2ARaster="$TMP_DIR/temp.vrt"

     qgis_process run enmapbox:SaveRasterLayerAs \
       --raster="$TMP_DIR/temp.vrt" \
       --creationProfile="GTiff INTERLEAVE=BAND COMPRESS=LZW PREDICTOR=2 BIGTIFF=YES" \
       --outputRaster="$OUTPUT_DIR/$OUTPUT"
     done


Or run in parallel using GNU ``parallel``:

.. code-block:: bash

   DATA_DIR="somepath/data"
   OUTPUT_DIR="somepath/output"

   function import_l2a {

     OUTPUT=$(basename $1 | sed "s/\-METADATA.XML/.tif/")
     TMP_DIR=$(mktemp -d)

     qgis_process run enmapbox:ImportEnmapL2AProduct \
       --file=$1 \
       --outputEnmapL2ARaster="$TMP_DIR/temp.vrt"

     qgis_process run enmapbox:SaveRasterLayerAs \
       --raster="$TMP_DIR/temp.vrt" \
       --creationProfile="GTiff INTERLEAVE=BAND COMPRESS=LZW PREDICTOR=2 BIGTIFF=YES" \
       --outputRaster="$2/$OUTPUT"
   }

   export -f import_l2a
   find $DATA_DIR -name "*METADATA.XML" | parallel -j4 import_l2a {} $OUTPUT_DIR

.. tip:: Instead of ``enmapbox:SaveRasterLayerAs`` you could also use the more elaborate ``enmapbox:TranslateRasterLayer``
         where you can, among other things, make spatial and/or spectral subsets of the input raster.

|

Example 2: Classification
-------------------------

The EnMAP-Box image classification process involves three main steps:

1. Creating a classification dataset using a feature raster and a layer which holds information on classes (in this example a point vector layer)
2. This dataset with the pixel values (features) and the categories from the vector layer (target) is then used to
   train a machine learning model
3. The resulting model is then applied to an image for classification

Using ``qgis_process``, a typical classification workflow could look like this:

.. code-block:: bash

   DATA_DIR="$HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/exampledata"
   OUTPUT_DIR="somepath/output"

   qgis_process run enmapbox:CreateClassificationDatasetFromCategorizedVectorLayerAndFeatureRaster \
     --featureRaster="$DATA_DIR/enmap_potsdam.tif" \
     --excludeBadBands=1 \
     --categorizedVector="$DATA_DIR/landcover_potsdam_point.gpkg" \
     --categoryField="level_2" \
     --outputClassificationDataset="$OUTPUT_DIR/dataset.pkl"

   qgis_process run enmapbox:FitRandomforestclassifier \
     --dataset="$OUTPUT_DIR/dataset.pkl" \
     --classifier="from sklearn.ensemble import RandomForestClassifier; classifier = RandomForestClassifier(n_estimators=100, oob_score=True)" \
     --outputClassifier="$OUTPUT_DIR/rfc_fit.pkl"

   qgis_process run enmapbox:PredictClassificationLayer \
     --raster="$DATA_DIR/enmap_potsdam.tif" \
     --classifier="$OUTPUT_DIR/rfc_fit.pkl" \
     --matchByName=1 \
     --outputClassification="$OUTPUT_DIR/classification.tif"

.. seealso::

   * To change the visualisation of the :term:`output categories<categorized raster layer>` you have the option to alter the
     QML file using the ``CreateDefaultPalettedRasterRenderer`` algorithm. Run
     ``qgis_process help enmapbox:CreateDefaultPalettedRasterRenderer`` for more information.
   * For accuracy assessment, have a look at ``enmapbox:ClassificationLayerAccuracyAndAreaReportForSimpleRandomSampling``
     or ``enmapbox:ClassificationLayerAccuracyAndAreaReportForStratifiedRandomSampling``
   * Depending on your input data, there are other algorithms for dataset creation, list them by
     running ``qgis_process list | grep CreateClassificationDataset``