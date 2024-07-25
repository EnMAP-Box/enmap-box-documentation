EnMAP-Box repository
####################

The EnMAP-Box source code is hosted in a Git repository at https://github.com/EnMAP-Box/enmap-box

.. _dev_enmapox_repo_structure:

Structure
=========

Overview
--------

The repository contains the following files and folders:

=============================== ========================================================================================
Folder/File                     Purpose
=============================== ========================================================================================
doc/                            EnMAP-Box Sphinx *.rst documentation
``doc_*``                       Deprecated doc folders (will be removed)
enmapbox/                       EnMAP-Box source code
enmapboxtesting/                Unit tests
scripts/                        Scripts to maintain the repository and build the EnMAP-Box QGIS Plugin
examples/                       Code examples how to use the EnMAP-Box API
examples/minimumexample/        Exemplary EnMAP-Box Application
site-packages/                  Other python libraries the EnMAP-Box depends on
snippets/                       Small source code snippets.
CHANGELOG
LICENCE.txt
LICENCE.md
README.md
__init__.py
CONTRIBUTORS.md
index.html
requirements.txt
requirements_developer.txt
setup.py                        required for read-the-docs installation
.gitignore                      defines files that should be ignored by the repository
.gitattributes                  defines binary files that are stored with git-lfs
.readthedocs.yml

=============================== ========================================================================================

Scripts for Developers
----------------------

The ``scripts`` directory contains scrips to support developers. Ensure that this folder is part of your python path, e.g add
it as source in your PyCharm project (left-mouse, mark directory as source):

===================================== ==========================================================================================================================================
Script                                Purpose
===================================== ==========================================================================================================================================
``scripts/setup_repository.py``       Creates resource files etc. required to test the EnMAP-Box by calling other scripts
``scripts/create_plugin.py``          Create the EnMAP-Box Plugin ZIP file.
``scripts/create_plugin.py``          Create the two shell-scripts ``runtests.bat`` and ``runtests.sh`` to run unit tests.
``scripts/install_testdata.py``       Downloads and installs the EnMAP-Box testdata and qgisresources
``scripts/compile_resourcefiles.py``  Complies EnMAP-Box resources (*.svg, *.png) into *_rc.py files
``scripts/iconselect.py``             Opens a browser to show EnMAP-Box and QGIS resources, e.g. icons
===================================== ==========================================================================================================================================

Generated Folders
-----------------

Some directories and files are not part of the repository and explicitly ignore in the `.gitignore` file, but required or
created during the development process. These are:

================================ =========================================================================================================
enmapboxtestdata/                Official EnMAP-Box testdata. Not part of repository code, can be installed calling
                                 ``scripts/install:_testdata.py``.
enmapboxunittestdata/            Unit test testdata. Not part of repository code, can be installed calling
                                 ``scripts/install:_testdata.py``.
qgisresources/                   QGIS resources compiled as python modules.
                                 Read :ref:`here<dev_repo_installation>` for details.
deploy/                          Builds of the EnMAP-Box plugin.
deploy/enmapboxplugin            Folder with last EnMAP-Box Plugin build.
deploy/enmapboxplugin.3.X...zip  Zipped version of a EnMAP-box Plugin build.
================================ =========================================================================================================


.. _dev_repo_installation:

Install the EnMAP-Box repository
================================

#. Open your shell, clone the EnMAP-Box repository including its submodules:

    .. code-block:: batch

        cd <my_repositories>
        git clone --recurse-submodules git@github.com:EnMAP-Box/enmap-box.git
        cd enmapbox
        git config --local include.path ../.gitconfig

#. Add ``<my_repositories>/enmapbox/`` as source location to your PyCharm project
    (instead of that in your QGIS active profile!)


#. (Optional) install the QGIS source code repository.

    For the next step, but also if you like to discover the QGIS ++ code, it is recommended to install the
    QGIS repository as well. Some EnMAP-Box scripts can use data from the QGIS source code, e.g. to show images that
    otherwise are available on runtime in the QGIS Desktop application only.

    .. code-block:: batch

        cd <my_repositories>
        git clone https://github.com/qgis/QGIS.git

    Now define a environmental variable ``QGIS_REPO`` in the IDE / PyCharm startup script (:ref:`dev_setup_pycharm`)

    ============= ====================================================================
    OS            Command
    ============= ====================================================================
    Windows       set QGIS_REPO=<my_repositories/QGIS>
    Linux /macOS  DIR_REPO=<my_repositories/QGIS>
                  export QGIS_REPO
    ============= ====================================================================


#. Run ``scripts/setup_repository.py`` to create Qt resource modules and perform a dependency check.

   The EnMAP-Box uses the Qt resource system (see https://doc.qt.io/qt-5/resources.html for details) to access icons.
   This step creates for each Qt resource file (``filename.qrc``) a corresponding python module
   (``filename.py``) that contains a binary encrypted description of resources (icons, images, etc.).
   During startup, these resources are loaded and can be accessed by resource path strings.

   The EnMAP-Box re-uses several icons provided by the QGIS desktop application. For example,
   the QGIS icon for raster layers is available at ``:/images/themes/default/mIconPolygonLayer.svg`` and can be
   visualized in the QGIS python shell as followed:

    .. code-block:: batch

        icon = QIcon(r':/images/themes/default/mIconRaster.svg')
        label = QLabel()
        label.setPixmap(icon.pixmap(QSize(150,150)))
        label.show()

    .. figure:: img/resources_qgis_icon_example.png
         :width: 200px

         The QGIS icon for raster (mIconRaster.svg)

   If we start and develop application from inside PyCharm, we usually don't have access to QGIS desktop application
   resources. However, if you have downloaded the QGIS repository as described above, ``scripts/setup_repository.py``
   will look for it, compile the resource files and write them into folder ``enmap-box/qgisresources``.



Install / Update EnMAP-Box Testdata
===================================

The most-recent EnMAP-Box testdata is hosted on https://bitbucket.org/hu-geomatics/enmap-box/downloads
If missing or outdatet, it will be downloaded and installed after a user
clicks on `Project > Load Example Data`. The downloaded data will be extracted into
``<root>/enmapboxtestdata``, with ``<root>`` either being the EnMAP-Box repository folder or the QGIS plugin installation
folder.

The testdata can be download explicitly:

.. code-block:: python

    import enmapbox.dependencycheck
    enmapbox.dependencycheck.installTestData(ask=False, overwrite_existing=True)


.. _dev_repo_update_remote_sources:

Get Updates from other Repositories
===================================

The EnMAP-Box includes source-code from external code repositories.
They are defined as submodules in `.gitmodules`, e.g. like:

.. code-block:: bash

    [submodule "enmapbox/qgispluginsupport"]
        path = enmapbox/qgispluginsupport
        url = git://github.com/EnMAP-Box/qgispluginsupport.git
        pushurl = git@github.com:EnMAP-Box/qgispluginsupport.git
        branch = master

Updating submodules from its origin lication (``url``) can be done by:
.. code-block:: bash

        cd enmapbox
        git submodule update --remote

Pushing local modification into a new branch of the submodule's origin can be done with:

.. code-block:: bash

        cd <path/submodule>
        git add .
        git commit -m "my changes"
        git push -u origin HEAD:my_update_branch
