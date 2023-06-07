#!/usr/bin/python3
def print_last_digit(number):
    n = 10
    if number < 0:
        n = -10
    last = number % 10
    if last < 0:
        last *= -1
    print("{0:d}".format(last), end="")
    return last
