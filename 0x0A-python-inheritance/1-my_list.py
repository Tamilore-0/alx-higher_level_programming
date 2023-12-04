#!usr/bin/python3
"""
Module: Mylist

This module defines the Mylist class,
which is a subclass of the built-in list class.
"""


class Mylist(list):
    """
    Mylist class extends the functionality of the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
