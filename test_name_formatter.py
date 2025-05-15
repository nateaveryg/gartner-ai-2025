import unittest
from name_formatter import format_name

class TestFormatName(unittest.TestCase):

    def test_name_with_no_middle_initial(self):
        """Test formatting for names without a middle initial."""
        self.assertEqual(format_name("John", "Doe"), "John Doe")
        self.assertEqual(format_name("Alice", "Smith", middle_initial=None), "Alice Smith")
        self.assertEqual(format_name("Bob", "Johnson", middle_initial=""), "Bob Johnson")
        self.assertEqual(format_name("Charlie", "Brown", middle_initial="   "), "Charlie Brown")

    def test_name_with_capitalized_middle_initial(self):
        """
        Test formatting for names with a capitalized middle initial.
        The initial should be followed by a period.
        """
        self.assertEqual(format_name("Jane", "Doe", "M"), "Jane M. Doe")
        self.assertEqual(format_name("David", "Lee", "R"), "David R. Lee")
        # Test with surrounding spaces
        self.assertEqual(format_name("Eve", "Adams", " S "), "Eve S. Adams")
        # Test with capitalized initial already followed by a period (should normalize)
        self.assertEqual(format_name("Clark", "Kent", "S."), "Clark S. Kent")
        # Test with multi-character capitalized initial (should take first char)
        self.assertEqual(format_name("Bruce", "Wayne", "BATMAN"), "Bruce B. Wayne")

    def test_name_with_lowercase_middle_initial(self):
        """
        Test formatting for names with a lowercase middle initial.
        The middle initial should be capitalized and followed by a single period, like 'A.'.
        """
        self.assertEqual(format_name("Peter", "Pan", "p"), "Peter P. Pan")
        self.assertEqual(format_name("Olivia", "Jones", "o"), "Olivia O. Jones")
        # Test with surrounding spaces
        self.assertEqual(format_name("Samuel", "Clark", " t "), "Samuel T. Clark")
        # Test with lowercase initial already followed by a period (should normalize and capitalize)
        self.assertEqual(format_name("Walter", "White", "w."), "Walter W. White")
        # Test with multi-character lowercase initial (should take first char and capitalize)
        self.assertEqual(format_name("Max", "Power", "danger"), "Max D. Power")
        # Test another simple lowercase initial
        self.assertEqual(format_name("Sarah", "Connor", "j"), "Sarah J. Connor")


if __name__ == '__main__':
    unittest.main()
