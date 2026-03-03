import unittest
from src.utils.helper import validate_number

class TestHelper(unittest.TestCase):

    def test_validate_number_valid(self):
        self.assertEqual(validate_number("10"), 10)

    def test_validate_number_invalid(self):
        with self.assertRaises(ValueError):
            validate_number("abc")

if __name__ == "__main__":
    unittest.main()