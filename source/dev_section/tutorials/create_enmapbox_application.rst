.. include:: ../external_links.rst

.. _dev_tut_create_enmapbox_application:

Create EnMAP-Box Applications
#############################


Applications for the EnMAP-Box define an `EnMAPBoxApplication` instance that describes basic
information like the Applications name and how a user can start it. The following examples are taken from the
``examples/minimumexample`` package, which you might copy and modify to implement own EnMAPBox Applications.

1. Initialize a new EnMAP-Box Application
=========================================

An EnMAP-Box application inherits from `EnMAPBoxApplication` and defines basic information like a
`name` and `version`. The variable `license` defaults to `GNU GPL-3`, but might be changed::

    from qgis.PyQt.QtGui import QIcon
    from qgis.PyQt.QtWidgets import QMenu, QAction, QWidget, QHBoxLayout, QLabel, QPushButton
    from enmapbox.gui.applications import EnMAPBoxApplication
    from qgis.core import *


    VERSION = '0.0.1'
    LICENSE = 'GNU GPL-3'
    APP_DIR = os.path.dirname(__file__)

    APP_NAME = 'My First EnMAPBox App'

    class ExampleEnMAPBoxApp(EnMAPBoxApplication):
        """
        This Class inherits from an EnMAPBoxApplication
        """
        def __init__(self, enmapBox, parent=None):
            super(ExampleEnMAPBoxApp, self).__init__(enmapBox, parent=parent)

            #specify the name of this app
            self.name = APP_NAME

            #specify a version string

            self.version = VERSION

            #specify a licence under which you distribute this application
            self.licence = LICENSE


2. Define an Menu
=================

To become accessible via a menu of the EnMAP-Box, the application needs to implement `EnMAPBoxApplication.menu(...)` to
return a QAction_ or (better) a QMenu_ with multiple QActions_. By default, the returned object is added to the EnMAP-Box
"Application" menu from where users can start the QAction_ that you defined::

    def menu(self, appMenu):
        """
        Returns a QMenu that will be added to the parent `appMenu`
        :param appMenu:
        :return: QMenu
        """
        assert isinstance(appMenu, QMenu)
        """
        Specify menu, submenus and actions that become accessible from the EnMAP-Box GUI
        :return: the QMenu or QAction to be added to the "Applications" menu.
        """

        # this way you can add your QMenu/QAction to an other menu entry, e.g. 'Tools'
        # appMenu = self.enmapbox.menu('Tools')

        menu = appMenu.addMenu('My Example App')
        menu.setIcon(self.icon())

        #add a QAction that starts a process of your application.
        #In this case it will open your GUI.
        a = menu.addAction('Show ExampleApp GUI')
        assert isinstance(a, QAction)
        a.triggered.connect(self.startGUI)
        appMenu.addMenu(menu)

        return menu


3. Define QgsProcessingAlgorithms for the EnMAPBoxAlgorithm Provider
====================================================================

Your Application might provide one or multiple QgsProcessingAlgorithms_ for the QGIS Processing Framework. This way your algorithms
become visible in the QGIS Processing Toolbox and can be used in the QGIS Model Builder.
To add your QgsProcessingAlgorithms_ to the EnMAP-Box Algorithm Provider implement `EnMAPBoxApplication.processingAlgorithms(...)`.

For the sake of simplicity, let's define a simple function and a QgsProcessingAlgorithm_ to call it::

    def exampleAlgorithm(*args, **kwds)->list:
        """
        An dummy algorithm that prints the provided arguments and keywords and returns its inputs.
        """
        print('Start exampleAlgorithm...')

        text = ['Arguments: {}'.format(len(args))]
        for i, a in enumerate(args):
            text.append('Argument {} = {}'.format(i+1, str(a)))

        text.append('Keywords: {}'.format(len(kwds)))
        for key, parameter in kwds.items():
            text.append('{} = {}'.format(key, parameter))
        print('\n'.join(text))
        print('exampleAlgorithm finished')

        return args, kwds


    class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
        """
        Exemplary implementation of a QgsProcessingAlgorithm.
        See https://api.qgis.org/api/classQgsProcessingAlgorithm.html for API documentation
        """
        def __init__(self):
            super(ExampleProcessingAlgorithm, self).__init__()

        def createInstance(self)->QgsProcessingAlgorithm:
            """
            Creates a new instance of the algorithm class.
            :return: QgsProcessingAlgorithm
            """
            return ExampleProcessingAlgorithm()

        def name(self)->str:
            return 'examplealgorithm'

        def displayName(self):
            return 'Minimal Example Algorithm'

        def groupId(self)->str:
            """
            Returns the unique ID of the group this algorithm belongs to.
            :return: str
            """
            return GROUP_ID

        def group(self)->str:
            """
            Returns the name of the group this algorithm belongs to.
            :return: str
            """
            return APP_NAME

        def initAlgorithm(self, configuration:dict=None):
            """
            Initializes the algorithm using the specified configuration.
            :param configuration: dict
            """
            self.addParameter(QgsProcessingParameterRasterLayer('pathInput', 'The Input Dataset'))
            self.addParameter(QgsProcessingParameterNumber('value','The value', QgsProcessingParameterNumber.Double, 1, False, 0.00, 999999.99))
            self.addParameter(QgsProcessingParameterRasterDestination('pathOutput', 'The Output Dataset'))

        def processAlgorithm(self, parameters:dict, context:QgsProcessingContext, feedback:QgsProcessingFeedback):
            """
            Runs the algorithm using the specified parameters.
            :param parameters: dict
            :param context: QgsProcessingContext
            :param feedback: QgsProcessingFeedback
            :return: dict
            """
            assert isinstance(parameters, dict)
            assert isinstance(context, QgsProcessingContext)
            assert isinstance(feedback, QgsProcessingFeedback)

            args, kwds  = exampleAlgorithm(parameters)

            outputs = {'args' : args, 'kwds': kwds}
            return outputs


Now define `EnMAPBoxApplication.processingAlgorithms(...)` to add the `ExampleProcessingAlgorithm` to the `EnMAPBoxProcessingProvider`::

    def processingAlgorithms(self)->list:
        """
        This function returns the QGIS Processing Framework algorithms specified by your application
        :return: [list-of-QgsProcessingAlgorithms]
        """

        return [ExampleProcessingAlgorithm()]


Calling the `ExampleProcessingAlgorithm` from the QGIS Processing Toolbox should now create a printout on your python console like::

    Parameters:
    pathInput = <qgis._core.QgsRasterLayer object at 0x0000018AA3C47A68>
    pathOutput = <QgsProcessingOutputLayerDefinition {'sink':C:/Users/ivan_ivanowitch/AppData/Local/Temp/processing_cb76d9820fc64087aa8264f0f8505334/642d8e0abb764557881346399dda9c68/pathOutput.bsq, 'createOptions': {'fileEncoding': 'System'}}>
    value = 1.0



4. Create a Graphical User Interface
====================================

The `startGUI()` function is used to open the graphical user interface. A very simple GUI could be::

    def onButtonClicked():
        print('Button was pressed')

    w = QWidget()
    w.setLayout(QVBoxLayout())
    w.layout().addWidget(QLabel('Hello World'))
    btn = QPushButton()
    btn.setText('click me')
    btn.clicked.connect(onButtonClicked)
    w.layout().addWidget(btn)
    w.show()


A GUI quickly becomes complex if programmed line-by-line only. We prefer to use the QDesigner. It allows to
*draw* the GUI frontend which then is saved as `*.ui` XML file. This file can be translated into the PyQt code where you
just write the backend.


List of environmental variables
===============================

.. warning::

    This will be changed soon

The following environmental variables can be set to change the starting behaviour of the EnMAP-Box.

====================  ====================  ==============================================================================================
Name                  Values, * = Default   Description
====================  ====================  ==============================================================================================
EMB_LOAD_PF           TRUE*/FALSE           Load QGIS processing framework.
EMB_LOAD_EA           TRUE*/FALSE           Loads external applications.
EMB_DEBUG             TRUE/FALSE*           Enable additional debug printouts.
EMB_SPLASHSCREEN      TRUE*/FALSE           Splashscreen on EnMAP-Box start.
EMB_MESSAGE_TIMEOUT   integer               Timeout in seconds for popup messages in the message bar.
EMB_APPLICATION_PATH  string                list of directories (separated by ';' or '\n' (newline)) to load EnMAPBoxApplications from.
====================  ====================  ==============================================================================================

Further links and sources
=========================

* https://devguide.python.org/

Git for Beginners
-----------------

* https://rogerdudler.github.io/git-guide/
* https://rogerdudler.github.io/git-guide/files/git_cheat_sheet.pdf


PyQGIS
------

* https://api.qgis.org/api/
* https://webgeodatavore.github.io/pyqgis-samples/
* https://www.qgis.org/en/site/getinvolved/development/index.html


Python Code Documentation
-------------------------

* https://www.sphinx-doc.org/en/master/usage/quickstart.html
* https://devguide.python.org/documenting/
* https://docutils.sourceforge.io/rst.html
* https://sphinx-rtd-theme.readthedocs.io/en/latest/index.html
