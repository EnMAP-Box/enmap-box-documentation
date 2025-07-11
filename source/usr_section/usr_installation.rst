.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

############
Installation
############

The EnMAP-Box is a plugin for QGIS. It required the QGIS python API and various other python packages.
Here we describe how you can install QGIS, the required python packages and the EnMAP-Box plugin.


.. _usr_installation_install_qgis:

1. Install QGIS
===============

.. tabs::

   .. group-tab:: Windows

      **Install QGIS via the official Standalone/OSGeo4W Installer**

         Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box
         using the QGIS installer from https://www.qgis.org/en/site/forusers/alldownloads.html#windows.

         For beginners, we recommend using the standalone installers. More advanced QGIS users can use OSGeo4W installer,
         which eases updates of existing QGIS installation.

         In case you already have the current QGIS LTR or LR version installed, you can skip this step.

         In case you have an outdated QGIS version, make sure to install a current version.


   .. group-tab:: Linux

     **Install QGIS on Linux**

     Install QGIS as described here https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu ,
     or follow the instructions for conda.

   .. group-tab:: MacOS

      **Install QGIS on MacOS**

      .. note::

         As of June 2025, the official QGIS page https://qgis.org/en/site/forusers/download.html
         has the following notice:

         .. image:: /img/installation_macos_qgiswarning.png



         We have made better experiences in using conda to
         install QGIS and all python packages require to run the EnMAP-Box
         (tested on macOS Sequoia 15.5 (24F74), Intel MacBook 2010 and Mac Mini 2024).

         Therefore, please follow the installation guide given in the *Conda* tab.



      ..
         Therefore, please install QGIS either using **conda**, or using
         the installer provided `OpenGIS.ch <https://www.opengis.ch/>`_:


         #. Download the latest package installer from https://github.com/opengisch/qgis-conda-builder/releases.
         #. Open the installer in Finder using the context menu.

             .. figure:: /img/macos/opengisch/install_exp_finder.png
                :width: 60%

                Call *Open* from the finder's context menu ...

             .. figure:: /img/macos/opengisch/install_exp_open.png
                :width: 35%

                ... to show and use the *Open* button in the next dialog.

          #. Select a location to install the QGIS.app (e.g., ``QGIS-3.36.app``), such as `/System/Applications`.

             .. figure:: /img/macos/opengisch/install_exp_folder.png


   .. group-tab:: Conda

      .. _usr_installation_qgis_conda:

      **Install QGIS with conda (cross-platform)**

      Conda is a cross-platform package manager that allows to install software in separated environments. We recommend
      installing conda using `Miniforge <https://conda-forge.org/download>`_, a minimal installer which
      by default installs conda packages from the `conda-forge <https://conda-forge.org/>`_ channel.

      *Linux / Unix / MacOS:*

          .. code-block:: bash

            # download install script
            curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

            # run install script
            sh Miniforge3-$(uname)-$(uname -m).sh

      *Windows:*

            Download and run the miniforge installer from https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe


      When done, continue with the installation of `QGIS and python dependencies <usr_installation_install_dependencies_>`_ in conda.


.. _usr_installation_install_dependencies:

2. Install Python Dependencies
==============================

.. tabs::

   .. group-tab:: Windows

         **Install Python Dependencies**

         #. Close QGIS, if it is open.

         #. Open the OSGeo4W Shell from the start menu.

            .. image:: /img/windows_start_osgeo.png

         #. Install Python dependencies via PIP by executing:

            .. code-block:: batch

               pip install --upgrade --user -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/osgeo4w/requirements_osgeo4w.txt

            .. note::

              In rare cases, the user folder may contain wrongly installed packages,
              which are interfering with the package version managed by OSGeo4W, e.g. numpy, scipy or gdal.
              Wrongly installed packages can be deleted manually from the user folder.

              To locate the user folder used by your QGIS instance, run the following inside your QGIS Python console::

                 >>> import site
                 >>> print(site.USER_SITE)
                 C:\Users\Andreas\AppData\Roaming\Python\Python39\site-packages

         #. (Optional) Install **HDF5** dependency via the OSGeo4W installer:

            The **HDF5** dependency is only required for importing PRISMA products.

            Start the OSGeo4W installer by executing:

            .. code-block:: batch

               setup

            Search for **h5py**, select the latest version of the *python3-h5py* package and finish the installation.

            .. image:: /img/osgeo4w_install_h5py.png


         #. Open QGIS from the start menu.

   .. group-tab:: Linux

       **Install Python Dependencies**

       #. Open the Terminal (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`T`).

       #. Make sure the following packages are installed using the system package manager:

          .. code-block:: console

             sudo apt install python3-pip python3-venv pyqt5-dev-tools python3-matplotlib

       #. **(Optional)** For some EnMAP-Box tools you may also need the following packages:

          .. code-block:: console

             sudo apt install python3-h5py python3-pyqt5.qtopengl python3-netcdf4

       #. Open QGIS and the QGIS Python Console (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`P`). Type the following and confirm with enter:

          .. code-block:: python

             import sys; sys.executable

          This shows the path of the Python executable that QGIS is using, usually it is ``/usr/bin/python3``.
          We need to ensure that additional Python packages get installed into the same Python environment.
          This is the case if the command ``which python3`` returns the path of the Python executable shown in QGIS!

          If not, please use the full path, e.g. ``/usr/bin/python3`` instead of ``python3`` in the following steps.

          Close QGIS.

       #. Create a `virtual python environment <https://docs.python.org/3/library/venv.html>`_ in a directory of your choice (e.g. ``~/.virtualenvs/enmapbox``):

          .. code-block:: console

             python3 -m venv --upgrade-deps --system-site-packages ~/.virtualenvs/enmapbox

       #. Activate the environment:

          .. code-block:: console

             source ~/.virtualenvs/enmapbox/bin/activate

          Now you should see the environment name in brackets at the beginning of your prompt, e.g. ``(enmapbox)``.

       #. Install missing Python dependencies with pip inside the virtual environment:

          .. code-block:: console

             python3 -m pip install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/linux/requirements_ubuntu.txt

       #. Start QGIS (from the activated environment, see step 6):

          .. code-block:: console

             qgis

       .. hint::

         You can add a shortcut to your applications menu, so you do not have to open a Terminal and type the above-mentioned commands (6 & 8) every time you want to start QGIS with the EnMAP-Box environment:

         Create the file :file:`~/.local/share/applications/enmapbox.desktop` with the following content (if you used another installation path in the instructions above, change accordingly):

          .. code-block:: text

             [Desktop Entry]
             Name=QGIS (EnMAP-Box)
             Exec=/bin/bash -c "source ~/.virtualenvs/enmapbox/bin/activate && qgis %F"
             Terminal=false
             Icon=qgis
             Type=Application
             Categories=Education;Science;Geography;

   .. group-tab:: MacOS

       **Install Python Dependencies**

       Use the *QGIS-<version>.app* internal pip3 to install or update missing python packages:

       .. code-block:: bash

         /Applications/QGIS-3.36.app/Contents/bin/pip3 install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/macos/requirements_macos.txt

       .. note::
         This step needs to be repeated after updates to the QGIS.app.

         Do not-update packages like numpy or GDAL with pip, as this might break parts of your QGIS application.

   .. group-tab:: Conda

         **Install a python environment for the EnMAP-Box**

         #. Open the `Miniforge <https://conda-forge.org>`_ prompt

            .. image:: /img/windows_start_miniforge.png


         #. Install QGIS and python dependencies, using one of the conda environment files (`enmapbox_*.yml`) from
            https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda, e.g.

            .. code-block:: batch

                conda env create -n enmapbox --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_full.yml

            ``--file=<uri>`` specifies the path to the \*.yml file that defines the environment.

            ``-n <name>`` or ``--name <nam>`` can be used to change the environment name.

            The environment files provided for download vary by used QGIS release and python packages to be:

            * *full* environments contains *all* python packages, including those used by single EnMAP-Box applications only
            * *light* environments contain python packages that are required to run most and all core EnMAP-Box applications
            * *ltr* environments use the current
              `QGIS Long Term release <https://qgis.org/resources/roadmap/#release-schedule>`_ instead of the
              latest (and newer) QGIS release that is available in conda.


            Use the *raw content* uri to download and install an EnMAP-Box conda environment from github.

            .. list-table::
               :header-rows: 1
               :widths: 15 10 70

               *  - Environment
                  - Size
                  - Path

               *  - `enmapbox_light`
                  - 4.58 GB
                  - https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_light.yml

               *  - `enmapbox_light_ltr`
                  - 4.65 GB
                  - https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_light_ltr.yml

               *  - `enmapbox_full`
                  - 6.46 GB
                  - https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_full.yml

               *  - `enmapbox_full_ltr`
                  - 6.90 GB
                  - https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_full_ltr.yml




         #. Activate the conda environment and start QGIS:

            .. code-block:: batch

               activate enmapbox
               qgis

        .. note::

            QGIS is developing rapidly. To keep an environment *<env_name>* up to date, call:

            .. code-block:: bash

                conda env update -n <env_name> --file=<env_name>.yml --prune

            To delete a conda environment, call:

            .. code-block:: bash

                conda env remove -n <env_name>



3. Install EnMAP-Box
====================

.. tabs::
   .. tab:: QGIS GUI

      **Install EnMAP-Box Plugin via the QGIS Plugin Manager**

      1. Start QGIS
      2. Go to Plugins -> Manage and Install Plugins
      3. Search for 'EnMAP-Box'
      4. Click on 'Install Plugin'

      .. figure:: /img/QgisGUI_InstallPlugin.gif
        :align: center

      **Activate Experimental Plugins (Optional)**
       5. Go to Plugins -> Manage and Install Plugins -> Settings
       6. Enable *Show also Experimental Plugins*

      .. figure:: /img/QgisGUI_Experimental.gif
        :align: center




   .. tab:: Command Line (Bash)

    The install the `qgis-plugin-manager <https://github.com/3liz/qgis-plugin-manager>`_ allows to install
    QGIS plugins like the EnMAP-Box from the command line:

    .. code-block:: bash

       **Install EnMAP-Box Plugin via the QGIS Plugin Manager**

       # define the path where your plugins are stored
       export QGIS_PLUGINPATH=~/.local/share/QGIS/QGIS3/profiles/default/python/plugins
       mkdir $QGIS_PLUGINPATH

       # install the 3Liz qgis-plugin-manager
       conda install qgis-plugin-manager
       qgis-plugin-manager init
       qgis-plugin-manager update

       # install the EnMAP-Box
       qgis-plugin-manger install 'EnMAP-Box 3'
















