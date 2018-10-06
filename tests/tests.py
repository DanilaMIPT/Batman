import app.helper as lib
import unittest

class TestMyFunc(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(lib.multiply(2, 3), 6)

    def test_mult_n0_is0(self):
        self.assertEqual(lib.multiply(2, 0), 0)
