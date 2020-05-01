"""
File: ion.py
Author: Rinat F Sabitov
Email: rinat.sabitov@gmail.com
Description: simple library that provides access to DESCRIPT.ION files
"""

import os
import tempfile
from shutil import copyfile

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


def parse_line(line):
    if line.startswith('"'):
        head, tail = line[line.index('"') + 1:line.rindex('"')], line[line.rindex('"') + 1:]
    else:
        head, tail = line.split(' ', 1)
    return head.strip(), tail.strip()


def normalize_key(clbl):

    def wrapper(key, *args, **kwargs):
        dfile = locate_decription_file(key)
        key = os.path.basename(key)
        return clbl(dfile, key, *args, **kwargs)

    return wrapper


@normalize_key
def delete_key(dfile, key):
    if not os.path.isfile(dfile):
        return
    with tempfile.NamedTemporaryFile('w+') as dst:
        with native_open(dfile, 'r') as src:
            for line in src:
                head, tail = parse_line(line)
                if head != key:
                    dst.write(line)
            dst.flush()
        copyfile(dst.name, dfile)


@normalize_key
def add_key(dfile, key, value):
    with native_open(dfile, 'a') as fh:
        if " " in key:
            key = '"' + key + '"'
        line = key + ' ' + value + '\n'
        fh.write(line)


@normalize_key
def get_key(dfile, key):
    with native_open(dfile, 'r') as dfile:
        for line in dfile:
            head, tail = parse_line(line)
            if head == key:
                return tail


class Description(object):

    def __getitem__(self, key):
        return get_key(key)

    def __setitem__(self, key, value):
        del self[key]
        add_key(key, value)

    def __delitem__(self, key):
        delete_key(key)

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
