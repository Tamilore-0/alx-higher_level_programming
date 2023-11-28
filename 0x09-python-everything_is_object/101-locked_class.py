#!/usr/bin/python3
"""
Module description goes here.
"""


class LockedClass:
    """LockedClass allows only 'first_name' attribute."""
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
