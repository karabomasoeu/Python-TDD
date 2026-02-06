import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
