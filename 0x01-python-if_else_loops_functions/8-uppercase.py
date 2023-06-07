#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            print("{0:c}".format(chr(ord(letter) - 32)), end="")
        else:
            print("{0:c}".format(letter))
