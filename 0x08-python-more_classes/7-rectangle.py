#!/usr/bin/python3

"""
    Rectangle class module
"""


class Rectangle():
    """
        Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            __init__ - class constructor
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
            area - returns the rectangle area
            Returns:
                int: rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            perimeter - returns the rectangle perimeter
            Returns:
                int: rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            __str__ - string representation of the rectangle
            Returns:
                str: string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            str = ""
            iterable = []
            for h in range(self.__height):
                for w in range(self.__width):
                    iterable.append(Rectangle.print_symbol)
                if h != self.__height - 1:
                    iterable.append("\n")
            str = str.join(iterable)
            return str

    def __repr__(self):
        """
            __repr__ - representation of the rectangle
            Returns:
                str: representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
            __del__ - rectangle destructor
        """
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
