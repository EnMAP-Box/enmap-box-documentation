.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

############
Installation
############

The Installation section explains how to set up EnMAP‑Box as a QGIS plugin on your computer. It guides you through installing a compatible
QGIS version, preparing the required Python environment, and then adding EnMAP‑Box via the QGIS
Plugin Manager or from a specific release.


.. _usr_installation_install_qgis:

1. QGIS and Python Dependencies
===============================

.. tabs::

   .. group-tab:: Windows

      **Install QGIS via the official Standalone/OSGeo4W Installer**

         Install the current QGIS 3.44 LTR to run the latest EnMAP-Box
         using the QGIS installer from https://www.qgis.org/en/site/forusers/alldownloads.html#windows.

         For beginners, we recommend using the standalone installers. More advanced QGIS users can use OSGeo4W installer,
         which eases updates of existing QGIS installation.

         In case you have an outdated QGIS, make sure to install a current version (3.44).

      **Install Python Dependencies**

         #. Close QGIS, if it is open.

         #. Search for OSGeo4W shell from the start menu. In case the OSgeo4W does not exists,
            run the Setup to install it.

            .. image:: /img/installation_osgeo4w_executables.png

            .. image:: /img/windows_start_osgeo.png

         #. Open the OSGeo4 shell and to install Python dependencies using PIP:

            .. code-block:: batch

               pip install --upgrade --user -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/osgeo4w/requirements_osgeo4w.txt

            .. note::

              In rare cases, the user folder may contain wrongly installed packages,
              which are interfering with the package version managed by OSGeo4W, e.g. numpy, scipy or gdal.
              Wrongly installed packages can be deleted manually from the user folder.

              To locate the user folder used by your QGIS instance, run the following inside your QGIS Python console::

                 >>> import site
                 >>> print(site.USER_SITE)
                 C:\Users\<user name>\AppData\Roaming\Python\Python39\site-packages

         #. Open QGIS from the start menu. If you are running into Installation issues, check out the :ref:`faq` for help.


   .. group-tab:: Linux

      .. warning::

         The Linux bare-metal installation uses the operating-system QGIS and Python environment.
         This is useful when you want a native QGIS installation without conda, but it is less isolated
         than the Conda setup. If dependency versions become difficult to resolve, use the *Conda* tab.

      **Install QGIS on Linux (bare-metal / apt)**

      The commands below install the QGIS 3.44 LTR packages on Ubuntu. For Debian, use the
      corresponding ``https://qgis.org/debian-ltr`` repository and Debian suite name.

      #. Open the Terminal (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`T`).

      #. Install the packages needed to add the QGIS package repository:

         .. code-block:: console

            sudo apt update
            sudo apt install ca-certificates gnupg wget
            sudo install -d -m 0755 /etc/apt/keyrings
            sudo wget -qO /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg

      #. Add the QGIS LTR repository. Use ``noble`` for Ubuntu 24.04 and ``jammy`` for Ubuntu 22.04.

         .. code-block:: console

            sudo tee /etc/apt/sources.list.d/qgis.sources >/dev/null <<'EOF'
            Types: deb deb-src
            URIs: https://qgis.org/ubuntu-ltr
            Suites: noble
            Architectures: amd64
            Components: main
            Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
            EOF

      #. Install QGIS and PyQGIS:

         .. code-block:: console

            sudo apt update
            sudo apt install qgis python3-qgis qgis-plugin-grass

      **Install Python Dependencies**

      #. Install the system packages required by common EnMAP-Box workflows:

         .. code-block:: console

            sudo apt install python3-pip python3-venv pyqt5-dev-tools python3-matplotlib

      #. **(Optional)** For some EnMAP-Box tools you may also need the following packages:

         .. code-block:: console

            sudo apt install python3-h5py python3-pyqt5.qtopengl python3-netcdf4

      #. Install the remaining EnMAP-Box Python dependencies into your user Python site:

         .. code-block:: console

            python3 -m pip install --user --upgrade --ignore-installed -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/linux/requirements_ubuntu.txt || \
            python3 -m pip install --user --upgrade --ignore-installed --break-system-packages -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/linux/requirements_ubuntu.txt

         On Ubuntu 24.04, pip may require ``--break-system-packages`` for user-site installs because
         the system Python environment is externally managed.

      #. Verify that QGIS uses the same Python installation:

         .. code-block:: console

            python3 -c "from qgis.core import Qgis; print(Qgis.QGIS_VERSION)"

      #. Start QGIS:

         .. code-block:: console

            qgis

   .. group-tab:: MacOS

       .. warning::

          The internal Python environment in macOS QGIS.app's restricts isolated package builds, but these
          are required by EnMAP-Box applications like the **EnMAP Processing Tool (EnPT)**.

          We therefore recommend to install QGIS and the Python dependencies required to run
          the EnMAP-Box using **Conda (see the *Conda* tab)**.
          This is significantly easier to manage, update, and resolve QGIS and dependency versions over time.


       **Install QGIS on MacOS**

       Install QGIS using the official macOS installer (e.g., version 3.44 LTR) from the `QGIS Download Page <https://qgis.org/en/site/forusers/download.html>`_. Download the ``.dmg`` file, open it, and drag QGIS to your Applications folder.


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

   .. group-tab:: Conda

      .. _usr_installation_qgis_conda:

      **Install QGIS and Python dependencies with conda (cross-platform)**

      Conda is a cross-platform package manager that allows to install software in separated environments.
      We recommend to install and use `Miniforge <https://conda-forge.org/download>`__, a minimal conda installer specific to
      packages from `conda-forge <https://conda-forge.org/>`_ channel. It contains a meta-package for packages needed by the EnMAP-Box https://anaconda.org/channels/conda-forge/packages/enmapbox

      ..
          *Linux / Unix / MacOS:*

              .. code-block:: bash

                # download install script
                curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

                # run install script
                sh Miniforge3-$(uname)-$(uname -m).sh

          *Windows:*

                Download and run the miniforge installer from https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe

      1. Open a conda terminal and create a conda environment that contains QGIS and all required packages.

         a) Use the **enmapbox** recipe to install packages required to run the EnMAP-Box, including EnPT, EnFROSP, SpecDeepMap

            .. code-block:: bash

               conda create -n enmapbox -c conda-forge enmapbox

         b) Use the **enmapbox-lite** recipe to install packages required to run the EnMAP-Box and *most* machine-learning applications

            .. code-block:: bash

               conda create -n enmapbox -c conda-forge enmapbox-lite


      2. Activate the conda environment and start QGIS:

        .. code-block:: batch

          conda activate enmapbox
          qgis

      .. note::

            QGIS, GDAL and other packages are developing rapidly. To keep an environment *<env_name>* up to date, call:

            .. code-block:: bash

                conda activate <env_name>
                (<env_name>) conda update --all

            To delete a conda environment, call:

            .. code-block:: bash

                conda env remove -n <env_name>

            To use a specific package version, call ``conda install <package>=<version>``.
            Such a step may require an update of various other packages. For example to use a specific QGIS version, call:

            .. code-block:: bash

                conda activate <env_name>
                (<env_name) conda install qgis=3.40

2. Install EnMAP-Box
====================

.. tabs::

   .. tab:: QGIS Plugin Manager

      **Install EnMAP-Box Plugin via the QGIS Plugin Manager**

      1. Start QGIS.
      2. Go to **Settings** ‣ **User Profiles** ‣ **New Profile...** and create a profile named ``EnMAP-Box``.
      3. Restart QGIS in the ``EnMAP-Box`` profile if QGIS does not switch automatically.
      4. Go to **Plugins** ‣ **Manage and Install Plugins**.
      5. Search for ``EnMAP-Box``.
      6. Click **Install Plugin**.

      .. figure:: /img/QgisGUI_InstallPlugin.gif
        :align: center
        :width: 100%

      **Activate Experimental Plugins (Optional)**

      #. Go to **Plugins** ‣ **Manage and Install Plugins** ‣ **Settings**.
      #. Enable **Show also Experimental Plugins**.

      .. figure:: /img/QgisGUI_Experimental.gif
        :align: center
        :width: 120%

   .. tab:: Command Line (Bash)

      The `qgis-plugin-manager <https://github.com/3liz/qgis-plugin-manager>`_ allows you to install
      QGIS plugins like EnMAP-Box from the command line. The commands below create a dedicated
      QGIS profile named ``EnMAP-Box`` and install the plugin into that profile.

      .. code-block:: bash

         export QGIS_PROFILE="EnMAP-Box"
         export QGIS_PROFILE_HOME="${HOME}/.local/share/QGIS/QGIS3/profiles/${QGIS_PROFILE}"
         export QGIS_PLUGINPATH="${QGIS_PROFILE_HOME}/python/plugins"
         export PATH="${HOME}/.local/bin:${PATH}"

         mkdir -p "${QGIS_PLUGINPATH}" "${QGIS_PROFILE_HOME}/QGIS"

         python3 -m pip install --user --upgrade --ignore-installed qgis-plugin-manager || \
         python3 -m pip install --user --upgrade --ignore-installed --break-system-packages qgis-plugin-manager

         qgis-plugin-manager init --qgis-version 3.44 --update
         qgis-plugin-manager install "EnMAP-Box 3" --upgrade --fix-permissions

         printf '[PythonPlugins]\nenmapboxplugin=true\n' \
           | tee "${QGIS_PROFILE_HOME}/QGIS/QGIS.ini" "${QGIS_PROFILE_HOME}/QGIS/QGIS3.ini" > /dev/null

         qgis --profile "${QGIS_PROFILE}"
