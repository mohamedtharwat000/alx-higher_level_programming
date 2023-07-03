#!/usr/bin/python3

"""
    Rectangle class module
"""


class Rectangle():
    """
        Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
            __init__ - class constructor
        """
        self.__width = width
        self.__height = height

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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            height - hight getter
            Returns:
                int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height - height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
