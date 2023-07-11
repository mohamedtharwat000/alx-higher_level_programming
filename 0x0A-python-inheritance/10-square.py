#!/usr/bin/python3

"""
    module for the class Square.
"""
Rectangle = __import__('8-rectangle').Rectangle


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

        super().__init__(self.__size, self.__size)

    def area(self):
        """
            area - returns the area of the square
            Retuens:
                area of the square
        """
        return self.__size * self.__size
