import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("king"))

    def test_validate_name_with_valid_input_string_of_int(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_valid_input_contained_string_of_int(self):
        self.assertEqual(False, validate_name("king1234"))

    def test_validate_name_with_valid_input_spacial_char(self):
        self.assertEqual(True, validate_name("F"))

    def test_validate_name_with_valid_input_empty_char(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_valid_input_space_char(self):
        self.assertEqual(False, validate_name("ff fff"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
