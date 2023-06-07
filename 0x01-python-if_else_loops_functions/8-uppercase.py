#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            result += "{0}".format(chr(ord(letter) - 32))
        else:
            result += "{0}".format(letter)
    print(result)
