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

.. raw:: html

   <div style="text-align: center;">
   <iframe width="100%" height="380" src="https://www.youtube-nocookie.com/embed/_SNbLmB8aCQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   <p><i>Video with step by step installation instructions</i></p>
   </div>


1. Install QGIS
---------------


Install QGIS version 3.26 or higher to run the EnMAP-Box.
You can `get QGIS here <https://www.qgis.org/en/site/forusers/download.html>`_.
Additional information on the installation process is provided in the `QGIS Documentation <https://www.qgis.org/en/site/forusers/alldownloads.html>`_.

In case you already have QGIS installed, you can skip this step.


MacOS
~~~~~

Before you can install QGIS from the downloaded disk image, you need to allow your macOS to install it:

1. Download the official all-in-one, signed installer `here <https://www.qgis.org/en/site/forusers/download.html>`_.

2. Extract the downloaded `qgis-macos-pr.dmg` and move it to your app folder

   |mac_copy1| |mac_copy2|

.. |mac_copy1| image:: /img/macos/install_qgis_copy1.png
   :width: 500px
.. |mac_copy2| image:: /img/macos/install_qgis_copy2.png
   :width: 500px

3. Installing or opening QGIS may raise a verification warning. In that case, open your system preferences, go to
   :menuselection:`Security & Privacy --> General` and allow QGIS to be opened anyway.

   |mac_check1| |mac_check2|

.. |mac_check1| image:: /img/macos/install_qgis_check1.png
   :width: 500px
.. |mac_check2| image:: /img/macos/install_qgis_check2.png
   :width: 500px

4. Now you can start QGIS.app from your application folder.

|

.. _install-python-packages:

2. Install required python packages
-----------------------------------

The EnMAP-Box plugin requires several python packages (click
`here <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/requirements.txt>`_ here for full list).
In the following we demonstrate two variants for installing the required packages (you **don't** have to do both!):

.. _package_installer:

2.1 Package Installer
~~~~~~~~~~~~~~~~~~~~~

The EnMAP-Box includes a Package Installer that offers a more or less one-click solution to install required python packages.
It can be accessed from the menu bar via :menuselection:`Project --> Package Installer`.

If you start the EnMAP-Box for the first time, you may see a warning.
The Package Installer can also be opened by clicking :guilabel:`Install Missing`.

.. image:: /img/warning_missing_packages.png

Use the :guilabel:`Yes to All` button to install all required python packages. Per default, this will install packages using pip into
the user directory (as this does not require admin rights). It is also possible to install/update packages individually via
the context menu inside the package list.

.. image:: /img/package_installer.png

It might be necessary to restart QGIS and the EnMAP-Box.

|

2.2 Command-line
~~~~~~~~~~~~~~~~

In case the :ref:`Package Installer <package_installer>` does not work for you or you do not want to use it,
try installing the packages from the command-line. This variant may be more reliable. See OS specific instructions below:

.. _install-packages-windows:

Windows
*******


1. Close QGIS, if it is open.

2. Run the OSGeo4W Shell as administrator, if possible. A convenient way to access the OSGeo4W Shell is from the start menu.
   Depending on the installation method you used to install QGIS, the shortcut will be listed under *QGIS 3.xx* (standalone installer)
   or *OSGeo4W* (network installer)

   Hold :kbd:`Ctrl` + :kbd:`Shift` and click on the OSGeo4W Shell entry (or right-click and choose *Run as administrator*)

   .. image:: /img/windows_start_osgeo.png

3. Activate the Python 3 environment by entering:


   .. code-block:: batch

      py3_env

   .. image:: ../img/shell_callpy3env.png

   .. note:: In more recent versions of QGIS the ``py3_env`` call might not be necessary or will simply not work. If so, just continue with the following step (4).


4. Install required python packages by entering:

   .. code-block:: batch

      python3 -m pip install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/requirements.txt


   Now all packages will be installed automatically. After completion, the shell should show something like this:

   .. image:: ../img/shell_install_output.png

   If the package installation was successful, you can close the shell. The required packages are installed now and
   you can continue to start/install the EnMAP-Box.

   .. error::

      In case you run into problems because pip is not available in your python environment
      (error message ``C:/.../python3.exe: No module named pip`` or similar), :ref:`follow these steps... <faq_no_pip>`

|

.. _install-packages-linux:

Linux
*****

1. Close QGIS, if it is open.
2. Open the terminal and install all missing packages using pip:

   .. code-block:: bash

      python3 -m pip install -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/requirements.txt

   .. hint:: Make sure to execute the pip command in the python environment QGIS is using (usually you can find out where
             python is located by running ``import sys; sys.executable`` in the QGIS Python Console). You then might have
             to change the ``python3`` part in the snippet below with the explicit QGIS python path.

             This also applies if you installed QGIS using **flatpak**, in that case install python modules as described `here <https://qgis.org/de/site/forusers/alldownloads.html#flatpak>`_.

   .. note::

      You might also consider to create a virtual environment (``python3 -m venv``), install the packages as described, set
      ``system-site-packages = true`` in the ``pyvenv.cfg``, activate this virtual environment and start ``qgis`` from there.
|

.. _install-packages-mac:

Mac
***

To install single python packages like the astropy package, open the Terminal and call::

   /Applications/QGIS.app/Contents/MacOS/bin/pip3 install -U astropy

Use ``-U`` or ``--update`` to update older package version.

To install all packages required, call::

   /Applications/QGIS.app/Contents/MacOS/bin/pip3 install -U -r https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/requirements.txt


More details on the QGIS packaging mechanism for macOS can be found `here <https://www.lutraconsulting.co.uk/blog/2020/10/01/qgis-macos-package/>`_.

|

.. error::

   See :ref:`FAQ <faq_requirements>` if you run into problems installing the packages.

|

.. _usr_installation_enmapbox:

3. Install or update the EnMAP-Box
----------------------------------


Install from QGIS plugin repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Open QGIS and go to :menuselection:`Plugins --> Manage and Install Plugins --> All`
#. In the search bar enter ``enmap`` or ``EnMAP-Box 3``
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


Install older version
~~~~~~~~~~~~~~~~~~~~~

#. Go to the QGIS Python Plugins Repository |download_link|
#. Click on the **Versions** tab to see all available version.
#. Click on the desired version and on the next page click |download|
#. It is recommended to uninstall previous EnMAP-Box versions (delete folder manually, or in QGIS via
   :menuselection:`Plugins --> Manage and Install Plugins --> Installed --> EnMAP-Box 3 --> Uninstall plugin`)
#. Open :menuselection:`Plugins --> Manage and Install Plugins --> Install from ZIP`.
#. Press :guilabel:`...` and select the downloaded zip file
   (:file:`enmapboxplugin.3.x.YYYYMMDDTHHMM.QGIS3.zip`) and click :guilabel:`Install plugin`.
#. Start the EnMAP-Box via the |icon| icon or from the menubar :menuselection:`Raster --> EnMAP-Box`.

.. |download| image:: ../img/qgis_download_button.png


|

