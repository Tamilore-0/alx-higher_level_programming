import sys
from io import StringIO
import unittest
from models.square import Square
from models.base import Base


# custom assert function to test printed output
def assertPrints(test_case, expected_output, func, *args, **kwargs):
    """
    Asserts that calling a function prints the expected output to stdout.

    Args:
        test_case (unittest.TestCase): The test case instance.
        expected_output (str): The expected output that should be printed.
        func (callable): The function to be tested.
        *args: Positional arguments to be passed to the function.
        **kwargs: Keyword arguments to be passed to the function.
    """
    captured_output = StringIO()
    sys.stdout = captured_output
    try:
        func(*args, **kwargs) # args and kwargs if other variables are needed for execution
        captured_output.seek(0)
        actual_output = captured_output.read()
        test_case.assertEqual(expected_output, actual_output)
    finally:
        sys.stdout = sys.__stdout__


class TestSquare(unittest.TestCase):

    def test_create_square(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_create_square_with_position(self):
        square = Square(3, 2, 1)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)
        self.assertIsNotNone(square.id)

    def test_create_square_with_id(self):
        square = Square(4, id=7)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 7)

    def test_size_property(self):
        square = Square(6)
        self.assertEqual(square.size, 6)

        square.size = 8
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_str_representation(self):
        square = Square(5, 2, 3, 1)
        square.id = 1
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_str_representation_no_id(self):
        square = Square(4, 1, 1)
        expected_output = "[Square] ({}) 1/1 - 4".format(square.id)
        self.assertEqual(str(square), expected_output)

    def test_update_attributes(self):
        square = Square(2, 2, 2, 2)
        square.update(5, 3, 3, 3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 5)

    def test_update_attributes_keyword_args(self):
        square = Square(2, 2, 2, 2)
        square.update(id=5, size=3, x=3, y=3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 5)

    def test_update_attributes_mixed_args(self):
        square = Square(2, 2, 2, 2)
        square.update(id=5, size=3, x=3, y=3)
        self.assertEqual(square.width, 3)
        self.assertEqual(square.height, 3)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 5)

    # Testing to_dictionary()
    def test_to_dictionary(self):
        s = Square(10, 2, 1)
        s_dictionary = s.to_dictionary()
        expected_output = f"{{'id': {s.id}, 'x': {s.x}, 'size': {s.size}, 'y': {s.y}}}\n"
        assertPrints(self, expected_output, print, s_dictionary)  
    
if __name__ == '__main__':
    unittest.main()
