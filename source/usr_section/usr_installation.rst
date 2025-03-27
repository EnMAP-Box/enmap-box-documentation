



.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

############
Installation
############

The EnMAP-Box is a plugin for QGIS. It required the QGIS python API and various other python packages.
Here we describe how you can install QGIS, the required python packages and the EnMAP-Box plugin.

1. Install QGIS
===============

.. tabs::

   .. group-tab:: Windows

      **Install QGIS via the official Standalone/OSGeo4W Installer**

         Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box.
         You can `get the QGIS Standalone Installer here <https://www.qgis.org/en/site/forusers/alldownloads.html#windows>`_.

         For beginners, we recommend using the standalone installers. More advanced QGIS users can use OSGeo4W installer,
         which eases updates of existing QGIS installation.

         In case you already have the current QGIS LTR or LR version installed, you can skip this step.

         In case you have an outdated QGIS version, make sure to install a current version.


   .. group-tab:: Linux

     **Install QGIS on Linux**

     The following instructions were written for and tested on Ubuntu (22.04 & 24.04). They should also work for other Debian-based distributions.

     Install QGIS as described here https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu


   .. group-tab:: MacOS

      **Install QGIS on MacOS**

      *Note*

      As of March 2025, the official QGIS.app from https://qgis.org/en/site/forusers/download.html
      still uses Python 3.9 and GDAL 3.2.2 (see https://github.com/EnMAP-Box/enmap-box/issues/858).
      Various EnMAP-Box components and Python packages used by them now require newer versions of GDAL and Python.

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

   .. _usr_installation_qgis_conda:
   .. group-tab:: Conda

      **Install QGIS with conda (cross-platform)**

      Conda is a cross-platform package manager that allows install software in separated environments.

      It is recommended to use Miniforge, a minimal installer for conda specific to the
      `conda-forge<https://conda-forge.org/>`_ channel.

      You can get the Miniforge Installer here <https://conda-forge.org/download/>`_.


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

         Do not-update packages like numpy or GDAL with pip. This will break the QGIS application.

   .. group-tab:: Conda

         **Install a python environment for the EnMAP-Box**

         #. Open the Miniforge Prompt from the start menu.

            .. image:: /img/windows_start_miniforge.png

         #. Select the uri of a conda environment from https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda
            that you like to install for running the EnMAP-Box:

            .. list-table::
               :header-rows: 1

               *  - Name
                  - Size
                  - Notes
                  - Path

               *  - `enmapbox_light_latest.yml`
                  -
                  - QGIS Latest Release (LR) with python dependencies core/most EnMAP-Box applications
                  - https://github.com/EnMAP-Box/enmap-box/blob/main/.env/conda/enmapbox_light_latest.yml

               *  - `enmapbox_light_longterm.yml`
                  -
                  - QGIS Latest Release (LTR) with python dependencies core/most EnMAP-Box applications
                  - https://github.com/EnMAP-Box/enmap-box/blob/main/.env/conda/enmapbox_light_longterm.yml

               *  - `enmapbox_full_longterm`
                  -
                  - QGIS Long Term Release (LTR) with python dependencies for all EnMAP-Box applications
                  - https://github.com/EnMAP-Box/enmap-box/blob/main/.env/conda/enmapbox_full_longterm.yml

               *  - `enmapbox_full_latest.yml`
                  -
                  - QGIS Latest Release (LR) with python dependencies for all EnMAP-Box applications
                  - https://github.com/EnMAP-Box/enmap-box/blob/main/.env/conda/enmapbox_full_latest.yml



         #. Install the selected conda environment, e.g.

            .. code-block:: batch

               mamba env create -n enmapbox --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml

         #. Activate the "enmapbox" environment and open QGIS by executing:

            .. code-block:: batch

               activate enmapbox
               qgis


3. Install EnMAP-Box
====================

.. tabs::
   .. tab:: QGIS GUI

      **Install EnMAP-Box Plugin via the QGIS Plugin Manager**

      1. Call ``qgis&`` to open QGIS in an X-Window
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




















.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |cb0| image:: /img/icons/cb0.png
   :width: 28px
.. |cb1| image:: /img/icons/cb1.png
   :width: 28px
.. |icon| image:: /img/icon.png
   :width: 30px
