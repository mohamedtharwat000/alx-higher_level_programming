#!/usr/bin/python3

"""
    module for the class MyList
"""


class MyList(list):
    """
        MyList - class inherits from list
    """
    def __init__(self, *args):
        """
            __init__ - class constructor
            Args:
                *args: Variable length argument list.
        """
        super().__init__(*args)

    def print_sorted(self):
        """
            print_sorted - prints the list in sorted order
        """
        print(sorted(self))
