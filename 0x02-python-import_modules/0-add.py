#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    a, b = 1, 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))
