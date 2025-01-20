



.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

Installation
============

The **EnMAP-Box** is a plugin for **QGIS** and requires additional **python packages**.

.. tabs::

   .. tab:: Windows

      **QGIS Installation on Windows**

      **Install QGIS via the official Standalone/OSGeo4W Installer**

         Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box.
         You can `get the QGIS Standalone Installer here <https://www.qgis.org/en/site/forusers/alldownloads.html#windows>`_.
         For beginners, we recommend using the standalone installers.
         More advanced QGIS users can use OSGeo4W installer.

         In case you already have the current QGIS LTR or LR version installed, you can skip this step.

         In case you have an outdated QGIS version, make sure to install a current version.


   .. tab:: Linux

     **QGIS Installation on Linux (Ubuntu)**

     The following instructions were written for and tested on Ubuntu (22.04 & 23.10). They should also work for other Debian-based distributions.

     **Install QGIS via the official repository**

       Install QGIS as described here https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu



   .. tab:: MacOS

     **QGIS Installation on MacOS**

     **Install QGIS.app**

       As of April 2024, the official QGIS.app from https://qgis.org/en/site/forusers/download.html
       still uses an outdated GDAL 3.2.2 (see https://github.com/EnMAP-Box/enmap-box/issues/858).

       Therefore, please use the installer provided by `OpenGIS.ch <https://www.opengis.ch/>`_ instead:

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


   .. tab:: Conda

      **Install QGIS via the Mambaforge Package Manager in Windows**

         It is recommended to use Miniforge, a minimal installer for Conda specific to conda-forge.
         You can `get the Miniforge Windows Installer here <https://conda-forge.org/miniforge/>`_.


      **Install QGIS via conda/mamba in Linux**

        It is recommended to use Micromamba, a minimal installer for conda/mamba.
        You can `get Micromamba here <https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html>`_. You may
        of course also use conda, just swap ``micromamba`` with ``conda`` in the instructions below.


      **Install QGIS via conda in MacOS**

         Install conda for macOS as described in https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html.
         It is recommended to use the Miniforge installer from https://github.com/conda-forge/miniforge/.




.. tabs::

   .. tab:: Windows

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

            Search for **h5py**, select the latest version and finish the installation.

         #. Open QGIS from the start menu.

   .. tab:: Linux

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

   .. tab:: MacOS

     **Install Python Dependencies**

       Install missing Python dependencies using the QGIS.app internal pip3.

       .. code-block:: bash

         /Applications/QGIS-3.36.app/Contents/bin/pip3 install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/macos/requirements_macos.txt

       .. note::
         This step needs to be repeated after updates to the QGIS.app.

   .. tab:: Conda

      **Install Python Dependencies in Windows**

         #. Open the Miniforge Prompt from the start menu.

            .. image:: /img/windows_start_miniforge.png

         #. Install QGIS LTR and EnMAP-Box Python dependencies into a new "enmapbox" environment:

            .. code-block:: batch

               mamba env create -n enmapbox -f https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml

         #. Activate the "enmapbox" environment and open QGIS by executing:

            .. code-block:: batch

               activate enmapbox
               qgis

      **Install Python Dependencies in Linux**

        #. Open the Terminal, and install QGIS LTR and EnMAP-Box Python dependencies into a new "enmapbox" environment:

          .. code-block:: bash

             curl -O https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml
             micromamba env create -n enmapbox -f ./enmapbox_full_longterm.yml
             rm -v ./enmapbox_full_longterm.yml

          .. note::

             There are `multiple environment files available <https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda>`_,
             depending on whether you want to install the latest QGIS version or the long-term release.

        #. Activate the created "enmapbox" environment and open QGIS by executing:

          .. code-block:: bash

             micromamba activate enmapbox
             qgis

      **Install Python Dependencies in MacOS**

         #. Open the Miniforge Prompt from the start menu.

            .. image:: /img/windows_start_miniforge.png

         #. Install QGIS and EnMAP-Box Python dependencies into a new "enmapbox" environment:

            .. code-block:: batch

               mamba env create -n enmapbox -f https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml

         #. Activate the "enmapbox" environment and open QGIS by executing:

            .. code-block:: batch

               activate enmapbox
               qgis







.. tabs::

   .. tab:: Plugin Installation
      .. tabs::
         .. tab:: QGIS GUI

            1. Call ``qgis&`` to open QGIS in an X-Window
            2. Go to Plugins -> Manage and Install Plugins
            3. Search for 'EnMAP-Box'
            4. Click on 'Install Plugin'

            .. figure:: /img/qgis_plugin_manager.png
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
