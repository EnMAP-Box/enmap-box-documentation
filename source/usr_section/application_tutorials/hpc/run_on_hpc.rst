EnMAP-Box in High Performance Computing (HPC) environments
==========================================================

.. _run_on_hpc:


This section describes how the EnMAP-Box can be installed and used on a Linux Server using the job scheduler SLURM.

.. note::

    This guide is written for users who are familiar with the command line and job schedulers. If you are not familiar with these topics, please ask your system administrator for help.

    This guide was tested on High-Performance Computing Platform (HPC)  provided by the Humboldt-Universität zu Berlin
    https://hu.berlin/hpc .

Installation
------------

1. Login to your HPC shell

2. Ensure that conda / miniconda is installed and available to you.
   See [miniforge3](https://github.com/conda-forge/miniforge) for installation instructions.

   Example: to activate conda on the HU HPC, you need to load the miniforge3 module.

    .. code-block:: bash

        module load miniforge3


3. Create a conda environment *enmapbox* with all dependencies needed to the EnMAP-Box:

    .. code-block:: bash

        conda env create -n enmapbox -f https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_latest.yml

4. Activate *enmapbox* and ensure that the local QGIS installation is setup right:

    .. code-block:: bash

        # activate EnMAP-Box environment
        conda activate enmapbox

        # show version infos
        qgis_process --version

        # list qgis plugins
        qgis_process plugins # list plugins
        qgis_process list # list available processing algorithms


    To visualize geo-data on the HPC, you can start QGIS in a X-Window:

    .. code-block:: bash

        qgis&


5. Install and activate the EnMAP-Box QGIS plugin. Either start the QGIS GUI and use the QGIS plugin manager, or use
   the `3Liz qgis-plugin-manager <https://github.com/3liz/qgis-plugin-manager>`_ to manage QGIS plugins from the command line.


    .. tabs::

        .. tab:: QGIS GUI

            1. Call ``qgis&`` to ppen QGIS in an X-Window
            2. Go to Plugins -> Manage and Install Plugins
            3. Search for 'EnMAP-Box'
            4. Click on 'Install Plugin'

            .. figure:: img/qgis_plugin_manager.png
               :align: center


        .. tab:: Command Line (Bash)

            To install QGIS plugins from CLI only, we fist install the https://github.com/3liz/qgis-plugin-manager

            .. code-block:: bash



                # define the path where your plugins are stored
                export QGIS_PLUGINPATH=~/.local/share/QGIS/QGIS3/profiles/default/python/plugins
                mkdir $QGIS_PLUGINPATH

                # install the 3Liz qgis-plugin-manager
                conda install qgis-plugin-manager
                qgis-plugin-manager init
                qgis-plugin-manager update

                # install the EnMAP-Box
                qgis-plugin-manger install 'EnMAP-Box 3'



7. Check that the EnMAP-Box is installed and their processing algorithms available on your CLI:

    Call ``qgis_process plugins list`` to see which plugins are loaded and available.

    .. code-block:: bash

        jakimowb@slurm-login:~> qgis_process plugins list
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/enmapboxresources_rc.py
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/coreapps/enmapboxapplications/ressources_rc.py
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/qgispluginsupport/qps/qpsresources_rc.py
        <frozen importlib._bootstrap>:488: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 216 from C header, got 232 from PyObject
        Problem with GRASS installation: GRASS was not found or is not correctly installed
        Available plugins
        (* indicates loaded plugins which implement Processing providers)

          enmapboxplugin
        * grassprovider
        * processing


    If necessary, enable the EnMAP-Box plugin with ``qgis_process plugins enable enmapboxplugin``:

    .. code-block:: bash

        jakimowb@slurm-login:~> qgis_process plugins enable enmapboxplugin
        Enabling plugin: "enmapboxplugin"
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/enmapboxresources_rc.py
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/coreapps/enmapboxapplications/ressources_rc.py
        load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/qgispluginsupport/qps/qpsresources_rc.py
        <frozen importlib._bootstrap>:488: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 216 from C header, got 232 from PyObject
        Enabled enmapboxplugin (EnMAP-Box 3)

        Available plugins
        (* indicates enabled plugins which implement Processing providers)

        * enmapboxplugin
        * grassprovider
        * processing



    Now list the processing algorithms provided by the EnMAP-Box:

    .. code-block:: bash

        qgis_process list | grep 'enmapbox'
        <frozen importlib._bootstrap>:488: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 216 from C header, got 232 from PyObject
        Problem with GRASS installation: GRASS was not found or is not correctly installed
        enmapbox:AggregateRasterLayerBands      Aggregate raster layer bands
        enmapbox:AggregateRasterLayers  Aggregate raster layers
        enmapbox:ApplyMaskLayerToRasterLayer    Apply mask layer to raster layer
        enmapbox:Build3DCube    Build 3D Cube
        enmapbox:ClassFractionLayerFromCategorizedLayer Class fraction layer from categorized layer
        enmapbox:ClassSeparabilityReport        Class separability report
        enmapbox:ClassificationLayerAccuracyAndAreaReportForStratifiedRandomSampling    Classification layer accuracy and area report (for stratified random sampling)
        enmapbox:ClassificationLayerAccuracyReport      Classification layer accuracy report
        enmapbox:ClassificationLayerFromClassProbabilityfractionLayer   Classification layer from class probability/fraction layer
        enmapbox:ClassificationLayerFromRenderedImage   Classification layer from rendered image
        enmapbox:ClassificationWorkflow Classification workflow
        enmapbox:ClassifierFeatureRankingPermutationImportance  Classifier feature ranking (permutation importance)
        enmapbox:ClassifierPerformanceReport    Classifier performance report
        enmapbox:ConvexHullAndContinuumremoval  Convex hull and continuum-removal
        enmapbox:CreateClassificationDatasetFromCategorizedRasterLayerAndFeatureRaster  Create classification dataset (from categorized raster layer and feature raster)
        enmapbox:CreateClassificationDatasetFromCategorizedSpectralLibrary      Create classification dataset (from categorized spectral library)
        enmapbox:CreateClassificationDatasetFromCategorizedVectorLayerAndFeatureRaster  Create classification dataset (from categorized vector layer and feature raster)
        enmapbox:CreateClassificationDatasetFromCategorizedVectorLayerWithAttributeTable        Create classification dataset (from categorized vector layer with attribute table)
        enmapbox:CreateClassificationDatasetFromJsonFile        Create classification dataset (from JSON file)
        enmapbox:CreateClassificationDatasetFromPythonCode      Create classification dataset (from Python code)
        enmapbox:CreateClassificationDatasetFromTableWithCategoriesAndFeatureFields     Create classification dataset (from table with categories and feature fields)
        enmapbox:CreateClassificationDatasetFromTextFiles       Create classification dataset (from text files)
        . . .


Run EnMAP-Box GUI
-----------------

1. Call ``qgis&`` to open QGIS in an X-Window.
2. Click the EnMAP-Box icon |enmapbox| to start the EnMAP-Box
3. Click *Project->Add Exampledata* to download and visualize the EnMAP-Box example data.


.. figure:: img/hpc_qgis_with_enmapbox.png


Run Processing Algorithms
-------------------------

Let's create a working directory and download some example data:

.. code-block:: bash


    DIR_DATA=/lustre/geographie/jakimowb/data
    mkdir -p $DIR_DATA
    cd $DIR_DATA
    wget -O enmapdata.zip https://box.hu-berlin.de/f/c35a6b0655c54d518aab/?dl=1
    unzip enmapdata.zip -d enmapdata

    # list all *METADATA.XML files
    find . -type f -name '*METADATA.XML'


Select the METADATA.XML path and run the *EnMAP-Box import EnMAP L2A* algorithm. It will create a single raster file from the L2A product that
contains the reflectance values of the EnMAP bands and enriches this raster with metadata for QGIS and the EnMAP-Box.

.. code-block:: bash

   PATH_L2A=enmapdata/ENMAP01-____L2A-DT0000001867_20220724T104526Z_008_V010302_20230628T165614Z-METADATA.XML
   qgis_process run enmapbox:ImportEnmapL2AProduct \
      --detectorOverlap=1 \
      --file=$PATH_L2A \
      --outputEnmapL2ARaster=$DIR_DATA/enmap_l2a.vrt


The output should look like:

.. code-block:: bash

   load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/enmapboxresources_rc.py
   load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/coreapps/enmapboxapplications/ressources_rc.py
   load /home/geographie/jakimowb/.local/share/QGIS/QGIS3/profiles/default/python/plugins/enmapboxplugin/enmapbox/qgispluginsupport/qps/qpsresources_rc.py
   <frozen importlib._bootstrap>:488: RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 216 from C header, got 232 from PyObject
   Problem with GRASS installation: GRASS was not found or is not correctly installed

   ----------------
   Inputs
   ----------------

   file:   enmapdata/ENMAP01-____L2A-DT0000001867_20220724T104526Z_008_V010302_20230628T165614Z-METADATA.XML
   outputEnmapL2ARaster:   /lustre/geographie/jakimowb/data/enmap_l2a.tif


   Create Raster [1275x1240x206](Float32) -co INTERLEAVE=BAND COMPRESS=LZW TILED=YES BIGTIFF=YES /lustre/geographie/jakimowb/data/enmap_l2a.tif
   0...10...20...30...40...50...60...70...80...90...100 - done.
   Execution completed in 19.3 seconds
   Results: {'outputRaster': '/lustre/geographie/jakimowb/data/enmap_l2a.tif'}
   Execution completed in 22.61 seconds

   ----------------
   Results
   ----------------

   outputEnmapL2ARaster:   /lustre/geographie/jakimowb/data/enmap_l2a.tif


Now open the image in QGIS:

.. code-block:: bash

    qgis $DIR_DATA/enmap_l2a.vrt&

.. figure:: img/hpc_qgis_enmap_l2a_import.png

Run Processing Models
---------------------

The QGIS Model Designer allows you to create QGIS Processing Models to describe comprehensive workflows that combine EnMAP-Box and other
QGIS algorithms.

.. figure:: img/hpc_qgis_model_builder.png


These models can be saved an shared in \*.model3 files. Download the :download:`CreateSpectralIndices.model3 <models/CreateSpectralIndices.model3>`
and show its parameters:

.. code-block:: bash

   >qgis_process help ~/CreateSpectralIndices.model3

      CreateIndices (CreateIndices)

   ----------------
   Description
   ----------------


   ----------------
   Arguments
   ----------------

   inputfile: InputFile
           Argument type:  file
           Acceptable values:
                   - Path to a file
   outputimage: OutputImage
           Argument type:  rasterDestination
           Acceptable values:
                   - Path for new raster layer

   ----------------
   Outputs
   ----------------

   outputimage: <outputRaster>
           OutputImage



To run it, call:

.. code-block:: bash

   > qgis_process run ~/CreateSpectralIndices.model3 \
         -- inputfile=ENMAP01-____L2A-DT0000001867_20220724T104526Z_008_V010302_20230628T165614Z-METADATA.XML \
            outputimage=~/myresult.tif

   ----------------
   Inputs
   ----------------

   inputfile:      ENMAP01-____L2A-DT0000001867_20220724T104526Z_008_V010302_20230628T165614Z-METADATA.XML
   outputimage:    /home/geographie/jakimowb/myresult.vrt


   Create Raster [1275x1240x218](Float32) -co INTERLEAVE=BAND COMPRESS=LZW TILED=YES BIGTIFF=YES /tmp/processing_zzyKzi/0854a4cf4d624d69803deeb2ce382e00/outputEnmapL2ARaster.tif
   0...10...20...30...40...50
   Execution completed in 18.73 seconds
   Results: {'outputRaster': '/tmp/processing_zzyKzi/0854a4cf4d624d69803deeb2ce382e00/outputEnmapL2ARaster.tif'}
   Execution completed in 21.99 seconds
   gdal_vrt_module_0x557a0e002550:12: RuntimeWarning: invalid value encountered in divide
   gdal_vrt_module_0x557a0aca6bc0:12: RuntimeWarning: invalid value encountered in divide
   gdal_vrt_module_0x557a12d68350:12: RuntimeWarning: invalid value encountered in divide
   gdal_vrt_module_0x557a0dfdbec0:12: RuntimeWarning: invalid value encountered in divide
   Execution completed in 2.37 seconds
   ...60...70...80...90...100 - done.
   Model processed OK. Executed 2 algorithm(s) total in 24.479 s.

   ----------------
   Results
   ----------------

   outputimage:    /home/geographie/jakimowb/myresult.tif


Call ``qgis ~/myresult.tif`` to visualize the created image in QGIS:

.. figure:: img/hpc_qgis_spectral_indices.png




Use SLURM
---------

We assume that a lot of EnMAP Level 2 data has been ordered and already downloaded to ``INPUT_FOLDER``.

.. code-block:: bash

   >INPUT_DIR=~/mydata/enmap_l2
   > ls -l INPUT_DIR
   total 22473296
   -rw-r--r-- 1 jakimowb zwei 1869591839 Aug 13 17:40 dims_op_oc_oc-en_701696137_1.tar.gz
   -rw-r--r-- 1 jakimowb zwei 4879114711 Aug 13 17:41 dims_op_oc_oc-en_701696137_2.tar.gz
   -rw-r--r-- 1 jakimowb zwei 1785007592 Aug 13 17:35 dims_op_oc_oc-en_701696243_1.tar.gz
   -rw-r--r-- 1 jakimowb zwei 4792925417 Aug 13 17:37 dims_op_oc_oc-en_701696243_2.tar.gz
   -rw-r--r-- 1 jakimowb zwei 1910992910 Aug 13 17:29 dims_op_oc_oc-en_701696349_1.tar.gz
   ...

Each ``dims_*_tar.gz`` file contains one or more EnMAP Level 2 products and auxiliary information that can
be listed with:

.. code-block:: bash

   > tar -tzf dims_op_oc_oc-en_701696137_1.tar.gz
   dims_op_oc_oc-en_701696137_1/
   dims_op_oc_oc-en_701696137_1/tools/
   dims_op_oc_oc-en_701696137_1/tools/defcopyright.html
   dims_op_oc_oc-en_701696137_1/tools/EnMAP_Data_License_v1.1_final.pdf
   dims_op_oc_oc-en_701696137_1/tools/EnMAP_Data_License_v1.1_final.pdf.tooldes
   dims_op_oc_oc-en_701696137_1/tools/iif.xsd
   dims_op_oc_oc-en_701696137_1/tools/iif.xsd.tooldes
   dims_op_oc_oc-en_701696137_1/tools/tf.xsd
   dims_op_oc_oc-en_701696137_1/tools/tf.xsd.tooldes
   dims_op_oc_oc-en_701696137_1/tools/leiste.gif
   dims_op_oc_oc-en_701696137_1/tools/logo_dlr.jpg
   dims_op_oc_oc-en_701696137_1/tools/logo_dfd.jpg
   dims_op_oc_oc-en_701696137_1/tools/erde_weiss_small.gif
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/ENMAP01-____L2A-DT0000014911_20230428T093524Z_016_V010402_20240809T151155Z.ZIP
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/ENMAP01-____L2A-DT0000014911_20230428T093533Z_018_V010402_20240809T145654Z.ZIP
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/ENMAP01-____L2A-DT0000014911_20230428T093520Z_015_V010402_20240809T151634Z.ZIP
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/ENMAP01-____L2A-DT0000014911_20230428T093529Z_017_V010402_20240809T145835Z.ZIP
   dims_op_oc_oc-en_701696137_1/ENMAP.HSI.L2A/ENMAP01-____L2A-DT0000014911_20230428T093506Z_012_V010402_20240809T152833Z.ZIP
   dims_op_oc_oc-en_701696137_1/iif/
   dims_op_oc_oc-en_701696137_1/iif/dims_nz_pl_dfd_XXXXB00000000681141327206_iif.xml
   dims_op_oc_oc-en_701696137_1/iif/dims_nz_pl_dfd_XXXXB00000000681141326695_iif.xml
   dims_op_oc_oc-en_701696137_1/iif/dims_nz_pl_dfd_XXXXB00000000681141327597_iif.xml
   dims_op_oc_oc-en_701696137_1/iif/dims_nz_pl_dfd_XXXXB00000000681141326969_iif.xml
   dims_op_oc_oc-en_701696137_1/iif/dims_nz_pl_dfd_XXXXB00000000681141328372_iif.xml
   dims_op_oc_oc-en_701696137_1/readme.html


In order to process and visualize the EnMAP data more easily, we would like to save the image data
as standardized TIFF format with BSQ interleave and metadata like band-wavelength information. For each tar.gz file we
like to:
1. unzip all contained EnMAP01_*.ZIP files
2. use the EnMAP-Box `enmapbox:importEnmapL2AProduct` algorithm to create a single raster image with
   reflectance values and band-metadata that can be used in QGIS and the EnMAP-Box.
3. cleanup unzipped tar.gz and EnMAP01_*.ZIP files.

The following bash script does this for all tar.gz files in the INPUT_DIR:

.. code-block:: bash

   #!/bin/bash


   INPUT_DIR=~/mydata/enmap_l2
   OUTPUT_DIR=~/mydata/enmap_l2_tif

   # ensure that your standard environmental settings are available
   source ~/.bashrc

   # activate the enmapbox conda environment
   module load miniforge3
   conda activate enmapbox

   mkdir -p $OUTPUT_DIR


   mapfile -t FILES < <(find "$INPUT_DIR" -name "*.tar.gz" -type f)
   echo "Found ${#FILES[@]} tar.gz files:"
   for FILE in "${FILES[@]}"; do

     DIR_TMP="$OUTPUT_DIR/$(basename "$FILE" .tar.gz)"
     mkdir -p $DIR_TMP

     # Step 1: extract zip files from tar.gz archive
     echo "Extract $FILE to $DIR_TMP..."
     tar -xzvf "$FILE" -C $DIR_TMP --wildcards '*.ZIP'


     # Step 2: unzip zip files
     mapfile -t ZIPFILES < <(find "$DIR_TMP" -name "ENMAP01*.ZIP" -type f)
     DIR_UNZIPPED="$DIR_TMP/unzipped"
     mkdir -p DIR_UNZIPPED
     for zip_file in "${ZIPFILES[@]}"; do
       echo "UNZIP $zip_file..."
       unzip "$zip_file" -o -d "$DIR_UNZIPPED"
       break
     done

     # Step 3: import the L2A product as image to be used with QGIS / EnMAP-Box
     mapfile -t METADATAFILES < <(find "$DIR_UNZIPPED" -name "ENMAP01*-METADATA.XML" -type f)
     echo "Found ${#METADATAFILES[@]} *.MEDATA.XML files:"
     for xml_file in "${METADATAFILES[@]}"; do
       tif_file="${xml_file%METADATA.XML}-IMAGE_L2A.tif"

       printf "Import $xml_file \nto $tif_file"

       qgis_process run enmapbox:ImportEnmapL2AProduct -- \
              file=$xml_file \
              setBadBands=true \
              excludeBadBands=true \
              detectorOverlap=0 \
              outputEnmapL2ARaster=$tif_file

     done

     # Step 4: move the EnMAP Scene folder to output directory and cleanup everything
     mv -r "$DIR_UNZIPPED"/* "$OUTPUT_DIR"
     rm -r $DIR_TMP
     break

   done

Now we enhance this script so that we can schedule it as SLURM job, and run the loop over all tar.gz files in the INPUT_DIR in parallel.





Notes
-----


The *QT_QPA_PLATFORM* environment variable can be used to enable or disable graphical windows for QGIS / Qt apps.

This is necessary to run the EnMAP-Box on a HPC which usually has now graphical interface.

.. code-block:: bash

    export QT_QPA_PLATFORM=offscreen




.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |enmapbox| image:: /img/icons/enmapbox.png
   :width: 28px
