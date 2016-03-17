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
    result = os.path.join(cwd, next(alt, DESCRIPTION_FILE))
    return result


def delete_key_from_file(fh, key):
    pos = 0
    for line in fh:
        head, tail = line.split(' ', 1)
        if head != key:
            fh.seek(pos)
            fh.write(line)
            pos = fh.tell()
    fh.truncate()


class Description(object):

    def __getitem__(self, key):
        dfile = locate_decription_file(key)
        with native_open(dfile, 'r') as f:
            for line in f:
                head, tail = line.split(' ', 1)
                if head == key:
                    return tail.rstrip('\n')

    def __setitem__(self, key, value):
        dfile = locate_decription_file(key)
        with native_open(dfile, 'a+') as f:
            delete_key_from_file(f, key)
            f.write(key+' '+value+'\n')

    def __delitem__(self, key):
        dfile = locate_decription_file(key)
        with native_open(dfile, 'a+') as fh:
            delete_key_from_file(fh, key)

    def __get__(self, obj, objtype):
        return self[obj.name]

    def __set__(self, obj, val):
        self[obj.name] = val

    def __delete__(self, obj):
        del self[obj.name]

    def __contains__(self, key):
        return False


class DescriptionedFileObject(object):

    description = Description()

    def __init__(self, fileobject):
        self.fileobject = fileobject

    def __getattr__(self, attr):
        return getattr(self.fileobject, attr)

    def __enter__(self, *args, **kwargs):
        self.fileobject = self.fileobject.__enter__(*args, **kwargs)
        return self

    def __exit__(self, *args, **kwargs):
        return self.fileobject.__exit__(*args, **kwargs)
