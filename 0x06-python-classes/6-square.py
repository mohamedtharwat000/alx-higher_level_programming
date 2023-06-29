#!/usr/bin/python3
"""
    Square class
"""
class Square:
    """
    Define a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init method
        @size (int): size of the square
        @position (tuple): position of the square

        @return: None
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
        @return: the current square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size - method that sets the current square size
        @value (int): size of the square
        @return: None
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
        @return: the current square position
        """
        return self.__positionself

    @position.setter
    def position(self, value):
        """
        position - method that sets the current square position
        @value (tuple): position of the square
        @return: None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Area - method that returns the current square area
        @return: the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Print - method that prints in stdout the square with the character #
        @return: None
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
