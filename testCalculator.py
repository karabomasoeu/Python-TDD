import unittest
from calculator import add, sub, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-1, -1)
        self.assertEqual(result, -2)

    def test_sub_two_numbers(self):
        result = sub(3, 2)
        self.assertEqual(result, 1)

    def test_sub_negative_numbers(self):
        result = sub(-1, -1)
        self.assertEqual(result, 0)

    def test_multiply_positive_numbers(self):
        result = multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiply_by_zero(self):
        result = multiply(0, 5)
        self.assertEqual(result, 0)

    def test_multiply_negative_numbers(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)

    def test_divide_positive_numbers(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)

    def test_divide_negative_numbers(self):
        result = divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_by_zero(self):
        result = divide(0, 6)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
