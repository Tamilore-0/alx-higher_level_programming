#!/usr/bin/python3
"""
Module defining a base class
"""


import json
import os
import turtle
import csv


class Base:
    """
    Base class for managing object identities.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base object with a unique identifier.

        Args:
            id (int): The identity of the new Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that writes the JSON string representation of list_objs
        to a file.
        """
        filename = f'{cls.__name__}.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                data = cls.to_json_string(
                        [_.to_dictionary() for _ in list_objs]
                        )
                file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes
        set from the provided dictionary.
        """
        dummy_instance = cls(1, 1, 1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".csv"  # creates a filename for the CSV file
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")  # Return an empty list
            else:
                if cls.__name__ == "Rectangle":
                    # assign fieldnames depending on the object
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                # write dictionaries to the CSV file
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    # converts the object to a dictionary
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads from a CSV file

        Returns:
            list: list of dictionaries
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    # Depending on the class name, different fieldnames
                    #  will be used for reading data from the CSV file
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                # reads data from the CSV file
                list = csv.DictReader(file, fieldnames=fieldnames)

                # convert the read dictionaries into a list of dictionaries
                list = [dict([k, int(v)] for k, v in d.items())
                        for d in list]
                return [cls.create(**d) for d in list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): A list of rectangles
            list_squares (list): A list of squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
