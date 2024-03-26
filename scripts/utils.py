import fnmatch
import os
import re


def file_search(rootdir,
                pattern,
                recursive: bool = False,
                ignoreCase: bool = False,
                directories: bool = False,
                fullpath: bool = False):
    """
    Searches for files or folders
    :param rootdir: root directory to search in
    :param pattern: wildcard ("my*files.*") or regular expression that describes the file or folder name.
    :param recursive: set True to search recursively.
    :param ignoreCase: set True to ignore character case.
    :param directories: set True to search for directories/folders instead of files.
    :param fullpath: set True if the entire path should be evaluated and not the file name only
    :return: enumerator over file paths
    """
    assert os.path.isdir(rootdir), "Path is not a directory:{}".format(rootdir)
    regType = type(re.compile('.*'))

    for entry in os.scandir(rootdir):
        if directories is False:
            if entry.is_file():
                if fullpath:
                    name = entry.path
                else:
                    name = os.path.basename(entry.path)
                if isinstance(pattern, regType):
                    if pattern.search(name):
                        yield entry.path.replace('\\', '/')

                elif (ignoreCase and fnmatch.fnmatch(name, pattern.lower())) \
                        or fnmatch.fnmatch(name, pattern):
                    yield entry.path.replace('\\', '/')
            elif entry.is_dir() and recursive is True:
                for r in file_search(entry.path, pattern, recursive=recursive, directories=directories):
                    yield r
        else:
            if entry.is_dir():
                if recursive is True:
                    for d in file_search(entry.path, pattern, recursive=recursive, directories=directories):
                        yield d

                if fullpath:
                    name = entry.path
                else:
                    name = os.path.basename(entry.path)
                if isinstance(pattern, regType):
                    if pattern.search(name):
                        yield entry.path.replace('\\', '/')

                elif (ignoreCase and fnmatch.fnmatch(name, pattern.lower())) \
                        or fnmatch.fnmatch(name, pattern):
                    yield entry.path.replace('\\', '/')
