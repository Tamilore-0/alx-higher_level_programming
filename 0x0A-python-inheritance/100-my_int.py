#!/usr/bin/python3
"""
Module defining the MyInt class.
"""


class MyInt(int):
    """
    MyInt class that inherits from int with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==), inverting the comparison.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=), inverting the comparison.
        """
        return super().__eq__(other)
