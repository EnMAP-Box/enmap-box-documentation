import enum
import os
import re
import shutil
import subprocess
import warnings
from os import walk
from pathlib import Path
from typing import Dict, List, Optional, Union

import qgis
import qgis.PyQt.QtCore
import qgis.PyQt.QtGui
import qgis.PyQt.QtWidgets
import qgis.core
import qgis.gui


DIR_REPO = Path(__file__).parents[1]
DIR_OTHER_REPOS = DIR_REPO.parent
DIR_SOURCE = DIR_REPO / 'source'

DIR_ICONS = DIR_SOURCE / 'img/icons'

ICON_DIRS = [
    DIR_ICONS,
]

ENV_INKSCAPE_BIN = 'INKSCAPE_BIN'

# add icon sources from EnMAP-Box Repository
ENMAP_BOX_REPO = None
if 'ENMAP_BOX_REPO' in os.environ:
    ENMAP_BOX_REPO = Path(os.environ['ENMAP_BOX_REPO'])
else:
    ENMAP_BOX_REPO = DIR_OTHER_REPOS / 'enmap-box'
if isinstance(ENMAP_BOX_REPO, Path) and ENMAP_BOX_REPO.is_dir():
    ICON_DIRS.append(ENMAP_BOX_REPO / 'enmapbox/gui/ui/icons')
else:
    print('Could not find EnMAP-Box repository')

# add icon sources from QGIS Repository
QGIS_REPO = None
if 'QGIS_REPO' in os.environ:
    QGIS_REPO = Path(os.environ['QGIS_REPO'])
else:
    QGIS_REPO = DIR_OTHER_REPOS / 'QGIS'
if isinstance(QGIS_REPO, Path) and QGIS_REPO.is_dir():
    ICON_DIRS.append(QGIS_REPO / 'images/themes/default')
else:
    print('Could not find QGIS repository')


def inkscapeBin() -> Path:
    """
    Searches for the Inkscape binary
    """
    if ENV_INKSCAPE_BIN in os.environ:
        path = os.environ[ENV_INKSCAPE_BIN]
    else:
        path = shutil.which('inkscape')
    if path:
        path = Path(path)

    assert path.is_file(), f'Could not find inkscape executable. Set {ENV_INKSCAPE_BIN}=<path to inkscape binary>'
    return path


class SourceType(enum.Flag):
    Icon = enum.auto()
    Link = enum.auto()
    Raw = enum.auto()


class Substitute(object):

    def __init__(self, name: str,
                 definition: Optional[str] = None,
                 stype: SourceType = SourceType.Link):
        self.name = name
        self.stype: SourceType = stype
        self.icon_path: Optional[Path] = None
        self.definition: Optional[str] = definition

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (f'{self.__class__.__name__}:{self.name}<{self.stype}>'
                f'\n\ticon_path="{self.icon_path}"'
                f'\n\tdefinition="{self.definition}"')


def isSubDir(parentDir, subDir) -> bool:
    parentDir = Path(parentDir)
    subDir = Path(subDir)
    return subDir.as_posix().startswith(parentDir.as_posix())


class SubstituteCollection(object):

    def __init__(self,
                 source_root: Union[Path, str],
                 dir_rst_icons: Union[Path, str, None] = None):
        assert source_root.is_dir()

        self.mIconSize: int = 28

        self.mSourceRoot = Path(source_root)

        self.mPathInkscapeBin: Optional[Path] = None

        if dir_rst_icons:
            assert isSubDir(self.mSourceRoot, dir_rst_icons)
        else:
            dir_rst_icons = source_root / 'icons'
        assert dir_rst_icons.is_dir()
        self.dir_rst_icons: Path = Path(dir_rst_icons)

        self.mSubstitutes: Dict[str, Substitute] = dict()

    def __getitem__(self, item):
        return self.mSubstitutes[item]

    def __contains__(self, item):
        return self.mSubstitutes.__contains__(item)

    def addLinkSubstitute(self, name: str, link: str):
        sub = Substitute(name, definition=link, stype=SourceType.Link)
        self.addSubstitute(sub)

    def addSubstitute(self, substitute: Substitute):
        assert isinstance(substitute, Substitute)
        if substitute.name in self.mSubstitutes:
            warnings.warn(f'Definition {substitute} already exists: {self[substitute.name]}')
        else:
            self.mSubstitutes[substitute.name] = substitute

    def readSubstitutionDefinitions(self, rst_file: Union[str, Path]) -> List[Substitute]:
        """
        Reads an RST or text file and collects all substitutions.

        Args:
            rst_file: Path to the RST file

        Returns:
            List of Substitute objects

        Examples of recognized substitutions:
        .. |osgeoinstaller| image:: /img/osgeoinstaller.png

        .. |navtools| image:: img/navtools.png
           :height: 27px
        """
        rst_file = Path(rst_file)
        assert rst_file.exists() and rst_file.is_file()

        substitutes = []
        rst_file = Path(rst_file)
        assert rst_file.exists() and rst_file.is_file()

        substitutes = []

        # Pattern for image substitutions
        pattern_img = re.compile(r"\.\. \|([^|]+)\| image:: ([^\n]+)(?:\n[ ]+:[^\n]+)*")

        # Pattern for unicode substitutions
        pattern_unicode = re.compile(r"\.\. \|([^|]+)\| unicode:: ([^\n]+)(?:\n[ ]+:[^\n]+)*")

        # Pattern for link substitutions
        pattern_link = re.compile(r"\.\. \|([^|]+)\| replace:: `([^<]+)<([^>]+)>`_+")

        with open(rst_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if MSG_DO_NOT_EDIT in content:
                content = content.split(MSG_DO_NOT_EDIT)[0].strip()
            if MSG_DO_NOT_EDIT_OLD in content:
                content = content.split(MSG_DO_NOT_EDIT_OLD)[0].strip()


            # Find image substitutions
            for match in pattern_img.finditer(content):
                name = match.group(1)
                image_path = match.group(2).strip()

                sub = Substitute(name, definition=match.group(0), stype=SourceType.Raw)
                if image_path.startswith('/'):
                    sub.icon_path = Path(image_path[1:])  # Remove leading /
                else:
                    sub.icon_path = (rst_file.parent / image_path).relative_to(self.mSourceRoot)
                substitutes.append(sub)

            # Find unicode substitutions
            for match in pattern_unicode.finditer(content):
                name = match.group(1)
                definition = match.group(0)
                sub = Substitute(name, definition=definition, stype=SourceType.Raw)
                substitutes.append(sub)

            # Find link substitutions
            for match in pattern_link.finditer(content):
                name = match.group(1)
                definition = match.group(0)
                sub = Substitute(name, definition=definition, stype=SourceType.Raw)
                substitutes.append(sub)

        return substitutes

    def readIcons(self, source: Path, extensions: List[str] = ['svg', 'png']) -> List[str]:
        assert source.is_dir()
        errors = []
        for ext in extensions:
            for p in find_by_ext(source, ext):
                assert p.is_file()
                name = p.stem
                if name in self:
                    errors.append(
                        f'Name already exists "{name}" {p}:'
                        f'\n\t {self[name]}')
                    continue

                sub = Substitute(name, stype=SourceType.Icon)
                sub.icon_path = p
                if isSubDir(self.mSourceRoot, p.parent):
                    sub.definition = p.relative_to(self.mSourceRoot)

                self.addSubstitute(sub)
                s = ""
        return errors

    def addManualDefinitions(self, source: Path):
        substitutes = self.readSubstitutionDefinitions(source)
        for s in substitutes:
            assert isinstance(s, Substitute)
            self.addSubstitute(s)


    def updateRST(self, path_rst: Union[str, Path], relative_paths: bool = False):
        path_rst = Path(path_rst)
        assert path_rst.is_file()
        assert path_rst.name.endswith('.rst')

        with open(path_rst, 'r') as f:
            lines = f.read().strip()
            if MSG_DO_NOT_EDIT in lines:
                lines = lines.split(MSG_DO_NOT_EDIT)[0].strip()
            if MSG_DO_NOT_EDIT_OLD in lines:
                lines = lines.split(MSG_DO_NOT_EDIT_OLD)[0].strip()

            lines = lines.splitlines()

        updated_rst = []
        s_pattern = re.compile(r"(?<!\.\. )\|([\w\d-]+)\|")


        local_substitutes = {s.name:s for s in self.readSubstitutionDefinitions(path_rst)}
        global_substitutes = []

        missing_substitute_definitions = []
        for i, line in enumerate(lines):
            for r in s_pattern.findall(line):
                if r not in local_substitutes:
                    missing_substitute_definitions.append([i+1, line, r])

        if len(missing_substitute_definitions) > 0:
            print(f'Update {path_rst}')
            updated_rst += lines + [f'\n\n{MSG_DO_NOT_EDIT}\n']
            for (lno, line, r) in sorted(missing_substitute_definitions, key=lambda x: x[2]):

                if r in local_substitutes:
                    continue
                    # sub = local_substitutes[r]
                elif r in self:
                    sub = self[r]
                else:
                    warnings.warn(f'Missing definition for "{r}"\nFile "{path_rst}":{lno}, \nin "{line}".'
                                  f'Either add definition to file or scripts/substitutions.txt')
                    continue

                if sub.name not in global_substitutes:
                    rst_code = self.toRST(sub,
                                          copy_icon=True,
                                          path_rst=path_rst if relative_paths else None)
                    updated_rst.append(rst_code)
                    global_substitutes.append(sub.name)
                s = ""
            # add final newline
            updated_rst.append('')
            with open(path_rst, 'w', encoding='utf-8') as f:
                f.write('\n'.join(updated_rst))
            s = ""

    def print(self):
        for s in self.mSubstitutes.values():
            print(self.toRST(s))

    def inkscapeBin(self) -> Path:

        if self.mPathInkscapeBin is None:
            self.mPathInkscapeBin = inkscapeBin()
        return self.mPathInkscapeBin

    def toRST(self,
              sub: Substitute,
              copy_icon: bool = False,
              path_rst: Optional[Path] = None) -> str:
        """
        Create the substitute definition
        :param sub: Substitute
        :param copy_icon: set True to copy icon files (*.svg, *.png) into the loca SOURCE/icons directory, if necessary
        :param path_rst: if set to the path of the rst file, the substitute code will use a relative icon path
        :return: str with substitue code, e.g.
            .. |icon| image:: /icons/icon.png
               :width: 28px
        """

        if sub.stype == SourceType.Raw:
            return sub.definition

        elif sub.stype == SourceType.Link:
            # .. |Bitbucket| replace:: `Bitbucket <https://bitbucket.org>`__
            return f'.. |{sub.name}| replace:: `{sub.definition}`__'

        elif sub.stype == SourceType.Icon:
            # .. |classinfo_remove| image:: icons/classinfo_remove.png
            #    :width: 28px
            assert isinstance(sub.icon_path, Path)
            if sub.icon_path.is_absolute():
                assert sub.icon_path.is_file()
            else:
                assert (self.mSourceRoot / sub.icon_path).is_file()

            if not isSubDir(self.mSourceRoot, sub.icon_path):
                if copy_icon:
                    path_src = sub.icon_path
                    path_png = DIR_ICONS / f'{path_src.stem}.png'
                    if path_src.name.endswith('.svg'):
                        print(f'Convert {path_src}\n\tto {path_png}')
                        cmd = [
                            #  'inkscape',
                            f'{self.inkscapeBin()}',
                            '--export-type=png',
                            '--export-area-page',
                            f'--export-filename={path_png}',
                            f'{path_src}'
                        ]
                        subprocess.run(cmd, check=True)
                    elif path_src.name.endswith('.png'):
                        print(f'Copy {path_src}\n\tto {path_png}')
                        shutil.copy(path_src, path_png)
                    else:
                        raise NotImplementedError(f'Unsupported icon type: {path_src}')

                    sub.icon_path = path_png
                else:
                    warnings.warn(f'Icon does not exist in rst source folder: {sub.icon_path}')

            if isinstance(path_rst, Path):
                path_rel = sub.icon_path.relative_to(path_rst, walk_up=True)
            else:
                path_rel = sub.icon_path.relative_to(self.mSourceRoot)

            return '\n'.join([
                f'.. |{sub.name}| image:: /{path_rel.as_posix()}',
                f'   :width: {self.mIconSize}px'
            ])

        else:
            raise NotImplementedError()





def add_api_definitions(collection: SubstituteCollection):
    # add manual links

    # autogenerated singular forms
    objects = []
    for module in [
        qgis,
        qgis.core,
        qgis.gui,
        qgis.PyQt.QtCore,
        qgis.PyQt.QtWidgets,
        qgis.PyQt.QtGui,
    ]:
        for key in module.__dict__.keys():
            if re.search('^(Qgs|Q)', key):
                objects.append(key)

    rx_qgis = re.compile('^Qgs|Qgis.*')
    objects = sorted(set(objects))
    for i, obj in enumerate(objects):
        if obj in ['QtCore', 'QtGui', 'QtWidget']:
            continue
        target = None
        if rx_qgis.match(obj):
            # https://qgis.org/api/classQgsProject.html
            target = "https://api.qgis.org/api/class{}.html".format(obj)
        elif obj.startswith('Q'):
            # https://doc.qt.io/qt-5/qwidget.html
            target = "https://doc.qt.io/qt-5/{}.html".format(obj.lower())

        if target is None:
            continue

        # singular + plural form
        names = [obj, obj + 's']
        for name in names:
            if name.endswith('ss'):
                continue
            if name not in collection.mSubstitutes.keys():
                collection.addLinkSubstitute(name, f'{name} <{target}>')


MSG_DO_NOT_EDIT = '.. AUTOGENERATED SUBSTITUTIONS - DO NOT EDIT PAST THIS LINE'
MSG_DO_NOT_EDIT_OLD = '.. Substitutions definitions - AVOID EDITING PAST THIS LINE'

def find_by_ext(folder, extension) -> List[Path]:
    """
    create list with absolute paths to all *.extension files inside
    folder and its sub-folders
    """
    found_files = [Path(dirpath) / f
                   for dirpath, dirnames, files in walk(folder)
                   for f in files if f.endswith('.' + extension)]
    return found_files


if __name__ == '__main__':
    collection = SubstituteCollection(DIR_SOURCE, dir_rst_icons=DIR_ICONS)

    path_manual = Path(__file__).parent / 'substitutions.txt'
    collection.addManualDefinitions(path_manual)
    add_api_definitions(collection)
    for d in ICON_DIRS:
        print(f'Read icons from {d}')
        collection.readIcons(d)

    #collection.updateRST(
    #    r'D:\Repositories\enmap-box-documentation\source\usr_section\usr_cookbook\graphical_modeler.rst')

    for file in find_by_ext(DIR_SOURCE, 'rst'):
        collection.updateRST(file)

    # collection.print()
