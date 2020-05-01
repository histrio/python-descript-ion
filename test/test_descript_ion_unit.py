"""
File: test_descript_ion_unit.py
Author: Rinat F Sabitov
Description:
"""
import pytest


import descript.ion


# tmp_file, tmp_filename = tempfile.mkstemp()
# tmp_file2, tmp_filename2 = tempfile.mkstemp()
# description = 'test description'

test_descriptions = [
    "test description",
]


@pytest.fixture
def tmp_filename(tmpdir, request):
    filename = '{0}.txt'.format(request.fixturename)
    tmp_file = tmpdir.join(filename)
    tmp_file.write('some file')
    return str(tmp_file)


tmp_filename2 = tmp_filename


@pytest.mark.parametrize('description', test_descriptions)
def test_descripions_as_dict(tmp_filename, description):
    descriptions = descript.ion.Description()
    descriptions[tmp_filename] = description
    assert descriptions[tmp_filename] == description


@pytest.mark.parametrize('description', test_descriptions)
def test_read_write(description, tmp_filename):
    f = descript.ion.open(tmp_filename, 'r')
    try:
        f.description = description
        assert f.description == description
    finally:
        del f.description
        f.close()


@pytest.mark.parametrize('description', test_descriptions)
def test_read_write_with_context(tmp_filename, description):
    with descript.ion.open(tmp_filename) as f:
        f.description = description

    with descript.ion.open(tmp_filename) as f:
        assert f.description == description
        del f.description


@pytest.mark.parametrize('description', test_descriptions)
def test_read_write_binary(description, tmp_filename):
    with descript.ion.open(tmp_filename, 'wb') as f:
        f.description = description

    with descript.ion.open(tmp_filename, 'rb') as f:
        assert f.description == description
        del f.description


@pytest.mark.parametrize('description', test_descriptions)
def test_read_write_with_two_files(description, tmp_filename, tmp_filename2):
    try:
        f = descript.ion.open(tmp_filename, 'r')
        f2 = descript.ion.open(tmp_filename2, 'r')
        f.description = description
        f2.description = description + '2'

        assert f.description == description
        assert f2.description == description + '2'
    finally:
        del f.description
        del f2.description
        f.close()
        f2.close()


@pytest.mark.parametrize('description', test_descriptions)
def test_read_write_with_file_with_spaces_in_name(description, tmp_filename):
    with descript.ion.open(tmp_filename + ' test', 'a+') as f:
        f.description = description
        assert f.description == description
        del f.description
