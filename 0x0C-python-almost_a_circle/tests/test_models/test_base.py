import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import mock_open, patch

class TestBase(unittest.TestCase):
    def setUp(self):
        # Reset shared state before each test
        Base._Base__nb_objects = 0

    def tearDown(self):
        # Clean up after each test if needed
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_constructor_with_no_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)  # The first instance should have id = 1

    def test_constructor_incrementing_ids(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)  # First instance should have id = 1
        self.assertEqual(obj2.id, 2)  # Second instance should have id = 2

    def test_constructor_with_custom_id(self):
        obj = Base(id=100)
        self.assertEqual(obj.id, 100)  # The id should be set to the specified value

    def test_constructor_with_string(self):
        obj = Base(id="hello")
        self.assertEqual(obj.id, "hello")
    
    def test_constructor_with_boolean(self):
        obj = Base(id=True)
        self.assertEqual(obj.id, True)
        
    def test_constructor_with_Overloading(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
            Base(1, 2, 3)
    
    def test_constructor_with_negative_id(self):
        obj = Base(id=-5)
        self.assertEqual(obj.id, -5)  # The id should be set to the specified negative value

    def test_constructor_with_zero_id(self):
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)  # The id should be set to the specified zero value

    def test_constructor_with_float_id(self):
        obj = Base(id=3.14)
        self.assertEqual(obj.id, 3.14)  # The id should be set to the specified float value

    def test_constructor_with_list_id(self):
        obj = Base(id=[1, 2, 3])
        self.assertEqual(obj.id, [1, 2, 3])  # The id should be set to the specified list value
        
    def test_constructor_with_None_id(self):
        obj = Base(id=None)
        self.assertEqual(obj.id, 1)  # The id should default to 1 when None is provided

    # Testing to_json_string method
    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_with_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_non_empty_list(self):
        data = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        result = Base.to_json_string(data)
        expected_result = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(result, expected_result)

    # Testing save_to_file method
    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), len('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}]'))
            
    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
            
    # Testing from_json_string method
    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))
        
    # Testing Create method
    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
        
    # Testing load_from_file method
    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
    
if __name__ == '__main__':
    unittest.main()
