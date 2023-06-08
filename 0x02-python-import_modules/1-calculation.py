#!/usr/bin/python3
import calculator_1.py as calculator
if __name__ == "__main__":
    a = 10
    b = 5
    print("{0:d} + {1:d} = {2:d}".format(a, b, calculator.add(a, b)))
    print("{0:d} + {1:d} = {2:d}".format(a, b, calculator.sub(a, b)))
    print("{0:d} + {1:d} = {2:d}".format(a, b, calculator.mul(a, b)))
    print("{0:d} + {1:d} = {2:d}".format(a, b, calculator.div(a, b)))
