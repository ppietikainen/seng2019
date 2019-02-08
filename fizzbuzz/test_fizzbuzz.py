import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_return_number_as_string(self):
        self.assertEqual(FizzBuzz("1"), "1")

if __name__ == '__main__':
    unittest.main()

