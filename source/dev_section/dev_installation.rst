*Last Update: 2025-06-19*

.. _dev_installation:

Installation
############

Overview
========

If you like to develop an EnMAP-Box application, or more general, a QGIS and Qt application, we recommend to use
a state-of-the-art Integrated Development Environment (IDE) like |PyCharm|. It offers run-time debugging,
code completion, spell-checking, syntax highlighting, SCM support, unit-testing and many other helpful things.

1. Have Git Installed
=====================

..
    @Arayan add Windows | Linux | macOS tabs

If not, download and install *Git* from https://git-scm.com/downloads

Check if git is installed to your local shell, e.g. as:

.. code-block:: bat

    C:\Windows\System32>git --version
    git version 2.26.0.windows.1


2. Clone the EnMAP-Box Repository
=================================

Clone the EnMAP-Box repository (or a fork) to your local ``my_repositories`` folder and update
its submodules by:

..
    @Arayan add Windows | Linux | macOS tabs here

.. code-block:: bash

    cd my_repositories
    git clone --recurse-submodules git@github.com:EnMAP-Box/enmap-box.git
    cd enmap-box
    git config --local include.path ../.gitconfig

The last line ensures that pull requests will update submodules as well.

Now you can use `git pull <https://git-scm.com/docs/git-pull>`__ to update your local copy of the
EnMAP-Box repository:

.. code-block:: bash

    cd my_repositories/enmap-box
    git pull


.. tip::

        Replace the repo uri with that of your EnMAP-Box repo fork, if you like to
        provide code via pull requests.

.. _dev_installation_create_conda_qgis:

3. Setup the QGIS Environment
=============================

This section gives examples how you can setup a QGIS & EnMAP-Box development environment, e.g. to be used by PyCharm.

.. tabs::

    .. group-tab:: Windows

        **Install or update packages**

        1. Install QGIS using the OSGeo4W Network installer https://qgis.org/en/site/forusers/download.html

        2. Install the OSGeo4W environment to a folder of choice (preferably one you have permanent writing access to).
           In following this is called `OSGeo4W`.

        3. Start the OSGeo4W Setup.

        4. Go forward to these steps by clicking `next`. Usually the default settings should be fine
            * 'Advanced Install'
            * 'Install from Internet'
            * 'Root Directory' (should be your `OSGEO4W` directory)
            * Select Local Package Directory (default)
            * Select Your Internet Connect (default Direct Connection)
            * Choose A Download Site (default https://download.osgeo.org )

        5. Select Packages to install / update

            +---------------------+------------------------------+
            | Package             | Note                         |
            +=====================+==============================+
            | qgis                | recent official QGIS version |
            +---------------------+------------------------------+
            |python3-scikit-learn |                              |
            +---------------------+------------------------------+

        6. Press Next to install packages / updates

        **Setup development environment**

        1. Copy the `qgis-env.bat` and `start_pycharm.bat` from https://github.com/EnMAP-Box/enmap-box/tree/main/.env/osgeo4w
           to a local folder, e.g. your windows desktop
        2. Modify the `qgis-env.bat` config section to fit to your local environment, i.e. set the correct paths to your
           local OSGeoW installation and PyCharm executable

            .. code-block:: batch

                @echo off

                :: ### CONFIG SECTION ###
                :: root of local OSGEO4W installation
                set OSGEO4W_ROOT=D:\OSGeo4W
                :: PyCharm executable, adjust for version updates
                set PYCHARM_EXE="C:\Program Files (x86)\JetBrains\PyCharm 2022.1.2\bin\pycharm64.exe"

                :: git binaries and git lfs binaries
                set BIN_GIT=C:\Program Files\Git\bin
                set BIN_LFS=C:\Program Files\Git LFS

        3. Call `start_pycharm.bat` to open PyCharm within the latest QGIS release.
           You can modify the start script to start a different QGIS build. E.g.

            .. code-block:: batch

                call "%~dp0\qgis-env.bat" qgis-ltr
                start "PYCHARM" /B %PYCHARM_EXE%

           will start the QGIS Long Term Release (if installed) instead of the latest QGIS release (`qgis`).

           Possible QGIS versions provided by the OSGeo4W installer are:

           +----------------+--------------------------------------------------+
           | Build          | Description                                      |
           +================+==================================================+
           | `qgis`         | QGIS Desktop (latest release)                    |
           +----------------+--------------------------------------------------+
           | `qgis-ltr`     | QGIS Desktop (long term release)                 |
           +----------------+--------------------------------------------------+
           | `qgis-dev`     | QGIS nightly build of the development branch     |
           +----------------+--------------------------------------------------+
           | `qgis-rel-dev` | QGIS nightly build of the latest release branch  |
           +----------------+--------------------------------------------------+

    .. group-tab:: Linux & macOS

        Due to the much simpler installation and maintenance, we recommend to install QGIS for Linux and macOS
        using conda.

    .. group-tab:: Conda

        The installation of QGIS within `conda <https://docs.conda.io/en/latest>`_
        is (almost) the same on macOS, Windows or Linux. Using conda
        it is often much easier to install additional python packages, and
        admin rights are not required.

        1. Make sure `conda <https://docs.conda.io/projects/conda/en/stable/>`_ is installed on your system.
           We recommend to use the `miniforge <https://github.com/conda-forge/miniforge>`_
           installer, which defaults to packages from the `conda-forge channel <https://conda-forge.org/>`_.

        2. Create a new conda environment using one of the EnMAP-Box environment files
           from `<https://github.com/EnMAP-Box/enmap-box/tree/main/.env/conda>`_

            .. list-table:: Conda environments to run the EnMAP-Box
                :header-rows: 1

                *   - Environment File
                    - Description
                *   - `enmapbox_full_latest.yml <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_latest.yml>`_
                    - Most-recent QGIS release and python dependencies for all EnMAP-box applications,
                      including numba.
                *   - `enmapbox_light_latest.yml <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_light_latest.yml>`_
                    - Most-recent QGIS release and minimum (*light*) set of python dependencies to run EnMAP-Box.
                *   - `enmapbox_full_longterm.yml <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_longterm.yml>`_
                    - Most-recent QGIS long-term release (LTR) and python dependencies for all
                      EnMAP-box applications, including numba.
                *   - `enmapbox_light_latest.yml <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_light_latest.yml>`_
                    - Most-recent QGIS long-term release (LTR) and minimum set of python dependencies
                      to run EnMAP-Box.
                *   - `enmapbox_light_3.38.yml <https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_light_3.38.yml>`_
                    - QGIS 3.38 with minimum set of python dependencies to run EnMAP-Box.


           E.g. to install the latest QGIS with all python requirements in a conda environment named *enmapbox*, run:

            .. code-block:: batch

               conda env create --name enmapbox --file https://raw.githubusercontent.com/EnMAP-Box/enmap-box/main/.env/conda/enmapbox_full_latest.yml

        .. tip::

           Depending on the components and applications you like to use, it might be required to install more packages.
           If you cloned the EnMAP-Box repository you can also point to the local :file:`enmapbox_full_latest.yml`.
           Edit the ``--name`` or the YAML file itself as you wish. For more information on creating and managing conda
           environments visit the
           `conda documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=manage%20environments#creating-an-environment-from-an-environment-yml-file>`_

        3.  `Activate <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=manage%20environments#activating-an-environment>`_
            the new environment:

            .. code-block:: batch

               conda activate enmapbox


        4.  Now you can start `|QGIS`|, the :ref:`Qt Designer <dev_additional_tools>` and
            :ref:`Qt Assistant <dev_additional_tools>` from your conda shell:

            .. code-block:: batch

               qgis
               designer
               assistant


        5. To easily start applications in this environment that have not been installed by conda, you might
           define aliases during the activation of the environment, e.g. to start PyCharm

            * Create an activation script and define an alias for PyCharm:

                Windows: *<your conda installation>/envs/enmapbox/etc/conda/activate.d/pycharm-activate.bat*

                .. code-block:: batch

                 @echo off
                 doskey pycharm="<path to pycharm executable>"


                MacOS: *<your conda installation>/envs/enmapbox/etc.conda/activate.d/pycharm-activate.sh*

                .. code-block:: bash

                 alias pycharm='open -a PyCharm\ CE.app'

            * For completeness, also create a deactivation script:

                Windows: *<your conda installation>/envs/enmapbox/etc/conda/deactivate.d/others-deactivate.bat*

                .. code-block:: batch

                    @echo off
                    doskey pycharm=

                MacOS/Linux: *<your conda installation>/envs/enmapbox/etc.conda/deactivate.d/pycharm-deactivate.sh*

                .. code-block:: bash

                    alias pycharm=


    .. group-tab:: Docker

        .. todo::

            Describe installation using docker image



.. _dev_setup_pycharm:

4. Setup the IDE
================

..
    @aryan add PyCharm and VSCode Tab

.. tabs::

   .. group-tab:: PyCharm



        1.  Start |PyCharm| and add `my_repositories/enmap-box` as new project via *File > Open File or Project*

        2.  If this is not already the case, tell PyCharm where to find your Git-executable.
            Open *File > Settings > Version Control > Git* to set *Path to Git executable*.
            Press *Test* to check the used Git version.

            .. figure:: img/pycharm_git_settings.png

                Set the Git executable used by PyCharm

            .. tip::

                Use ``where`` to return the path of a git-executable that is available in your DOS/Linux/macOS shell

                .. code-block:: bat

                    (enmapbox) C:\>where git
                    C:\Users\my_username\AppData\Local\Programs\Git\cmd\git.exe


        3.  Switch to *Project: enmap-box > Project Interpreter* and select the QGIS python as python interpreter.



            .. figure:: img/pycharm_conda_interpreter_add.png

                Add the *enmapbox* python to the list of python interpreters


            .. figure:: img/pycharm_conda_interpreter.png

                Select the *enmapbox* python as project interpreter



        4.  Switch to *Project Structure* and add the QGIS python folder as additional project content root.

            ============= ===========================================================================
            OSGeo4W       ``<your OSGeo4W folder>\bin\python``
            Linux         ``/usr/bin/python3``
            macOS         ``/Application/QGIS.app/Contents/MacOS/bin/python3``
            conda (win)   ``<conda root>/envs/enmapbox/Library/python``
            conda (linux) ``<conda root>/envs/enmapbox/share/qgis/python``
            conda (macOS) ``<conda root>/envs/enmapbox/QGIS.app/Contents/MacOS/../Resources/python``
            ============= ===========================================================================


            Right-click on the ``plugins`` subfolder and select :guilabel:`Sources`.
            This makes QGIS internal plugins like the "processing" plugin available to PyCharm.

            Now the PyQGIS API is available to your Python installation.

            .. tip::

                The same way allows you to include other directories to your project's *PYTHONPATH*,
                e.g. to make code available from other folder or repositories.


            .. figure:: img/pycharm_project_content_roots.png

                Use ``enmap/Library/python`` as additional content root


   .. group-tab:: VS Code

        .. todo:

            Describe Setup with VS Code


5.  PyCharm and PyQGIS may need the environmental variable ``QGIS_PREFIX_PATH``. Typical paths are:

    ================= ===============================================================================
    QGIS Installation QGIS_PREFIX_PATH
    ================= ===============================================================================
    OSGeo4W           `<OSGeo4W>/apps/qgis`
    Linux
    conda (Windows)   `<conda installation>\\envs\\enmap\\Library`
    conda (Linux)     `<conda installation>/envs/enmapbox`
    conda (macOS)     `<conda installation>/envs/enmapbox/QGIS.app/Contents/Resources`
    ================= ===============================================================================

    If not already set in the environment from which you started PyCharm, you can set it explicitly.
    Open *Run > Debug ... > Edit Configurations* and add the *QGIS_PREFIX_PATH* to the User environmental variables.
    This way PyCharm runs python files in a environment with *QGIS_PREFIX_PATH* defined.

    .. figure:: img/pycharm_QGIS_PREFIX_PATH.png

    Also define the Environment variables for the Python console. Go to *File > Settings > Build, Execution, Deployment > Console > Python Console*
    and add *QGIS_PREFIX_PATH* to the Environment variables.

    .. figure:: img/pycharm_qgispath_console.png

    You may also modify the shell used in your PyCharm terminal to use the QGIS environment.
    Open *Tools > Terminal* and set the shell path to, for example:

    ================= ===============================================================================
    QGIS Installation Terminal path
    ================= ===============================================================================
    OSGeo4W           ``cmd.exe "/K" qgis_env.bat`` (see above how to create the ``qgis_env.bat``)
    conda (Windows)   ``cmd.exe "/K" <conda installation>\Scripts\activate.bat enmapbox``
    ================= ===============================================================================




    .. figure:: img/pycharm_conda_terminal.png

        How to use the conda terminal in PyCharm


6.  Test the Python environment

    To check if the QGIS API is available, open a *Python Console* and import the ``QgsApplication`` object.

    .. code-block:: python

        from qgis.core import QgsApplication
        QgsApplication.instance() is None

    The output should return ``True``, as we have not initialized any QgsApplication.

    Now check if we can use the EnMAP-Box API to start the EnMAP-Box

    .. code-block:: python

        import enmapbox
        enmapbox.run()

    This should initialize a new QgsApplication and start the EnMAP-Box.
    The outputs printed to the python shell should look like:

    .. code-block:: bash

        Application state:
        QGIS_PREFIX_PATH env var:		D:\miniconda3\envs\enmapbox\Library
        Prefix:		D:\miniconda3\envs\enmap\Library
        Plugin Path:		D:\miniconda3\envs\enmapbox\Library/plugins
        Package Data Path:	D:\miniconda3\envs\enmapbox\Library/.
        Active Theme Name:
        Active Theme Path:	D:\miniconda3\envs\enmapbox\Library/./resources/themes\\icons/
        Default Theme Path:	:/images/themes/default/
        SVG Search Paths:	D:\miniconda3\envs\enmapbox\Library/./svg/
                C:\Users\geo_beja\AppData\Local\Temp\QGIS-PythonTestConfigPathp1k7w_s_\profiles\default/svg/
        User DB Path:	D:\miniconda3\envs\enmapbox\Library/./resources/qgis.db
        Auth DB Path:	C:\Users\geo_beja\AppData\Local\Temp\QGIS-PythonTestConfigPathp1k7w_s_\profiles\default/qgis-auth.db


    If the terminal environment was setup well, you
    can start the EnMAP-Box from the *Terminal* window as well by

    .. code-block:: bat

        (enmapbox) ..\enmap-box>python enmapbox


Additional Tools
================

The Qt company provides various tools that help to create Qt applications. They are useful for PyQt and PyQGIS users
as well.

.. _dev_additional_tools:

.. tabs::

    .. _dev_qt_assistant:
    .. group-tab:: Qt Assistant

        The Qt Assistant allows to discover and read `*.qch` files, which are provided for the
        Qt and QGIS APIs. Although written to document the C++ code, most descriptions apply 1:1 to the Python API.

        The Qt Assistant browses `*.qch` files super fast and also offline, which is why it is often a better
        alternative to the slower Python online documentation.
        In addition, the `*.qch` docs link into the QGIS C++ source code,
        which makes it easier to understand the functionality of the QGIS API.

        1.  Download the ``*.qch*`` files which contain:

            * the Qt API documentation files: https://github.com/PierreRaybaut/PyQtdoc
            * the QGIS API documentation  `qgis.qch <https://api.qgis.org/api/qgis.qch>`_


            Go to *Preferences > Add* and add the following ``*.qch`` files

            ============= =====================================
            File          Documentation
            ============= =====================================
            qgis.qch      qgis.core, qgis.gui
            qtcore.qch    Qt5.QtCore
            qtgui.qch     Qt5.QtGui
            qtwidgets.qch Qt5.QtWidgets
            ============= =====================================

            `D:\OSGEO4W\apps\Python312\Lib\site-packages\PyQtdoc`

            Now you can explore the Qt (``Q...``) and QGIS (``Qgs...``) classes

            .. figure:: img/qt_assistant.png
                 :width: 100%


        1.  Start the Qt Assistant, e.g. from your PyCharm terminal:

            .. code-block:: bat

                (enmapbox) $>assistant


    The following script can be used to regularly update the QGIS documentation:

    .. code-block:: bash

        curl --output <path_to>/qgis.qch --url https://api.qgis.org/api/qgis.qch
        assistant -register <path_to>/qgis.qch -quiet


    .. group-tab:: Qt Designer

        The Qt Designer is a powerful tool to create GUI frontends by drawing, drag and drop.
        Created GUI form files are saved in a XML file ending with ``*.ui``. These can be called from
        python to automatically create the entire GUI backend, e.g. windows and buttons defined with the Qt Designer.

        You can start the Qt Designer from your PyCharm terminal by:

            .. code-block:: bat

                (enmapbox) $>designer


        .. figure:: img/qt_designer_example.png
             :width: 100%

             Qt Designer showing the metadataeditor.ui for the Metadata editor.

    .. group-tab:: Qt Creator

        The Qt Creator is the one-in-all IDE to develop Qt C++ applications. It includes the functionality covered by Qt Assistant
        (here called Help) and Qt Designer (here called form designer) and helps to browse C++ code. It is the preferred tool to
        explore the QGIS C++ source code, for example if you like to better understand what it does behind the QGIS python API.

        Qt and the Qt Creator are available at https://www.qt.io/download. Ensure to install the code documentation for the same
        Qt version used by QGIS.

        .. figure:: img/qt_creator_example_ui.png
             :width: 100%

             Qt Creator with opened metadataeditor.ui.

        ..
                SSH access on windows
                1. create a ssh key pair
                2. upload public key to repository of choice
                3. install Putty
                4. start Pageant.ext and add your private key to
                5. add :code:`set GIT_SSH=C:\Program Files\PuTTY\plink.exe` to your startup script
                6. there is an issue with a frozen command line when a server is connected the first time with ssh
                   (see https://stackoverflow.com/questions/33240137/git-clone-pull-continually-freezing-at-store-key-in-cache)
                   to solve it, start putty and connect to the server once per SSH (e.g. to github.com).
                   putty will save its fingerprint
                7. now you can call git push using ssh authentication in background

OSGeo4W for Devs
================

The OSGeo4W installer for QGIS on windows allows you to install and maintain
different QGIS versions in parallel.

.. list-table:: Some OSGeo4W QGIS versions
    :widths: 30 50
    :header-rows: 1

    *   - Package
        - Descriptions

    *   - ``qgis``
        - Latest QGIS release (LR)

    *   - ``qgis-ltr``
        - QGIS long term release (LTR)

    *   - ``qgis-dev``
        - Nightly build of QGIS developer branch

    *   - ``qgis-qt6``
        -   QGIS Desktop using Qt6 (QGIS 4.0)




Setup Environment
-----------------

1. Download the (new) OSGeo4W installer (`osgeo4w-setup.exe` from https://www.qgis.org/en/site/forusers/download.html )

2. Install the nightly build branch `qgis-dev` and related debug symbols `qgis-dev-pdb`.

3. Install other required packages, e.g. pip3 etc. Later on.
   In case of missing packages, search and install via OSGeo4W installer first. If not available there, use
   the OSGeo4W shell and call `pip`.

4. Create a `qgis-dev-env.bat` to setup your QGIS environment

    .. code-block:: bash

        set OSGEO4W_ROOT=D:\OSGeo4W
        set QGISDISTR=qgis-dev
        set DIR_GIT=C:\Program Files\Git\cmd
        set DIR_LFS=C:\Program Files\Git LFS
        :: add GIT and LFS to path

        call "%OSGEO4W_ROOT%\bin\o4w_env.bat"
        path %OSGEO4W_ROOT%\apps\%QGISDISTR%\bin;%DIR_GIT%;%DIR_LFS%;%PATH%

        set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/%QGISDISTR%
        set GDAL_FILENAME_IS_UTF8=YES
        rem Set VSI cache to be used as buffer, see #6448
        set VSI_CACHE=TRUE
        set VSI_CACHE_SIZE=1000000
        set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\%QGISDISTR%\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
        set PYTHONPATH=%OSGEO4W_ROOT%\apps\%QGISDISTR%\python;%OSGEO4W_ROOT%\apps\%QGISDISTR%\python\plugins;%PYTHONPATH%

    Don't forget to make git and git-lfs available in this environment.

5. Create a `qgis-dev-pycharm.bat` in the same folder as `qgis-dev.bat` that starts PyCharm

    .. code-block:: bash

        call "%~dp0\QGIS-dev.bat"
        set PYCHARM_EXE="C:\Program Files (x86)\JetBrains\PyCharm 2020.3.4\bin\pycharm64.exe"

        start "PYCHARM" /B %PYCHARM_EXE%

        :: uncomment to start QGIS
        :: start "QGIS" /B "%OSGEO4W_ROOT%\bin%QGISDISTR%-bin.exe" %*

6. Call `qgis-dev-pycharm.bat` to start PyCharm and set your project settings to:

* Project Interpreter: `<OSGEO4W>\bin\python.exe`

    .. figure:: img/pycharm_osgeo4w_interpreter.png
         :width: 100%

         Using the OSGeo4W python as project interpreter.

* Terminal Shell Path: `cmd.exe "/K" <your path to>\qgis-dev.bat`
  (this is why we created two batch files. `qgis-dev.bat` setups the environment, but does not start any app)

    .. figure:: img/pycharm_osgeo4w_terminal.png
         :width: 100%

         The `qgis-dev.bat` will be called when starting the terminal


* add `<OSGEO4W>\apps\qgis-dev\python` and
  `<OSGEO4W>\apps\qgis-dev\python\plugins` as source folders

    .. figure:: img/pycharm_osgeo4w_content_roots.png
         :width: 100%

         Adding the QGIS `python` and `python\plugins` folder as content roots.

Debug QGIS with Visual Studio
-----------------------------


1. Clone the QGIS repo and checkout the latest master

2. Install Visual Studio and open the QGIS repo

3. Start a QGIS desktop, e.g. with `qgis-dev` from the OSGeo4W shell

4. Attach the Visual Studio debugger to a QGIS desktop instance

* Open Debug > Attach to Process (CTRL+ALT+P)

* Filter available processes by 'QGIS' and, e.g., select `qgis-dev-bin.exe`

* Press the Attach button





References
==========

- Git -the simple guide (no deep shit) https://rogerdudler.github.io/git-guide/
- Qt5 C++ API https://doc.qt.io/qt-5/
- QGIS C++ API https://api.qgis.org/api/
- QGIS Python https://qgis.org/pyqgis
- QGIS Python developer cookbook https://docs.qgis.org/3.4/en/docs/pyqgis_developer_cookbook


.. AUTOGENERATED SUBSTITUTIONS - DO NOT EDIT PAST THIS LINE

.. |PyCharm| replace:: `PyCharm <https://www.jetbrains.com/pycharm/>`__
