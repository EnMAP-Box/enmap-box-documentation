

.. include:: /dev_section/external_links.rst



.. _faq:

=====================
FAQ & Troubleshooting
=====================


Bug report & feedback
=====================

.. note:: Your feedback is more than welcome! In case you encounter any problems with the EnMAP-Box or have
          suggestions of any kind for improving it (or this documentation), please let us know!

          **Please report issues** `here <https://github.com/EnMAP-Box/enmap-box/issues/new>`__

          **For questions use** `GitHub Discussions <https://github.com/EnMAP-Box/enmap-box/discussions>`__

Contact
=======

**E-Mail:** enmapbox@enmap.org


**Newsletter**: Subscribe to the EnMAP mailing list to be informed about new EnMAP-Box releases and other EnMAP related news.
Click `here <https://www.enmap.org/contact/>`_ for more information.

.. _citation_enmapbox:

Citation
========

Please cite the EnMAP-Box as:

.. code-block:: none

   Jakimow, B., Janz, A., Thiel, F., Okujeni, A., Hostert, P., van der Linden, S., 2023. EnMAP-Box:
   Imaging spectroscopy in QGIS. SoftwareX 23, 101507. https://doi.org/10.1016/j.softx.2023.101507

BibTeX:

.. code-block:: latex

   @article{JAKIMOW2023101507,
   title = {EnMAP-Box: Imaging spectroscopy in QGIS},
   journal = {SoftwareX},
   volume = {23},
   pages = {101507},
   year = {2023},
   issn = {2352-7110},
   doi = {10.1016/j.softx.2023.101507},
   url = {https://doi.org/10.1016/j.softx.2023.101507},
   author = {Benjamin Jakimow and Andreas Janz and Fabian Thiel and Akpona Okujeni and Patrick Hostert and van der Linden, Sebastian}
   }


.. For the general idea behind the EnMAP-Box please refer to:
..
.. .. code-block:: none
..
..    van der Linden, S., Rabe, A., Held, M., Jakimow, B., Leitão, P., Okujeni, A., Schwieder, M., Suess, S., Hostert, P., 2015.
..    The EnMAP-Box—A Toolbox and Application Programming Interface for EnMAP Data Processing.
..    Remote Sensing 7, 11249–11266. https://doi.org/10.3390/rs70911249

|

FAQ
===

This is a list of Frequently Asked Questions about the EnMAP-Box. Feel free to
suggest new entries!

.. _faq_no_pip:

* **Installation: no module named pip**

  In case you run into problems during installation because pip is not available in your python environment
  (error message ``C:/.../python3.exe: No module named pip`` or similar), follow these steps (Windows):

  Start the OSGeo4W installer from the OSGeo4W Shell by calling

  .. code-block:: batch

     setup

  .. image:: ../img/shell_setup.png

  which will open the OSGeo4W Setup dialog.

  Now navigate through the first pages of the dialog, by selecting the following settings:

  * Advanced Installation :guilabel:`Next`
  * Installation from Internet :guilabel:`Next`
  * default OSGeo4W root directory :guilabel:`Next`
  * local temp directory :guilabel:`Next`
  * direct connection :guilabel:`Next`
  * Select downloadsite ``https://download.osgeo.org`` :guilabel:`Next`

  Then use the textbox to filter, select and install the following packages (see video below for help):

  * python3-pip
  * python3-setuptools


  Click on the |osgeoinstaller| symbol once, which should usually change the *Skip* setting to installing the most recent
  version.

  Only **AFTER** having selected both packages, click :guilabel:`Next`.

  .. raw:: html

     <div><video width="90%" controls muted><source src="../_static/videos/osgeo_install_short.webm" type="video/webm">Your browser does not support HTML5 video.</video>
     <p><i>Demonstration of package selection in the Setup</i></p></div>

  Click :guilabel:`Finish` when the installation is done.

....

.. _faq_numba:

* **Installation: error ensomap / numba / TypeError jitdebug**

  EnSoMAP requires `Numba`_, a JIT compiler that translates python code into fast machine code.
  Unfortunately, Numba is not part of a standard QGIS installation. Installing it afterwards can be tricky,
  in particular on the standard Windows and macOS QGIS installations.
  If you want to use EnSoMAP and numba, we therefore recommend to use a QGIS that was installed with `Conda`_ instead.

  1.  Install conda and create a conda environment with QGIS
      :ref:`as described here<dev_installation_create_conda_qgis>`.
  2.  Install Numba

      .. code-block:: batch

          (qgis_stable) $>conda install numba --channel=conda-forge

  3.  Start the conda QGIS by:

      .. code-block:: batch

          (qgis_stable) $>qgis
  4.  If not already done, install the EnMAP-Box to your Conda-QGIS with the QGIS Plugin Manager.

....

* **Image Cube tool missing qtopengl / Missing OpenGL / QtOpenGL packages**

  On some systems we experiences problems related to a missing OpenGL support (e.g `Issue #299 <https://bitbucket.org/hu-geomatics/enmap-box/issues/299/image-cube-qt-issues-on-linux>`_)

  1. Ensure that you have installed OpenGL drivers that support your graphic card
  2. Ensure that `PyOpenGL <https://pyopengl.sourceforge.net>`_  is installed (``python3 -m pip install PyOpenGL``).

  On Linux, it might be necessary to install the Python bindings for QtOpenGL in order to start the Image Cube tool.

  .. code-block:: bash

     sudo apt install python3-pyqt5.qtopengl

....

* **Exception: Unable to find full path for "dockpanel.ui". Make its directory known to UI_DIRECTORIES**

  It's likely that an update of the EnMAP-Box plugin failed to remove a previous version properly.
  The following workaround might help:

  1. Navigate into the active QGIS profile folder. It can be opened via :menuselection:`Settings -->  User Profiles --> Open Active Profile Folder`
  2. Close QGIS. This is necessary to avoid any file handles on files or folders of the EnMAP-Box plugin.
  3. Delete the EnMAP-Box plugin folder manually, e.g. :file:`default/python/plugins/enmapboxplugin` if the active QGIS profile is *default*.
  4. Restart QGIS and install the most-recent EnMAP-Box version

|

Known Issues
============

Here is a list of known issues, that aren't fixed easily,
and/or only affect a specific version of QGIS or operating system:

* https://github.com/EnMAP-Box/enmap-box/labels/known%20issue
* Historic (old repository): https://bitbucket.org/hu-geomatics/enmap-box/issues?component=known+issue&status=on+hold





.. Substitutions definitions - AVOID EDITING PAST THIS LINE
   This will be automatically updated by the find_set_subst.py script.
   If you need to create a new substitution manually,
   please add it also to the substitutions.txt file in the
   source folder.

.. |osgeoinstaller| image:: /img/osgeoinstaller.png
