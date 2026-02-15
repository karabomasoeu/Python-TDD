import unittest 
from FizzBuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_returns_one_for_one(self):
        result = fizzbuzz(1)
        self.assertEqual(result, "1")

if __name__ == '__main__':
    unittest.main()
