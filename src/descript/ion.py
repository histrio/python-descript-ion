"""
File: ion.py
Author: Rinat F Sabitov
Email: rinat.sabitov@gmail.com
Description: simple library that provides access to DESCRIPT.ION files
"""

import os.path
import StringIO

DESCRIPTION_FILE = 'descript.ion'


def is_description_file(filename):
    return (os.path.isfile(filename)
        and os.path.basename(filename).lower() == DESCRIPTION_FILE)


def _get_description_filename(target_file):
    descript_path = os.path.dirname(os.path.abspath(target_file))
    try:
        result, = [dfile for dfile in os.listdir(descript_path)
            if is_description_file(dfile)]
    except ValueError:
        result = os.path.join(descript_path, DESCRIPTION_FILE)
    return result


def load_description_file(filename):
    import shlex
    result = {}
    if os.path.isfile(filename):
        with open(filename, 'r') as descript_file:
            for line in descript_file:
                lexer = shlex.shlex(line)
                key = lexer.get_token()
                value = ' '.join(list(lexer))
                result[key] = value
    return result

def save_description_file(filename, desc):
    with open(filename, 'w') as descript_file:
        for k, v in desc.items():
            if ' ' in k:
                k = '"' + k + '"'
            line = "%s %s\r\n" % (k, v)
            descript_file.write(line)



def dumps(target_file, description):
    description_filename = _get_description_filename(target_file)
    desc = load_description_file(description_filename)
    desc[os.path.basename(target_file)] = description
    save_description_file(description_filename, desc)


def loads(target_file):
    description_filename = _get_description_filename(target_file)
    desc = load_description_file(description_filename)
    return desc.get(os.path.basename(target_file))


class Description(object):

    def __init__(self, target_file, *args, **kwargs):
        self.target_file = target_file
        self._file = StringIO.StringIO()
        self._file.write(loads(target_file))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self, *args, **kwargs):
        return self._file.close()

    def flush(self):
        return self._file.flush()

    def isatty(self):
        return self._file.isatty()

    def next(self):
        return self._file.next()

    def read(self, *args, **kwargs):
        self._file.seek(0)
        return self._file.read(*args, **kwargs)

    def readline(self, *args, **kwargs):
        return self._file.readline(*args, **kwargs)

    def seek(self, *args, **kwargs):
        return self._file.seek(*args, **kwargs)

    def write(self, *args, **kwargs):
        result = self._file.write(*args, **kwargs)
        self._file.seek(0)
        dumps(self.target_file, self._file.read())
        return result




def dopen(target_file, *args, **kwargs):
    return Description(target_file, *args, **kwargs)
    #description_filename = _get_description_filename(target_file)
    #return open(description_filename, 'w+')
