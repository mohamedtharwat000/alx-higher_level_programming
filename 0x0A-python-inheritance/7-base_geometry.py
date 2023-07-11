#!/usr/bin/python3

"""
    module for the class BaseGeometry.
"""


class BaseGeometry:
    """
        class BaseGeometry
    """
    def area(self):
        """
            raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator - validates value
            Args:
                name (str): name
                value (int): value
            Raises:
                TypeError: if value is not an integer
                ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
