#!/usr/bin/python3
"""
Module
"""


class Student:
    """
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            if all(isinstance(_, str) for _ in attrs):
                selected_attrs = {attr: getattr(self, attr)
                                  for attr in attrs if hasattr(self, attr)}
                return selected_attrs
        return self.__dict__
