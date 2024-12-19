Use EnMAP-Box on a High Performance Computer (HPC)
==================================================

.. _run_on_hpc:


This section describes how the EnMAP-Box can be installed and used on a Linux Server using the job scheduler SLURM.

.. note::

    This guide is written for users who are familiar with the command line and job schedulers. If you are not familiar with these topics, please ask your system administrator for help.


1. Login to your HPC shell

2. Ensure that conda / minicoda is installed and available to you.
   See [miniforge3](https://github.com/conda-forge/miniforge) for installation instructions.

   Example: to activate conda on the HU HPC, you need to load the miniforge3 module.

    .. code-block:: bash

        module load miniforge3


3. Create a new conda environment with EnMAP-Box installed.

    .. code-block:: bash

        # define name of EnMAP-Box environment
        ENVNAME=enmapbox

        # create a new conda environment with the EnMAP-Box installed
        conda env create -n $ENVNAME -f https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_latest.yml

4. Activate the EnMAP-Box environment and call qgis_process to ensure that the local QGIS installation is setup right.

    .. code-block:: bash

        # activate the EnMAP-Box environment
        conda activate $ENVNAME

        # show version infos
        qgis_process --version

        # list qgis plugins
        qgis_process plugins # list plugins
        qgis_process list # list available processing algorithms


5. If required, install the EnMAP-Box from the plugin repository.
   For doing so we use the install https://github.com/3liz/qgis-plugin-manager

    .. code-block:: bash

        # install the EnMAP-Box from the plugin repository
        qgis_process plugins install enmapbox

        # install https://github.com/3liz/qgis-plugin-manager
        export QGIS_PLUGINPATH=~/.local/share/QGIS/QGIS3/profiles/default/python/plugins
        mkdir $QGIS_PLUGINPATH

        conda install qgis-plugin-manager
        qgis-plugin-manager init
        qgis-plugin-manager update
        qgis-plugin-manger install 'EnMAP-Box 3'

        # check that the EnMAP-Box is installed
        qgis-plugin-manager list
        qgis_process plugins list

6. Disable QGIS / QT apps to show graphical windows.
    This is necessary to run the EnMAP-Box on a HPC which usually has now graphical interface.

    .. code-block:: bash

        export QT_QPA_PLATFORM=offscreen

    However, you might enable it, e.g. to show the EnMAP-Box via X-Window

7. Run an EnMAP-Box processing algorithm:

    .. code-block:: bash

        # run the EnMAP-Box
        qgis_process run enmapbox:EnMAPBox