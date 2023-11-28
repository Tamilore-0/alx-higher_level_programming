#!/usr/bin/python3
"""
Module description goes here.
"""


class LockedClass:
    """LockedClass allows only 'first_name' attribute."""
    __slots__ = ('first_name')
