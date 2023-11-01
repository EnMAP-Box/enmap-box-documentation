.. include:: /icon_links.rst

.. |icon| image:: ../img/icon.png
   :width: 30px
   :height: 30px

.. |osgeoinstaller| image:: ../img/osgeoinstaller.png

.. |download_link| raw:: html

   <a href="https://plugins.qgis.org/plugins/enmapboxplugin/" target="_blank">https://plugins.qgis.org/plugins/enmapboxplugin/</a>

.. _usr_installation:

Installation (NEW)
==================

The **EnMAP-Box** is a plugin for **QGIS** and requires additional **python packages** that need to be installed independent from QGIS.

QGIS Installation on Windows
----------------------------

On a Windows system you have multiple options to install QGIS.

Option A: Install QGIS via OSGeo4W
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install QGIS
...............

Install either the current QGIS Long Term Release (LTR) or the current QGIS Latest Release (LR) to run the latest EnMAP-Box.
You can `get the QGIS MSI Installer here <https://www.qgis.org/en/site/forusers/download.html>`_.
It is recommended to use the MSI installer, instead of the Network Installer.

In case you already have the current QGIS LTR or LR version installed, you can skip this step.

In case you have an outdated QGIS version, make sure to reinstall.

2. Install Python Dependencies
..............................

#. Close QGIS, if it is open.

#. Open the OSGeo4W Shell from the start menu.

   .. image:: /img/windows_start_osgeo.png

#. Install Python dependencies by executing:

   .. code-block:: batch

      pip install --upgrade --user -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/requirements_osgeo4w.txt

#. Open QGIS from the start menu.

Option B: Install QGIS via Mambaforge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

QGIS Installation on Linux
--------------------------

todo @jakimow

QGIS Installation on MacOS
--------------------------

todo @jakimow

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
