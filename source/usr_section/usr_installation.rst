.. include:: /icon_links.rst

.. |icon| image:: ../img/icon.png
   :width: 30px
   :height: 30px

.. |osgeoinstaller| image:: ../img/osgeoinstaller.png

.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

Installation
============

The **EnMAP-Box** is a plugin for **QGIS** and requires additional **python packages** that need to be installed independent from QGIS.

QGIS Installation on Windows
----------------------------

On a Windows system you have multiple options to install QGIS.

Option A: Install QGIS via the official Standalone/OSGeo4W Installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install QGIS
...............

Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box.
You can `get the QGIS Standalone Installer here <https://www.qgis.org/en/site/forusers/alldownloads.html#windows>`_.
For beginners, we recommend using the standalone installers.
More advanced QGIS users can use OSGeo4W installer.

In case you already have the current QGIS LTR or LR version installed, you can skip this step.

In case you have an outdated QGIS version, make sure to install a current version.

2. Install Python Dependencies
..............................

#. Close QGIS, if it is open.

#. Open the OSGeo4W Shell from the start menu.

   .. image:: /img/windows_start_osgeo.png

#. Install Python dependencies via PIP by executing:

   .. code-block:: batch

      pip install --upgrade --user -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/osgeo4w/requirements_osgeo4w.txt

#. (Optional) Install **HDF5** dependency via the OSGeo4W installer:

    The **HDF5** dependency is only required for importing PRISMA products.

    Start the OSGeo4W installer by executing:

    .. code-block:: batch

       setup

    Search for **h5py**, select the latest version and finish the installation.

#. Open QGIS from the start menu.

Option B: Install QGIS via the Mambaforge Package Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Miniforge
....................

It is recommended to use Miniforge, a minimal installer for Conda specific to conda-forge.
You can `get the Miniforge Windows Installer here <https://conda-forge.org/miniforge/>`_.

2. Install QGIS and Python Dependencies
.......................................

#. Open the Miniforge Prompt from the start menu.

   .. image:: /img/windows_start_miniforge.png

#. Install QGIS LTR and EnMAP-Box Python dependencies into a new "enmapbox" environment:

   .. code-block:: batch

      mamba env create -n enmapbox -f https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml

#. Activate the "enmapbox" environment and open QGIS by executing:

   .. code-block:: batch

      activate enmapbox
      qgis

|

QGIS Installation on Linux (Ubuntu)
-----------------------------------

The following instructions were written for and tested on Ubuntu (22.04 & 23.10). They should also work for other Debian-based
distributions.

Option A: Install QGIS via the official repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install QGIS
...............

Install QGIS as described here https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu

2. Install Python Dependencies
..............................

#. Open the Terminal (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`T`).

#. Make sure the following packages are installed using the system package manager:

   .. code-block:: console

      sudo apt install python3-pip python3-venv pyqt5-dev-tools

#. **(optional)** for some EnMAP-Box tools you may also need the following packages:

   .. code-block:: console

      sudo apt install python3-h5py python3-pyqt5.qtopengl python3-netcdf4

#. Open QGIS and the QGIS Python Console (:kbd:`Ctrl` + :kbd:`Alt` + :kbd:`P`). Type the following and confirm with enter:

   .. code-block:: python

      import sys; sys.executable

   It shows the path of the python executable QGIS is using, usually ``/usr/bin/python3``. It should be the same path as
   the command ``which python3`` executed in the Terminal returns! Close QGIS.

#. Create a `virtual python environment <https://docs.python.org/3/library/venv.html>`_ in a directory of your choice (e.g. ``~/.virtualenvs/enmapbox``):

   .. code-block:: console

      python3 -m venv --upgrade-deps --system-site-packages ~/.virtualenvs/enmapbox

#. Activate the environment:

   .. code-block:: console

      source ~/.virtualenvs/enmapbox/bin/activate

   Now you should see the environment name in brackets at the beginning of your prompt, e.g. ``(enmapbox)``.

#. Install missing python dependencies with pip inside the virtual environment:

   .. code-block:: console

      python3 -m pip install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/linux/requirements_ubuntu.txt

#. Start QGIS (from the activated environment, see 6.):

   .. code-block:: console

      qgis

.. hint::

   You can add a shortcut to your applications menu, so you do not have to open a Terminal and type
   the above mentioned commands (6. & 8.) everytime you want to start QGIS with the EnMAP-Box environment:

   Create the file :file:`~/.local/share/applications/enmapbox.desktop` with the following content (if you used another installation path
   in the instructions above change accordingly):

   .. code-block:: text

      [Desktop Entry]
      Name=QGIS (EnMAP-Box)
      Exec=/bin/bash -c "source ~/.virtualenvs/enmapbox/bin/activate && qgis %F"
      Terminal=false
      Icon=qgis
      Type=Application
      Categories=Education;Science;Geography;

|

.. _conda_linux:

Option B: Install QGIS via conda/mamba
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Micromamba
......................

It is recommended to use Micromamba, a minimal installer for conda/mamba.
You can `get Micromamba here <https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html>`_. You may
of course also use conda, just swap ``micromamba`` with ``conda`` in the instructions below.

2. Install QGIS and Python Dependencies
.......................................

#. Open the Terminal, and install QGIS LTR and EnMAP-Box Python dependencies into a new "enmapbox" environment:

   .. code-block:: bash

      curl -O https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml
      micromamba env create -n enmapbox -f ./enmapbox_full_longterm.yml
      rm -v ./enmapbox_full_longterm.yml

   .. note::

      There are `multiple environment files available <https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda>`_,
      depending on whether you want to install the latest qgis version or the long-term release.

#. Activate the created "enmapbox" environment and open QGIS by executing:

   .. code-block:: bash

      micromamba activate enmapbox
      qgis


|

QGIS Installation on MacOS
--------------------------

Option A: Install QGIS via the official installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


1. Install QGIS
...............

Install QGIS as described here https://www.qgis.org/

2. Install Python Dependencies
..............................

.. todo::

   Not tested yet! But you should be able to install all packages using the following command executed in the Terminal:

   .. code-block:: console

      /Applications/QGIS.app/Contents/MacOS/bin/pip3 install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/osgeo4w/requirements_osgeo4w.txt




Option B: Install QGIS via conda/mamba
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Instructions will be updated soon. Look for the :ref:`conda Linux instructions <conda_linux>` above, they should also work on Mac.

|

EnMAP-Box Plugin Installation
-----------------------------

#. In QGIS go to :menuselection:`Plugins --> Manage and Install Plugins --> All`
#. In the search bar enter ``enmap``
#. Now the EnMAP-Box should be listed in the plugin list:

   .. figure:: ../img/pluginmanager_all.png

   Select it and click :guilabel:`Install plugin` (or :guilabel:`Upgrade` in case you update to a new version)
#. The following dialog might pop up afterwards:

   .. image:: /img/plugin_dep_manager.png

   Depending on whether you want to use the GEE Time Series Explorer check |cb1| or uncheck |cb0| the checkbox
   and confirm with :guilabel:`OK`

#. Start the EnMAP-Box via the |icon| icon or from the menubar :menuselection:`Raster --> EnMAP-Box`
#. (Optional): You can download a demo dataset via :menuselection:`Project --> Load Example Data`

.. admonition:: Experimental version

   It is also possible to install the most recent develop version of the EnMAP-Box. To do so, make sure that the option
   |cb1| **Show also experimental plugins** is activated in the plugin manager settings. Once activated, there is an additional button
   :guilabel:`Install Experimental Plugin` in the plugin manager.

   .. image:: /img/experimental_install.png

   .. warning::

      As the *experimental* tag suggests, this version comes with the newest features and developments, but might also be prone to bugs and crashes.
