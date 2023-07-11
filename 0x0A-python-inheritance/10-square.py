#!/usr/bin/python3

Rectangle = __import__('8-rectangle').Rectangle
"""
    module for the class Square.
"""


class Square(Rectangle):
    """
        class Square
    """
    def __init__(self, size):
        """
            __init__ - class constructor
            Args:
                size (int): size of the square
            Raises:
                TypeError: if size is not an integer
                ValueError: if size is <= 0
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            area - returns the area of the square
            Retuens:
                area of the square
        """
        return self.__size * self.__size
