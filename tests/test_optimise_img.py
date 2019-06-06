import setup_paths
import unittest
from optimise_img import Optimise
from img_extensions import keys

import os

cwd = os.path.dirname(os.path.realpath(__file__))
resources = os.path.join(cwd, 'resources')
text_outputs = os.path.join(cwd, 'test_outputs')

class TestOptimise(unittest.TestCase):

    def setUp(self):
        os.mkdir(text_outputs)

    def test_1(self):
        print(os.path.isdir(text_outputs))
        self.assertEquals(5, 5)

    def test_6(self):
        print(os.path.isdir(text_outputs))
        self.assertEquals(5, 5)

    def test_5(self):
        self.assertEquals(5, 5)

    def test_4(self):
        self.assertEquals(5, 5)

    def test_3(self):
        self.assertEquals(5, 5)

    def test_2(self):
        self.assertEquals(5, 5)

    def tearDown(self):
        os.rmdir(text_outputs)

if __name__ == '__main__':
    unittest.main()