#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    module for the class Rectangle.
"""


class Rectangle(BaseGeometry):
    """
        class Rectangle
    """
    def __init__(self, width, height):
        """
            __init__ - class constructor
            Args:
                width (int): width
                height (int): height
            Raises:
                TypeError: if width or height are not integers
                ValueError: if width or height are <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
