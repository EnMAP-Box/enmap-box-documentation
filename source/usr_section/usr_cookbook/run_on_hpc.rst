Use EnMAP-Box on a High Performance Computer (HPC)
==================================================

.. _run_on_hpc:


This section describes how the EnMAP-Box can be installed and used on a Linux Server using the job scheduler SLURM.

.. note::

    This guide is written for users who are familiar with the command line and job schedulers. If you are not familiar with these topics, please ask your system administrator for help.


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


5. Install the EnMAP-Box from the plugin repository and activate it as a QGIS plugin.

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

        # if required, enable the EnMAP-Box plugin
        qgis_process plugins enable enmapboxplugin

7. List all available EnMAP-Box processing algorithms

    .. code-block:: bash

        qgis_process list | grep 'enmapbox'


6. Disable QGIS / Qt apps to show graphical windows.
    This is necessary to run the EnMAP-Box on a HPC which usually has now graphical interface.

    .. code-block:: bash

        export QT_QPA_PLATFORM=offscreen

    However, you might enable it again, e.g. to open QGIS & the EnMAP-Box in an X-Window and inspect your data.

7. Run an EnMAP-Box processing algorithm:

    .. code-block:: bash

        # run the EnMAP-Box
        qgis_process run enmapbox:EnMAPBox