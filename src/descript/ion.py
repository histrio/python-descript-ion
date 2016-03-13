"""
File: ion.py
Author: Rinat F Sabitov
Email: rinat.sabitov@gmail.com
Description: simple library that provides access to DESCRIPT.ION files
"""

import os
import errno

DESCRIPTION_FILE = 'descript.ion'

native_open = open


def open(*args, **kwargs):
    result = native_open(*args, **kwargs)
    return DescriptionedFileObject(result)


def locate_decription_file(filename):
    cwd = os.path.dirname(filename)
    alt = (fn for fn in os.listdir(cwd) if fn.lower() == DESCRIPTION_FILE)
    return os.path.join(cwd, next(alt, DESCRIPTION_FILE))


class Description(object):

    def __getitem__(self, key):
        dfile = locate_decription_file(key)
        with native_open(dfile, 'r') as f:
            return f.read()

    def __setitem__(self, key, value):
        dfile = locate_decription_file(key)
        with native_open(dfile, 'w') as f:
            return f.write(value)

    def __delitem__(self, key):
        pass

    def __get__(self, obj, objtype):
        return self[obj.name]

    def __set__(self, obj, val):
        self[obj.name] = val

    def __delete__(self, obj):
        dfile = locate_decription_file(obj.name)
        try:
            os.remove(dfile)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

    def __contains__(self, key):
        return False


class DescriptionedFileObject(object):

    description = Description()

    def __init__(self, fileobject):
        self.fileobject = fileobject

    def __getattr__(self, attr):
        return getattr(self.fileobject, attr)

    def __enter__(self):
        self.fileobject = self.fileobject.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        return self.fileobject.__exit__(*args, **kwargs)
