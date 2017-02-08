import unittest
import os
from .sas1 import SAS1
from .sas3 import SAS3
from .sas3_extended import SAS3Extended

class TestSas(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_sas1(self):
        file_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = 'sas1_test_cases/miconic1-0.sas'
        abs_file_path = os.path.join(file_dir, rel_path)
        sas = SAS1.from_file(abs_file_path)
        with open(abs_file_path,'r') as f:
            self.assertEqual(str(sas),f.read())

    def test_sas3(self):
        file_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = 'sas3_test_cases/gripper_prob01.sas'
        abs_file_path = os.path.join(file_dir, rel_path)
        sas = SAS3.from_file(abs_file_path)
        with open(abs_file_path,'r') as f:
            self.assertEqual(str(sas),f.read())

    def test_sas3_extended(self):
        file_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = 'sas3_test_cases/gripper_prob01.sas'
        abs_file_path = os.path.join(file_dir, rel_path)
        sas = SAS3Extended.from_file(abs_file_path)
        with open(abs_file_path,'r') as f:
            self.assertEqual(str(sas),f.read())

    def test_sas3_extracted(self):
        file_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = 'sas3_test_cases/gripper_prob01_extracted.sas'
        abs_file_path = os.path.join(file_dir, rel_path)
        sas = SAS3Extended.from_file(abs_file_path)
        with open(abs_file_path,'r') as f:
            self.assertEqual(str(sas),f.read())

    def test_sas3_specified(self):
        file_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        orig_rel_path = 'sas3_test_cases/gripper_prob01.sas'
        target_rel_path = 'sas3_test_cases/gripper_prob01_specified.sas'

        orig_file_path = os.path.join(file_dir, orig_rel_path)
        target_file_path = os.path.join(file_dir, target_rel_path)
        sas = SAS3Extended.from_file(orig_file_path)
        copied = sas.to_fully_specified(False)
        with open(target_file_path,'r') as f:
            self.assertEqual(str(copied),f.read())

if __name__ == '__main__':
    unittest.main()
