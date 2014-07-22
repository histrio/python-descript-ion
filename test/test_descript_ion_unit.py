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
        self.description = 'test description'

    def test_read_write(self):
        descript.ion.dumps(self.tmp_filename, self.description)
        self.assertEqual(descript.ion.loads(self.tmp_filename),
            self.description)

    def test_description_file_wrapper(self):
        with descript.ion.dopen(self.tmp_filename, 'w') as descript_file:
            descript_file.write(self.description)
        with descript.ion.dopen(self.tmp_filename, 'r') as descript_file:
            self.assertEqual(descript_file.read(), self.description)

    def test_two_files(self):
        self.tmp2_file, self.tmp2_filename = tempfile.mkstemp()
        self.description2 = 'test description2'

        descript.ion.dumps(self.tmp_filename, self.description)
        descript.ion.dumps(self.tmp2_filename, self.description2)
        self.assertEqual(descript.ion.loads(self.tmp_filename),
            self.description)
        self.assertEqual(descript.ion.loads(self.tmp2_filename),
            self.description2)

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(DescriptIonTest)
    unittest.TextTestRunner(verbosity=2).run(tests)
