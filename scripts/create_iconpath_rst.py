import pathlib
import re
import os
import shutil
from os.path import basename, splitext, getmtime
from utils import file_search

# source dir (location of conf.py)

# Repo for EnMAP-Box documentation
DIR_REPO = pathlib.Path(__file__).parents[1]
DIR_SOURCE = DIR_REPO / 'source'

DIR_ICONS = DIR_SOURCE / 'img' / 'icons'
assert DIR_SOURCE.is_dir(), 'Documentation source directory does not exist'
assert DIR_ICONS.is_dir(), 'Documentation source icon directory does not exist'

if os.environ.get('ENMAPBOX_REPO'):
    DIR_ENMAPBOX_REPO = \
        pathlib.Path(os.environ.get('ENMAPBOX_REPO', '<missing>'))
else:
    # assume that repositories for EnMAP-Box documentation and
    # EnMAP-Box source code are in the same directory
    DIR_ENMAPBOX_REPO = DIR_REPO.parent / 'enmap-box'
assert DIR_ENMAPBOX_REPO.is_dir(), 'EnMAP-Box Repo not defined / not found'

ENMAPBOX_ICON_DIRS = \
    [DIR_ENMAPBOX_REPO / 'enmapbox/gui/ui/icons',
     DIR_ENMAPBOX_REPO / 'enmapbox/qgispluginsupport/qps/ui/icons']

PATH_RST = DIR_SOURCE / 'icon_links.rst'
rx_extensions = re.compile(r'\.(svg|png)$')

ICONS = dict()


def iconRstLink(path):
    return re.sub(r'[ \.]', '_', splitext(basename(path))[0])


for file in file_search(DIR_ICONS, rx_extensions):
    ICONS[iconRstLink(file)] = file

for iconDir in ENMAPBOX_ICON_DIRS:
    for file in file_search(iconDir, rx_extensions):
        linkName = iconRstLink(file)
        copyIcon = False
        if linkName not in ICONS:
            copyIcon = True
        else:
            # compare time stamp
            tSrc = getmtime(file)
            tDocs = getmtime(ICONS[linkName])
            if tSrc > tDocs:
                copyIcon = True

        if copyIcon:
            print(f'Copy {file}')
            file2 = DIR_ICONS / basename(file)
            shutil.copyfile(file, file2)
            ICONS[linkName] = file2

lines = []
for linkName, path in ICONS.items():
    relPath = pathlib.Path(path).relative_to(PATH_RST.parent).as_posix()
    lines.append(f'.. |{linkName}| image:: /{relPath}\n   :width: 28px')

# write rst file
with open(PATH_RST, 'w', encoding='utf-8', newline='') as f:
    f.write('\n'.join(lines))
