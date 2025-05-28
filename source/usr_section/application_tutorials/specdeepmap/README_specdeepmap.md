# Spectral Imaging Deep Learning Mapper (SpecDeepMap)

SpecDeepMap is a free and open source Application available in EnMAP-BOX v3.16 [QGIS Plugin ](https://www.qgis.org).

The SpecDeepMap Applictaion consists of six QGIS processing algorithms and is designed for Semantic Segmentation tasks (pixel classification).  

1_SpecDeepMap_Overview.png

SpecDeepMap Workflow


# Highlights

* an easy-to-use graphical user interface for training a deep learning model for semantic segmentation

* SpecDeepMap algorithm take geographical data characteristics into account as well as higher dimensional data structure common for multi &hyperspectral images.
  e.g. raster images, field spectrometer or table-sheets.

* Available Deep Learning architectures  U-Net, U-Net++, DeepLabV3+, and SegFormer with a variety of encoder backbones, such as ResNet-18 and -50, EfficientNet, MobileNet, ConvNext, and Swin-Transformer. 

* Integration of the foundation model backbones ResNet-18 and ResNet-50 trained for Sentinel-2 Top of Atmosphere Reflectance Imagery.

Documentation: 

Git Repository: https://github.com/EnMAP-Box/enmap-box/tree/main/enmapbox/apps/SpecDeepMap


# Run SpecDeepMap

SpecDeepMap Applicatio is a QGIS Plugin that can be installed from the QGIS Plugin Manager with .

However, the following steps show you how to run the EnMAP-Box from python without starting the QGIS Desktop
application.

# Installation of SpecDeepMap

SpecDeepMap is available by default in EnMAP-Box from version 3.16 onwards. To install EnMAP-Box, follow the official guide:

[https://enmap-box.readthedocs.io/en/latest/usr\_section/usr\_installation.html](https://enmap-box.readthedocs.io/en/latest/usr_section/usr_installation.html)

## Install QGIS & SpecDeepMap via Miniconda (Cross-Platform)

Miniconda is a cross-platform package manager that allows you to install software in isolated environments.

1. Download and install Miniconda: [https://www.anaconda.com/docs/getting-started/miniconda/main](https://www.anaconda.com/docs/getting-started/miniconda/main)
2. Open the Miniconda Prompt from your start menu.
3. Run the following command to create the specdeepmap environment:

```bash
conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap.yml -c conda-forge -y
```

4. Activate the environment and start QGIS:

```bash
activate specdeepmap
qgis
```

Once QGIS opens, you can access SpecDeepMap via the EnMAP-Box processing algorithm menu.

## Install QGIS & SpecDeepMap with GPU Support (Optional)

If you have a CUDA-capable GPU, you can configure SpecDeepMap to use GPU acceleration.

### Step 1: Activate the Environment

```bash
conda activate specdeepmap
```

### Step 2: Install PyTorch with CUDA (e.g. CUDA 12.4)

This download is large (\~4.5 GB).

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 -y --force-reinstall
```

Note: Although not tested personally, CUDA setup is also possible via the OSGeo4W Shell on Windows. First, install the CUDA Toolkit: [https://developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads), then run Step 2 in the OSGeo4W Shell.

See more details here: [https://geo-sam.readthedocs.io/en/latest/installation.html](https://geo-sam.readthedocs.io/en/latest/installation.html)

## Recovery Environment with Explicit Setup (CPU/GPU)

If SpecDeepMap breaks due to package updates or compatibility issues, you can recover a working environment using pre-defined environment files.

These files ensure full reproducibility by pinning exact package versions.

### CPU-Only Environment

```bash
conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap_cpu.yml -c conda-forge -y
```

### GPU Environment (CUDA 12.4)

```bash
conda env create -n specdeepmap --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/specdeepmap_cuda.yml -c conda-forge -y
```

If you want to use a newer CUDA version, you can first create the CPU environment, then manually re-install PyTorch using the appropriate pip install command (as shown in Step 2 of the GPU setup).



# License

The SpecDeepMap is released under the GNU Public License (GPL) Version 3 or above. A copy of this licence can be found in
the LICENSE.txt file that is part of the SpecDeepMap folder here [https://github.com/EnMAP-Box/enmap-box/blob/main/enmapbox/apps/SpecDeepMap/LICENSE_specdeepmap.md] 

The SpecDeepMap application partially uses code from TorchGeo, originally authored by Adam Stewart and developed under Microsoft.

TorchGeo is licensed under the MIT License, full license here [https://github.com/EnMAP-Box/enmap-box/blob/main/enmapbox/apps/SpecDeepMap/NOTICE.md]






