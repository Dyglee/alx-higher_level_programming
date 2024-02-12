#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""
    
    def test_rectangle_creation(self):
        """Test normal creation with no errors."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        
    def test_area(self):
        """Test the area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        
    def test_update_args(self):
        """Test the update method using *args."""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        
    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertDictEqual(r1_dict, expected)

if __name__ == "__main__":
    unittest.main()
