#!/usr/bin/python3

"""
Square class
"""


class Square:
    """
    Square - class that define a square
    """
    def __init__(self, size=0):
        """
        __init__ - class constructor
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        size - method that returns the current square size
        Returns:
            int: the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size - method that sets the current square size
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        area - method that returns the current square area
        Returns:
            int: the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        my_print - method that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
