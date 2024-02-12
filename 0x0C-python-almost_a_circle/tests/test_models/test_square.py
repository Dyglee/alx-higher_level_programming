#!/usr/bin/python3

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_creation(self):
        """Test normal creation with no errors."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_area(self):
        """Test the area method."""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_update_args(self):
        """Test the update method using *args."""
        s1 = Square(5, 0, 0, 1)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(s1_dict, expected)

if __name__ == "__main__":
    unittest.main()
