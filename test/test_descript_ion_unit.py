"""
File: test_descript_ion_unit.py
Author: Rinat F Sabitov
Description:
"""

import unittest
import descript.ion
import tempfile


class DescriptIonTest(unittest.TestCase):

    def setUp(self):
        self.tmp_file, self.tmp_filename = tempfile.mkstemp()
        self.tmp_file2, self.tmp_filename2 = tempfile.mkstemp()
        self.description = 'test description'

    def test_descripions_as_dict(self):
        descriptions = descript.ion.Description()
        descriptions[self.tmp_filename] = self.description
        self.assertEqual(descriptions[self.tmp_filename], self.description)

    def test_read_write(self):
        try:
            f = descript.ion.open(self.tmp_filename, 'r')
            f.description = self.description
            self.assertEqual(f.description, self.description)
        finally:
            del f.description
            f.close()

    def test_read_write_with_context(self):
        with descript.ion.open(self.tmp_filename) as f:
            f.description = self.description

        with descript.ion.open(self.tmp_filename) as f:
            self.assertEqual(f.description, self.description)
            del f.description

    def test_read_write_binary(self):
        with descript.ion.open(self.tmp_filename, 'wb') as f:
            f.description = self.description

        with descript.ion.open(self.tmp_filename, 'rb') as f:
            self.assertEqual(f.description, self.description)
            del f.description

    def test_read_write_with_two_files(self):
        try:
            f = descript.ion.open(self.tmp_filename, 'r')
            f2 = descript.ion.open(self.tmp_filename2, 'r')
            f.description = self.description
            f2.description = self.description+'2'

            self.assertEqual(f.description, self.description)
            self.assertEqual(f2.description, self.description+'2')
        finally:
            del f.description
            del f2.description
            f.close()
            f2.close()

    def test_read_write_with_file_with_spaces_in_name(self):
        with descript.ion.open(self.tmp_filename+' test', 'a+') as f:
            f.description = self.description
            self.assertEqual(f.description, self.description)
            del f.description


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(DescriptIonTest)
    unittest.TextTestRunner(verbosity=2).run(tests)
