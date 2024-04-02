# noinspection PyPep8Naming
import os
import pathlib
import re
import site
from utils import file_search

DIR_REPO = pathlib.Path(__file__).parents[1]
site.addsitedir(DIR_REPO / 'scripts')


def ensure_lowercase_file_extensions():
    DIR_DOCS = pathlib.Path(DIR_REPO) / 'source'
    rxUpercase = re.compile(r'\.(?P<ext>(PNG|JPEG))$')
    for path in file_search(DIR_DOCS, rxUpercase, recursive=True):
        p, ext = os.path.splitext(path)
        new_path = p + ext.lower()
        print(f'rename: {path}')
        os.rename(path, new_path)


if __name__ == "__main__":
    ensure_lowercase_file_extensions()
