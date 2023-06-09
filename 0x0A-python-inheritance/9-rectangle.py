#!/usr/bin/python3

"""
    module for the class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """
            area - returns the area of the rectangle
            Retuens:
                area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
            __str__ - returns a string representation of the rectangle
            Returns:
                string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
