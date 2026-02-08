import unittest
from calculator import add
from calculator import sub

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
