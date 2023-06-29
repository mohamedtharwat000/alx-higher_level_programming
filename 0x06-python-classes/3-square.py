#!/usr/bin/python3
"""
    Square class
"""
class Square:
    """
    Define a square
    """
    def __init__(self, size=0):
        """
        init method
        @size (int): size of the square
        @return: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Area - method that returns the current square area
        @return: the current square area
        """
        return (self.__size * self.__size)
