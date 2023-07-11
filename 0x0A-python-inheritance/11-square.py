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
        super().__init__(size, size)

        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """
            area - returns the area of the Square
            Retuens:
                area of the Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
            __str__ - returns a string representation of the Square
            Returns:
                string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
