.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

############
Installation
############

The EnMAP-Box is a plugin for QGIS. It requires the QGIS Python API and various other Python packages.
Here we describe how you can install QGIS, the required python packages and the EnMAP-Box plugin.


.. _usr_installation_install_qgis:

Install QGIS
============

.. tabs::

   .. group-tab:: Windows

      **Install QGIS via the official Standalone/OSGeo4W Installer**

         Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box
         using the QGIS installer from https://www.qgis.org/en/site/forusers/alldownloads.html#windows.

         For beginners, we recommend using the standalone installers. More advanced QGIS users can use OSGeo4W installer,
         which eases updates of existing QGIS installation.

         In case you already have the current QGIS LTR or LR version installed, you can skip this step.

         In case you have an outdated QGIS version, make sure to install a current version.

      **Install Python Dependencies**

         #. Close QGIS, if it is open.

         #. Search for OSGeo4W setup from the start menu and run the installation.

         #. Now, Open the OSGeo4W Shell from the start menu.

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

         #. Open QGIS from the start menu. If you are running into Installation issues, check out the :ref:`faq` for help.


   .. group-tab:: Linux

     **Install QGIS on Linux**

      Install QGIS as described here https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu ,
      or follow the instructions for conda.

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

       **Install QGIS on MacOS**

       You can install QGIS using the standard official macOS installer (e.g., version 3.44 LTR) directly from the `QGIS Download Page <https://qgis.org/en/site/forusers/download.html>`_. Simply download the ``.dmg`` file, open it, and drag QGIS to your Applications folder.

       .. note::
          **When to use Conda instead:**
          Installing via the official QGIS ``.dmg`` covers all core EnMAP-Box functionalities (including Machine Learning algorithms and 3D visualization). However, if your workflow specifically requires the **EnMAP Processing Tool wrapper (** ``enpt-enmapboxapp`` **)**, we highly recommend using **Conda** (see the *Conda* tab).

          The internal Python environment in the macOS QGIS app restricts isolated package builds required by EnPT. Furthermore, Conda is generally recommended as it makes it significantly easier to manage, update, and resolve complex geospatial dependencies over time.

       **Install Python Dependencies**

       Modern QGIS installations on macOS embed Python deeply within the application framework, meaning traditional terminal commands (like calling ``pip3`` from the ``bin`` folder) are no longer reliable. To safely install dependencies to the correct environment, you must execute the installation directly from within QGIS.

       1. Launch QGIS.
       2. Navigate to **Plugins** ‣ **Python Console** in the top menu bar.
       3. Copy the script below, paste it into the console prompt (``>>>``), and press **Enter**:

       .. code-block:: python

          import sys
          import os
          import runpy

          # 1. Manually create the missing 'bin' directory so pip stops crashing
          broken_bin_path = "/Applications/QGIS.app/Contents/Frameworks/bin"
          os.makedirs(broken_bin_path, exist_ok=True)

          print("Created missing bin directory. Finishing installation...")

          original_argv = sys.argv
          enmap_packages = [
              "colorama", "astropy", "PyOpenGL", "xgboost", "lightgbm",
              "catboost", "sympy", "numba>=0.57", "scikit-learn>=1.0"
          ]

          # 2. run pip with a flag to silence the script warnings
          sys.argv = ["pip", "install", "-U", "--no-warn-script-location"] + enmap_packages

          try:
              runpy.run_module("pip", run_name="__main__")
          except SystemExit:
              pass
          except Exception as e:
              print(f"An error occurred: {e}")
          finally:
              sys.argv = original_argv
              print("=========================================")
              print("All packages are now fully installed!")
              print("You can safely activate EnMAP-Box 3.")
              print("=========================================")

       4. Wait for the packages to download and compile. Once the console prints the success message, you can close the Python Console.
       5. Go to **Plugins** ‣ **Manage and Install Plugins...**, search for **EnMAP-Box 3**, and check the box to activate it.

   .. group-tab:: Conda

      .. _usr_installation_qgis_conda:

      **Install QGIS with conda (cross-platform)**

          Conda is a cross-platform package manager that allows to install software in separated environments. We recommend
          installing conda using `Miniforge <https://conda-forge.org/download>`__, a minimal installer which
          by default installs conda packages from the `conda-forge <https://conda-forge.org/>`_ channel.

          *Linux / Unix / MacOS:*

              .. code-block:: bash

                # download install script
                curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

                # run install script
                sh Miniforge3-$(uname)-$(uname -m).sh

          *Windows:*

                Download and run the miniforge installer from https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe


          When done, continue with the installation of QGIS and python dependencies in conda below.

      **Install a python environment for the EnMAP-Box**


         1. Open the `Miniforge <https://conda-forge.org>`__ prompt
              .. image:: /img/windows_start_miniforge.png


         2. Ensure to use the libmamba solver.

            To significantly speed up the environment creation, it is highly recommended to use the ``libmamba`` solver.
            First, check which solver is used::

                conda config --show solver

            If the used is not *libmamba*, you can install it with the following commands::

                 conda update -n base conda
                 conda install -n base conda-libmamba-solver
                 conda config --set solver libmamba

            For more details, see the `Anaconda blog post <https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community>`_ on this topic.

         2. Install QGIS and python dependencies, using one of the conda environment files (`enmapbox_*.yml`) from
            https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda, e.g.

            .. code-block:: batch

                conda env create -n enmapbox --file=https://raw.githubusercontent.com/EnMAP-Box/enmap-box/refs/heads/main/.env/conda/enmapbox_full.yml

            ``--file=<uri>`` specifies the path to the \*.yml file that defines the environment.

            ``-n <name>`` or ``--name <name>`` can be used to change the environment name.

            The environment files provided for download vary by used QGIS release and python packages to be:

            * *full* environments contains *all* python packages, including those used by single EnMAP-Box applications only
            * *light* environments contain python packages that are required to run most and all core EnMAP-Box applications
            * *ltr* environments use the current
              `QGIS Long Term release <https://qgis.org/resources/roadmap/#release-schedule>`_ instead of the
              latest (and newer) QGIS release that is available in conda.


            Use the *raw content* url to download and install an EnMAP-Box conda environment from github.

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

         3. Activate the conda environment and start QGIS:

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

Install EnMAP-Box
=================

.. tabs::

   .. tab:: QGIS GUI

      **Install EnMAP-Box Plugin via the QGIS Plugin Manager**

      1. Start QGIS
      2. Go to Plugins -> Manage and Install Plugins
      3. Search for 'EnMAP-Box'
      4. Click on 'Install Plugin'

      .. figure:: /img/QgisGUI_InstallPlugin.gif
        :align: center
        :width: 100%

      **Activate Experimental Plugins (Optional)**
       5. Go to Plugins -> Manage and Install Plugins -> Settings
       6. Enable *Show also Experimental Plugins*

      .. figure:: /img/QgisGUI_Experimental.gif
        :align: center
        :width: 120%

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
