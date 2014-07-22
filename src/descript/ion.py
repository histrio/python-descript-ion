"""
File: ion.py
Author: Rinat F Sabitov
Email: rinat.sabitov@gmail.com
Description: simple library that provides access to DESCRIPT.ION files
"""

import os.path

DESCRIPTION_FILE = 'descript.ion'


def is_description_file(filename):
    return os.path.isfile(filename) and os.path.basename(filename).lower() == DESCRIPTION_FILE


def _get_description_filename(target_file):
    descript_path = os.path.dirname(os.path.abspath(target_file))
    try:
        result, = [dfile for dfile in os.listdir(descript_path) if is_description_file(dfile)]
    except ValueError:
        result = os.path.join(descript_path, DESCRIPTION_FILE)
    return result


def dumps(target_file, description):
    description_filename = _get_description_filename(target_file)
    with open(description_filename, 'wa') as descript_file:
        descript_file.write(description)


def loads(target_file):
    description_filename = _get_description_filename(target_file)
    with open(description_filename, 'r') as descript_file:
        result = descript_file.read()
    return result


def dopen(target_file):
    description_filename = _get_description_filename(target_file)
    return open(description_filename, 'r+')
