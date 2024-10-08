import pathlib
import re
import qgis.PyQt.QtCore
import qgis.PyQt.QtGui
import qgis.PyQt.QtWidgets
import qgis.core

DIR_REPO = pathlib.Path(__file__).parents[1]
DIR_SOURCE = DIR_REPO / 'source'
assert DIR_SOURCE.is_dir()

PATH_LINK_RST = DIR_SOURCE / 'substitutions_links.txt'

objects = []
for module in [
    qgis,
    qgis.core,
    qgis.gui,
    qgis.PyQt.QtCore,
    qgis.PyQt.QtWidgets,
    qgis.PyQt.QtGui,
    qgis.PyQt.QtWidgets
]:
    s = ""
    for key in module.__dict__.keys():
        if re.search('^(Qgs|Q)', key):
            objects.append(key)
objects = sorted(objects)

lines = """# autogenerated file.

.. |PyCharm| replace:: `PyCharm <https://www.jetbrains.com/pycharm/>`_
.. |PyQtGraph| replace:: `PyQtGraph <https://pyqtgraph.readthedocs.io/en/latest/>`_
.. |PyDev| replace:: `PyDev <https://www.pydev.org>`_
.. |OSGeo4W| replace:: `OSGeo4W <https://www.osgeo.org/projects/osgeo4w>`_
.. |Bitbucket| replace:: `Bitbucket <https://bitbucket.org>`_
.. |Git| replace:: `Git <https://git-scm.com/>`_
.. |GitHub| replace:: `GitHub <https://github.com/>`_
.. |GDAL| replace:: `GDAL <https://www.gdal.org>`_
.. |QtWidgets| replace:: `QtWidgets <https://doc.qt.io/qt-5/qtwidgets-index.html>`_
.. |QtCore| replace:: `QtCore <https://doc.qt.io/qt-5/qtcore-index.html>`_
.. |QtGui| replace:: `QtGui <https://doc.qt.io/qt-5/qtgui-index.html>`_
.. |QGIS| replace:: `QGIS <https://www.qgis.org>`_
.. |qgis.gui| replace:: `qgis.gui <https://api.qgis.org/api/group__gui.html>`_
.. |qgis.core| replace:: `qgis.core <https://api.qgis.org/api/group__core.html>`_
.. |Miniconda| replace:: `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
.. |miniconda| replace:: `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
.. |Numba| replace:: `Numba <https://numba.pydata.org/>`_
.. |Conda| replace:: `Conda <https://docs.anaconda.com/miniconda/>`_
.. |conda| replace:: `conda <https://docs.anaconda.com/miniconda/>`_
.. |conda-forge| replace:: `conda-forge <https://conda-forge.org/>`_
.. |pip| replace:: `pip <https://pip.pypa.io/en/stable>`_

# autogenerated singular forms
"""

WRITTEN = []

rx_qgis = re.compile('^Qgs|Qgis.*')

for obj in objects:
    obj: str
    if obj in ['QtCore', 'QtGui', 'QtWidget']:
        continue
    print(obj)

    target = None
    if rx_qgis.match(obj):
        # https://qgis.org/api/classQgsProject.html
        target = "https://api.qgis.org/api/class{}.html".format(obj)
    elif obj.startswith('Q'):
        # https://doc.qt.io/qt-5/qwidget.html
        target = "https://doc.qt.io/qt-5/{}.html".format(obj.lower())
    else:
        continue

    singular = obj
    plural = obj + 's'

    line = None
    if singular.upper() not in WRITTEN:
        line = f'.. |{singular}|  replace:: `{singular} <{target}>`_'
        WRITTEN.append(singular.upper())

        if plural.upper() not in WRITTEN:
            line += f'\n.. |{plural}| replace:: `{plural} <{target}>`_'
            WRITTEN.append(plural.upper())

    if line:
        lines += '\n' + line

with open(PATH_LINK_RST, 'w', encoding='utf-8') as f:
    f.write(lines)
