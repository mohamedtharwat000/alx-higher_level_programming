#!/usr/bin/python3

"""
    Rectangle class module
"""


class Rectangle():
    """
        Rectangle class
    """
    def __init__(self):
        """
            __init__ - class constructor
        """
        self.__width = 0

    @property
    def width(self):
        """
            width - width getter
            Returns:
                int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width - width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
