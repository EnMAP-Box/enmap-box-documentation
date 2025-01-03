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

Extract multiple EnMAP Level 2A products
........................................

We assume that a lot of EnMAP Level 2 data has been ordered and was downloaded to ``INPUT_FOLDER``.

.. code-block:: bash

   >INPUT_DIR=~/mydata/enmap_l2
   > ls -lh INPUT_DIR
   total 185G
   -rw-r--r-- 1 jakimowb zwei 4.5G Aug 13 17:37 dims_op_oc_oc-en_701696243_2.tar.gz
   -rw-r--r-- 1 jakimowb zwei 1.8G Aug 13 17:29 dims_op_oc_oc-en_701696349_1.tar.gz
   -rw-r--r-- 1 jakimowb zwei 4.7G Aug 13 17:31 dims_op_oc_oc-en_701696349_2.tar.gz
   -rw-r--r-- 1 jakimowb zwei 2.1G Aug 13 17:26 dims_op_oc_oc-en_701696455_1.tar.gz
   -rw-r--r-- 1 jakimowb zwei 4.4G Aug 13 17:28 dims_op_oc_oc-en_701696455_2.tar.gz
   -rw-r--r-- 1 jakimowb zwei 1.7G Aug 13 17:21 dims_op_oc_oc-en_701696615_1.tar.gz
   # <many more>

Each ``*.tar.gz`` file contains one or more EnMAP Level 2 products and auxiliary information.
These files can be listed with:

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


In order to process and visualize the EnMAP data more easily, we would like to:

1. extract all EnMAP01_*.ZIP files from the tar.gz archive
2. unzip all contained EnMAP01_*.ZIP files
3. use the EnMAP-Box `enmapbox:importEnmapL2AProduct` algorithm to create a single raster image with
   reflectance values and band-metadata that can be used in QGIS and the EnMAP-Box.
4. cleanup unzipped tar.gz and EnMAP01_*.ZIP files.

We can do this for a single \*.tar.gz file with the following script ``extract_enmap_tgz.sh``:

.. code-block:: bash

   #!/bin/bash
   # A script to extract EnMAP Level 2A *.tar.gz archives

   if [ "$#" -ne 2 ]; then
       echo "Usage: $0 FILE OUTPUT_DIR"
       exit 1
   fi

   # Assign arguments to variables
   FILE=$1
   OUTPUT_DIR=$2

   # Validate FILE
   if [ ! -f "$FILE" ]; then
       echo "Error: FILE '$FILE' does not exist or is not a regular file."
       exit 2
   fi


   # Validate OUTPUT_DIR
   if [ ! -d "$OUTPUT_DIR" ]; then
       echo "Error: OUTPUT_DIR '$OUTPUT_DIR' does not exist or is not a directory."
       exit 3
   fi



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
     echo "unzip $zip_file..."
     unzip -o "$zip_file" -d "$DIR_UNZIPPED"
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
   # temporary outputs
   rsync -a "$DIR_UNZIPPED/" "$OUTPUT_DIR"
   rm -r $DIR_TMP

Parallelize extraction and import
.................................

The extraction and import can take a while. Therefore we like to run it in parallel for multiple
files. We can do this using two other scripts, one that defines the SLURM job ``extract_all.slurm`` and one that starts it ``extract_all.sh``.

    .. tabs::

        .. tab:: extract_all.slurm

            This script defines the SLURM job that extracts each \*.tar.gz in a separated slurm [job array task](https://slurm.schedmd.com/job_array.html)

            .. code-block:: bash

               #!/bin/bash
               # Slurm job to extract EnMAP Level 2A *.tar.gz in parallel

               #SBATCH --ntasks=1                    # Run on a single CPU
               #SBATCH --mem=4gb                     # Job memory request
               #SBATCH --partition=standard
               #SBATCH --account=jakimowb
               #SBATCH --output=job_output_%A_%a.log
               #SBATCH --error=job_error_%A_%a.log
               #SBATCH --cpus-per-task=1             # CPUs per task

               OUTPUT_DIR=$2
               JOBLIST=$1

               # ensure that your standard environmental settings are available
               source ~/.bashrc
               # activate the enmapbox conda environment
               module load miniforge3
               conda activate enmapbox
               export QT_QPA_PLATFORM=offscreen
               mkdir -p $OUTPUT_DIR

               FILE=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" "$JOBLIST")
               if [ -z "$FILE" ]; then
                   echo "No file found for SLURM_ARRAY_TASK_ID=$SLURM_ARRAY_TASK_ID"
                   exit 1
               fi

               # Process the file
               echo "Processing file: $FILE"
               source extract_enmap_tgz.sh "$FILE" "$OUTPUT_DIR"


        .. tab:: extract_all.sh

            This script adds the slurm job and all its sub-tasks to the SLURM job queue:

            .. code-block:: bash

               #!/bin/bash
               # A script to submit a SLURM job array to extract EnMAP Level 2A *.tar.gz archives

               INPUT_DIR=~/mydata/enmap_input
               OUTPUT_DIR=~/mydata/enmap_l2_tif
               JOBLIST=~/joblist.txt
               # mapfile -t FILES < <(find "$INPUT_DIR" -name "*.tar.gz" -type f)
               find "$INPUT_DIR" -name "*.tar.gz" -type f > "$JOBLIST"


               # ensure that your standard environmental settings are available
               source ~/.bashrc

               # activate the enmapbox conda environment
               module load miniforge3
               conda activate enmapbox

               export QT_QPA_PLATFORM=offscreen
               mkdir -p $OUTPUT_DIR

               # Count the number of files
               NUM_FILES=$(wc -l < "$JOBLIST")
               echo "Found $NUM_FILES tar.gz files."

               if [ "$NUM_FILES" -eq 0 ]; then
                   echo "No files found. Exiting."
                   exit 1
               fi

               # Submit the Slurm job array
               echo "Submitting Slurm job array with $NUM_FILES files..."
               sbatch --array=0-$(($NUM_FILES - 1))%4 extract.slurm $JOBLIST $OUTPUT_DIR


Calling ``./extract_all.sh`` will submit a SLURM job array that processes all EnMAP Level 2A \*.tar.gz files in parallel.

Inspect the job status
......................

The [squeue](https://slurm.schedmd.com/squeue.html) command can be used to inspect the job status:

.. code-block:: bash

   > squeue -u $USER
   JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   19523_0  standard extract. jakimowb  R       9:45      1 slurm-exec-029
   19523_1  standard extract. jakimowb  R       9:45      1 slurm-exec-029
   19523_2  standard extract. jakimowb  R       9:45      1 slurm-exec-029
   19523_3  standard extract. jakimowb  R       9:45      1 slurm-exec-029

Actually 4 jobs are running (ST = *R*) in parallel, as intended when starting the slurm job with ``--array=0-$(($NUM_FILES - 1))%4``.



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
