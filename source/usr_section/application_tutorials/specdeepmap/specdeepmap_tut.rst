

11. Spectral Imaging Deep Learning Mapper (SpecDeepMap): A Tutorial for Semantic Segmentation
#############################################################################################

**Authors:** Leon-Friedrich Thomas

**Publication date:** 01/04/2025

This tutorial give an introduction to the Processing Algorithms of the Spectral Imaging Deep Learning Mapper (SpecDeepMap) application.
It is designed for EnMAP-Box 3.16 or higher. Minor changes may be present in subsequent versions, such as modified menu labels or added parameter options.

In this Tutorial we will fine-tune a pretrained Resnet18 backbone for Sentinel-2 Top of Atmosphere reflectance imagery with European Union Crop type Map (EUCROPMAP) labels for a semantic segmentation task.

Introduction to SpecDeepMap
***************************

The SpecDeepMap applictaion consists of six QGIS processing algorithms and is designed for Semantic Segmentation tasks (pixel classification). With this application a user can train  deep-learning architectures U-Net, U-Net++, DeepLabV3+, and SegFormer with a variety of encoder backbones, such as ResNet-18 and -50, EfficientNet, MobileNet, ConvNext, and Swin-Transformer. SpecDeepMap is designed for multispectral and hyperspectral images and takes geospatial data characteristics into account. A highlight is the integration of the foundation model backbones ResNet-18 and ResNet-50 trained for Sentinel-2 Top of Atmosphere Reflectance Imagery.

    .. figure:: img/1_SpecDeepMap_Overview.png

         SpecDeepMap Workflow

Installation of SpecDeepMap
***************************

SpecDeepMap is available by default in EnMAP-box from 3.16 onwards until further notice. Follow EnMap-Box installation guide to regulary set up EnMAP-Box here or install via QGIS:
https://enmap-box.readthedocs.io/en/latest/usr_section/usr_installation.html

Install QGIS & SpecDeepMAp via mini-conda (cross-platform)
==========================================================

Miniconda is a cross-platform package manager that allows install software in separated environments. Get miniconda from https://www.anaconda.com/docs/getting-started/miniconda/main
After installing miniconda open the Mini-conda Prompt from the start menu.

    .. figure:: img/conda.jpg
         :scale: 60%

Install the an python environment using a yml file via the following command.

.. code-block:: bash

   conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap.yml -c conda-forge -y

Activate the "specdeepmap" environment and open QGIS by executing:

.. code-block:: bash

   activate specdeepmap
   qgis

In Qgis you can open EnMAP-Box and access SpecDeepMap via the EnMAP-box processing algorithm menu.

Install QGIS & SpecDeepMAp via mini-conda with GPU support (optional)
=====================================================================

If you have a cuda capable GPU you can also install cuda to use SpecDeepMap with GPU support:

Step 1: Activate the environment

.. code-block:: bash

   conda activate specdeepmap

Step 2: Re-install pytorch with cuda GPU support via pip (example for CUDA 12.4). This might take some time as cuda is around 4,5 GB.

.. code-block:: bash

   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 -y --force-reinstall

Not tested by myself but setting up cuda support is also possible via OSGeo4W Shell under windows. For this the developer of GEO-SAM recommend to first download and install the CUDA Toolkit (https://developer.nvidia.com/cuda-downloads) e.g. cuda 12.4 and then run step.2 command in the shell. (see:https://geo-sam.readthedocs.io/en/latest/installation.html ).

Recovery Environment with Explicitly Defined Setup for QGIS & SpecDeepMap via Miniconda (Cross-Platform)
========================================================================================================

If SpecDeepMap encounters issues due to Python package updates or incompatibilities, you can restore a fully functional environment using the provided configuration files. These define all required packages explicitly, ensuring that both CPU and GPU versions run reliably across platforms.

For cpu version run the following command in miniconda shell:

.. code-block:: bash

   conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap_cpu.yml -c conda-forge -y

For GPU version with cuda 12.4 run the following command in miniconda shell. If you need newer cuda version you can also create just the cpu environment and run a re-force install with newer cuda version (see step 2. of cuda installation).

.. code-block:: bash

   conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap_cuda.yml -c conda-forge -y



Getting started
***************

SpecDeepMap Menu
================

Launch QGIS and click the enmapbox icon in the toolbar to open the EnMAP-Box. In the EnMAP-Box GUI you can find the SpecDeepMap application in the algorithms in the **EnMAP-Box Processing Algorithms**.

    .. figure:: img/specdeepmap_menu.png

         SpecDeepMap Workflow

Download Example Data
=====================

* Download the imagery data and example label rasters from here
* Sentienl-2 TOA imagery download Sentinel-2 TOA imagery.
* EUCropmap labels: :download: EUCropmap labels.


1. Raster Splitter
******************

The Raster Splitter split a spectral imagery raster and a corresponding label raster with the same size into smaller image and label chips.
Classification Label raster should be expressed in any numeric values in range 0-255. The value 0 is reserved for unclassified or no-data.
The software user can define the chip size in X and y direction by the parameter tile size X and tile size Y. And also a step size X and step size Y.
In this example we split the Sentienl-2TOA image and the EUCROPMAP labels into smaller chips.


   .. figure:: img/1_Rastersplitter.jpeg

         Raster Splitter Interface

* Use the following inputs:  **Input raster image**: Sentinel_2_TOA_1.tif and **Input raster labels**: EUCROPMAP_1.tif .

* Set **tile size X** to 224 and **tile size Y** to 224 and **step size X** to 275 and **step size Y** to 275, to avoid spatial autocorrelation of the chips.

* Set **Minimum Class Label coverage per Tile (%)** to 100. This parameter define if we want only image chips with full label coverage or also partial covered label. In our case we use only fully covered labels chips so, set the parameter to 100.

* As **Output folder** Create a new folder call it SpecDeepMap_tutorial , chose the folder for the raster splitter output.*

* Run the algorithm with the given parameters this results in 2328 image and label chips. These are now stored in sub folder 'images' and 'labels' in the created folder 'SpecDeepMap_tutorial'.



2. Dataset Maker
****************

The Dataset Maker takes the created folder as Input and generates a training, validation and test datatsets with similar class distributions in form of CSV files with stored relative file paths to the image chips.
As well as a summary CSV file which show class distribution per dataset as well as suitable class weights for balanced training.

* As **Data folder** use the created  SpecDeepMap_tutorial folder.
* A default dataset split **Percentages of train images** is 80 and **Percentages of test images** is 10  and **Percentages of validation images** is 10. We will run the algorithm with this default setting. You can change this to a subset if you have less computing power e.g. **Percentages of train images** to 10 and  **Percentages of test images** to 5  and **Percentages of validation images** to 5.

* As **Output folder** use the previously created SpecDeepMap_tutorial folder.

   .. figure:: img/2_Dataset_Maker.jpeg

         Dataset Maker Interface

* Run the algorithm with the default split percentages of train images 80%, percentage of test image 10%, percentage of validation images 10%.

* After the algorithm run it displays all created CSV files in a window. If you feel like inspecting one you can click on it and it will be added to the file menus. Otherwise you can just close the window.
* Optionally if you want to later inspect a csv file e.g. the summary table in the enmapbox and load the 'Summary_train_val.csv' located in the SpecDeepMap_tutorial folder and open the attribute table.

   .. figure:: img/2_Dataset_Maker_Output.jpeg

         Dataset Maker Outputs: Summary CSV

3. Deep Learning Trainer
************************

The Deep Learning Trainer algorithm,  trains a deep-learning model in a supervised manner for a semantic segmentation task. It offers flexibility by enabling the training of various architectures, like U-Net, U-Net++, DeeplabV3+, and SegFormer paired with diverse backbones such as ResNet-50. A list of natively supported backbones can be found at https://smp.readthedocs.io/en/latest/encoders.html. Moreover, approximately 500 backbones from Pytorch Image Model Library, also known as Timm, are available, such as ConvNext and Swin-Transformers. A complete list of available Timm Encoders backbones is provided here: https://smp.readthedocs.io/en/latest/encoders_timm.html . To use any of the timm encoders 'tu-' must be added before the model string name.

   .. figure:: img/3_Deep_learning_trainer.jpeg

         Deep Learning Trainer Interface

* As **Input folder (Train and Validation dataset)** use the SpecDeepMap_tutorial folder. By **model architecture** and **model backbone** you can define possible model combinations. For this example leave the default values so Unet and resnet18.
* Change the **Load pretrained weights** parameter to Sentinel_2_TOA_Resnet18 to load the pretrained weights for Sentinel-2 TOA imagery stemming from Wang et al 2023 (https://arxiv.org/abs/2211.07044).
* We will use the default for the following parameter and leave them checked (**freeze backbone**, **data augumentation**, **early stopping** and **balanced Training using class weights**)

* As **Batch size** we use 16 and for **Epochs** 50. ( If you have less computational resources you can use als a batch size of 4 or 8 and only train for 5-8 epochs.
* As **Learning rate** we will use 0.003.
* As **type of device** use GPU if available and installed for the enmapbox python environment. Otherwise use CPU, isf you use CPU you can also just reduce the **Epochs** to 2, to minimize the waiting time.

* As **Path for saving tensorboard logger** use the SpecDeepMap_tutorial folder.
* As **Path for saving model** use the SpecDeepMap_tutorial folder.
* Lest run the model.

During training in the Logger Interface the progress of the training is printed after each epoch. (epoch means one loop through the training dataset). In the logger the train and validation loss is displayed, which should reduce during training and the train IoU and val IoU should increase.
The model uses the training data for learning the weights and the validation data is just used to check if the model over or underfits. ( if train and validation values are very different).
After training the logger displays the best model path for the best model. In general you want to use the model with the highest IoU score on the validation dataset. This is also written into the model file name, so you can find it later again at any time.
Here a logger visualization of the training we just performed. In our case with GPU 47 epochs took around 12 min. 47 because of early stopping ( stops training if val IoU doesn't increases).

   .. figure:: img/3_Deep_learning_trainer_output.jpeg

         Visualization of IoU and Loss per epoch during training of Deep Learning Trainer


4. Tensorboard visualizer (optional)
************************************

If you want to inspect the model behavior in more detail after the training you can use this algorithm and the logger location to open a Tensorboard, which is an interactive graphical environment to inspect model training behavior.
To call the Tensorboard visualizer you need to define as input the location where you saved the model logger in the Deep Learning trainer algorithm.

* Define for **Tensorboard logger Directory** the subfolder SpecDeepMap_tutorial/lightning_logs.
* The default **TensorBoard port** is 8000. In windows there is no need to change the port as each tensorboard port will be terminated before a new tensorboard is initialized. In other systems the algorithm doesnt support the port terminataion and it is  necessary to define a different port each time to open a new tensorboard.

   .. figure:: img/4_Tensorboard_visualizer.jpeg

         Tensorboard Interface

* Here a snippet of the Tensorboard visualization.

   .. figure:: img/4_Tensorboard_visualizer_output.jpeg

         Visualized Tensorboard

5. Deep Learning Tester
***********************

The Deep Learning Tester evaluates the performance of a trained model on the test dataset. Hereby it calculates the Intersection over Union Score per class as well as the overall mean.
For the parameter **Test Dataset** input the test_files.csv which we created with the Dataset Maker, it should be located in the folder SpecDeepMap_tutorial.

* As model checkpoint you should load the model with the highest Val IoU ( score is written in created checkpoint file names). Load the model with highest val iou score or download this checkpoint file and load the model from the checkpoint file.


   .. figure:: img/5_Deep_learning_tester.jpeg

         Deep Learning Tester Interface


* Use as **Device** GPU if available otherwise CPU.

* Define the location where you want to save **IoU CSV**. Use SpecDeepMap_tutorial as folder location and save a file test_score.csv in it.

* leave rest of default values as is. Run the algorithm. If you load test_score.csv in enmapbox you can inspect the Iou score per class and mean on test dataset. For this load the CSV and open it attribute table.

* Test achived a performance of Iou 0.56, which is in line with other foundation model performances on similar tasks.

* Here the test_score.csv visualized in enmapbox.

   .. figure::  img/5_Deep_learning_tester_output.jpeg

         Deep Learning Tester Output - IoU Scores on test dataset


6. Deep Learning Mapper
***********************

The Deep Learning Mapper can apply a trained model to an entire orthomosaic or satellite scene. In the background this algorithm automatically extracts overlapping image chips from the Input raster, predicts on them and crops them and combine them back together to a continiuos prediction image.
This enables easy employment of the model (also automatically apply same scaling and normalization as used in training of model). By cropping boundary pixels it also minimizes noise in prediction by reducing boundary effect common in 2D- CNNs.


   .. figure::  img/6_Deep_learning_mapper.jpeg

         Deep Learning Mapper Interface

* Use as **Input Raster** the spectral image Sentinel_2_TOA_2.tif and **Ground Truth Raster**: EUCROPMAP_2.tif .

* Use your model checkpoint with highest IoU on Validation data for **Model Checkpoint** ( same checkpoint as we used for the Deep Learning Tester).
* Otherwise use the downloaded checkpoint.

* For the **Minimum overlap of tiles in Percentage** use 20.

* Use ** Device** GPU if available otherwise CPU.

* For **Prediction as Raster** define the output: EU_CROPMAP_2_prediction.tif in the SpecDeepMap_tutorial folder.
* For **IoU CSV** define output: EU_CROPMAP_2_score.csv in the SpecDeepMap_tutorial folder.
* Run the algorithm.

You can open the predicted Raster and CSV in the Enmap-box to inspect the prediction visually and the IoU score per class. Mean IoU is 0.71 great!


   .. figure::  img/6_Deep_learning_mapper_output.jpeg

         Deep Learning mapper Output:Predicted Raster and IoU score


* Now you have absolved the Tutorial, congratultions!




.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |enmapbox| image:: /img/icons/enmapbox.png
   :width: 28px
.. |mActionDeleteSelected| image:: /img/icons/mActionDeleteSelected.svg
   :width: 28px
.. |mActionDeselectAll| image:: /img/icons/mActionDeselectAll.svg
   :width: 28px
.. |mActionInvertSelection| image:: /img/icons/mActionInvertSelection.svg
   :width: 28px
.. |mActionNewAttribute| image:: /img/icons/mActionNewAttribute.svg
   :width: 28px
.. |mActionSaveAllEdits| image:: /img/icons/mActionSaveAllEdits.svg
   :width: 28px
.. |mActionSaveEdits| image:: /img/icons/mActionSaveEdits.svg
   :width: 28px
.. |mActionSelectAll| image:: /img/icons/mActionSelectAll.svg
   :width: 28px
.. |mActionToggleEditing| image:: /img/icons/mActionToggleEditing.svg
   :width: 28px
.. |mSourceFields| image:: /img/icons/mSourceFields.svg
   :width: 28px
.. |plus_green_icon| image:: /img/icons/plus_green_icon.svg
   :width: 28px
.. |profile| image:: /img/icons/profile.svg
   :width: 28px
.. |profile_add_auto| image:: /img/icons/profile_add_auto.svg
   :width: 28px
.. |select_location| image:: /img/icons/select_location.svg
   :width: 28px
.. |speclib_add| image:: /img/icons/speclib_add.svg
   :width: 28px
.. |speclib_save| image:: /img/icons/speclib_save.svg
   :width: 28px
.. |viewlist_spectrumdock| image:: /img/icons/viewlist_spectrumdock.svg
   :width: 28px
