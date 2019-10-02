"""
File: test_descript_ion_unit.py
Author: Rinat F Sabitov
Description:
"""

import unittest
from src.descript import ion
import tempfile


tmp_file, tmp_filename = tempfile.mkstemp()
tmp_file2, tmp_filename2 = tempfile.mkstemp()
description = 'test description'

def test_descripions_as_dict():
    descriptions = ion.Description()
    descriptions[tmp_filename] = description
    assert descriptions[tmp_filename] == description

def test_read_write():
    try:
        f = ion.open(tmp_filename, 'r')
        f.description = description
        assert f.description == description
    finally:
        del f.description
        f.close()

def test_read_write_with_context():
    with ion.open(tmp_filename) as f:
        f.description = description

    with ion.open(tmp_filename) as f:
        assert f.description == description
        del f.description

def test_read_write_binary():
    with ion.open(tmp_filename, 'wb') as f:
        f.description = description

    with ion.open(tmp_filename, 'rb') as f:
        assert f.description == description
        del f.description

def test_read_write_with_two_files():
    try:
        f = ion.open(tmp_filename, 'r')
        f2 = ion.open(tmp_filename2, 'r')
        f.description = description
        f2.description = description+'2'

        assert f.description == description
        assert f2.description == description+'2'
    finally:
        del f.description
        del f2.description
        f.close()
        f2.close()

def test_read_write_with_file_with_spaces_in_name():
    with ion.open(tmp_filename+' test', 'a+') as f:
        f.description = description
        assert f.description == description
        del f.description
