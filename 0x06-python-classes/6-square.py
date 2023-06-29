#!/usr/bin/python3

"""
Square class
"""


class Square:
    """
    Square - class that define a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ - class constructor
        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple or len(position) != 2 or \
           type(position[0]) is not int or type(position[1]) is not int or \
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        position - method that returns the current square position
        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position - method that sets the current square position
        Args:
            value (tuple): position of the square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
