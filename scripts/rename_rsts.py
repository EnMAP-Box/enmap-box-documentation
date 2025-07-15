import re
import shutil
from pathlib import Path

from scripts.utils import file_search

ROOT = Path(r'D:\Repositories\enmap-box-documentation\source\usr_section\usr_manual\processing_algorithms')

for p_old in file_search(ROOT, '*.rst', recursive=True):
    p_old = Path(p_old)
    stem = p_old.stem

    stem2 = re.sub(r'[/()\-_ ]+', '_', stem)
    stem2 = re.sub('_$', '', stem2)

    if stem != stem2:
        p_new = p_old.parent / (stem2 + '.rst')
        shutil.move(p_old, p_new)
        print(f'Corrected: {p_new}')

    s = ""
