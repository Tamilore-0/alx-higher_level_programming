import sys
from io import StringIO
import unittest
from models.rectangle import Rectangle
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

class TestRectangle(unittest.TestCase):
    def setUp(self):
        # Reset shared state before each test
        Rectangle._Base__nb_objects = 0

    def tearDown(self):
        # Clean up after each test if needed
        pass

    # Tests for width attribute
    def test_width_positive_integer(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)

    def test_width_negative_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    def test_width_non_integer(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 5)

    # Tests for height attribute
    def test_height_positive_integer(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.height, 5)

    def test_height_negative_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_height_non_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid")

    # Tests for x attribute
    def test_x_positive_integer(self):
        rect = Rectangle(10, 5, 3)
        self.assertEqual(rect.x, 3)

    def test_x_negative_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -3)

    def test_x_non_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "invalid")

    # Tests for y attribute
    def test_y_positive_integer(self):
        rect = Rectangle(10, 5, 3, 2)
        self.assertEqual(rect.y, 2)

    def test_y_negative_integer(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 3, -2)

    def test_y_non_integer(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 3, "invalid")
        
    def test_incomplete_arguments(self):
        # Test with 0 argument
        with self.assertRaises(TypeError):
            Rectangle()
        # Test with 1 arguments
        with self.assertRaises(TypeError):
            Rectangle(1)
        # Testing with booleans
        with self.assertRaises(TypeError):
            Rectangle(True, False, True, False)
        # Testing wrong number of attr
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
    
    def test_access_width_directly(self):
        with self.assertRaises(AttributeError):
            print(self.rect.__width)

    def test_access_height_directly(self):
        with self.assertRaises(AttributeError):
            print(self.rect.__height)

    def test_access_x_directly(self):
        with self.assertRaises(AttributeError):
            print(self.rect.__x)

    def test_access_y_directly(self):
        with self.assertRaises(AttributeError):
            print(self.rect.__y)

    # Testing area() function   
    def test_valid_area(self):
        # Test valid input for width and height
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_invalid_area_type_error(self):
        # Test invalid input (TypeError)
        with self.assertRaises(TypeError):
            Rectangle("invalid", 5).area()

    def test_negative_width(self):
        # Test negative width (ValueError)
        with self.assertRaises(ValueError):
            Rectangle(-4, 5).area()

    def test_negative_height(self):
        # Test negative height (ValueError)
        with self.assertRaises(ValueError):
            Rectangle(4, -5).area()

    def test_zero_width(self):
        # Test zero width (ValueError)
        with self.assertRaises(ValueError):
            Rectangle(0, 5).area()

    def test_zero_height(self):
        # Test zero height (ValueError)
        with self.assertRaises(ValueError):
            Rectangle(4, 0).area()

    def test_zero_width_height(self):
        # Test zero width and height (ValueError)
        with self.assertRaises(ValueError):
            Rectangle(0, 0).area()
    
    # Testing display()
    def test_display_func(self):
        rect = Rectangle(2, 2)
        expected_output = "##\n##\n"
        assertPrints(self, expected_output, rect.display)
        
    def test_display_func2(self):
        rect = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        assertPrints(self, expected_output, rect.display)

    # Testing __str__
    def test_stdout_method(self):
        rect = Rectangle(4, 6, 2, 1, 12)
        expected_output = f"[Rectangle] ({rect.id}) {rect._Rectangle__x}/{rect._Rectangle__y} - {rect._Rectangle__width}/{rect._Rectangle__height}\n"
        assertPrints(self, expected_output, print, rect)
        
    # Testing update()
    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
     
    def test_update_args_None_id(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r1.id)
        self.assertEqual(correct, str(r1))
        
    def test_update_args_invalid(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r1.update(10, "Invalid")
        
    def test_update_args_negative(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            r1.update(10, -6)
        
    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        r1.update(height=1)
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
       
    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.id = 1
        with self.assertRaises(TypeError):
            r1.update(height="Invalid")
       
    # Testing to_dictionary()
    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9)
        rect_dictionary = rect.to_dictionary()
        expected_output = (
            "{"
            f"'x': {rect._Rectangle__x}"
            f", 'y': {rect._Rectangle__y}"
            f", 'id': {rect.id}"
            f", 'height': {rect._Rectangle__height}"
            f", 'width': {rect._Rectangle__width}"
            "}\n"
        )
        assertPrints(self, expected_output, print, rect_dictionary)  
    
if __name__ == "__main__":
    unittest.main()