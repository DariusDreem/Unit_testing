import unittest
from Password_validator import basic_test, intermediate_test, advanced_test


class TestBasicValidation(unittest.TestCase):
    """Tests pour la validation basique du mot de passe."""

    def test_valid_password(self):
        self.assertTrue(basic_test("Password123"))

    def test_valid_complex_password(self):
        self.assertTrue(basic_test("MySecurePassword123!"))

    def test_no_uppercase(self):
        self.assertFalse(basic_test("password123"))

    def test_no_lowercase(self):
        self.assertFalse(basic_test("PASSWORD123"))

    def test_no_digit(self):
        self.assertFalse(basic_test("Password"))

    def test_too_short(self):
        self.assertFalse(basic_test("Pa1"))

    def test_no_digit_with_special(self):
        self.assertFalse(basic_test("Password!"))


class TestIntermediateValidation(unittest.TestCase):
    """Tests pour la validation intermédiaire du mot de passe."""

    def test_no_special_character(self):
        self.assertFalse(intermediate_test("Password123"))

    def test_valid_with_special(self):
        self.assertTrue(intermediate_test("MySecureP@ssword123!"))

    def test_too_long(self):
        self.assertFalse(intermediate_test("P@ssw0rd12345678901234567890"))

    def test_max_length(self):
        self.assertTrue(intermediate_test("P@ssw0rd123456789012"))

    def test_contains_whitespace(self):
        self.assertFalse(intermediate_test("P@ssw0rd   "))

    def test_three_identical_chars(self):
        self.assertFalse(intermediate_test("P@ssw0rd!!!"))


class TestAdvancedValidation(unittest.TestCase):
    """Tests pour la validation avancée du mot de passe."""

    def test_simple_password_rejected(self):
        self.assertEqual(advanced_test("Password123"), "Too Simple")

    def test_very_strong_password(self):
        self.assertEqual(advanced_test("MySecureP@ssword123!"), "Very Strong")

    def test_weak_password(self):
        self.assertEqual(advanced_test("passord"), "Weak")

    def test_medium_password(self):
        self.assertEqual(advanced_test("pasw0rd"), "Medium")


if __name__ == "__main__":
    unittest.main()