from app.helper import multiply, add
import unittest

class TestMyFunc(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_mult_n0_is0(self):
        self.assertEqual(add(2, 0), 2)
