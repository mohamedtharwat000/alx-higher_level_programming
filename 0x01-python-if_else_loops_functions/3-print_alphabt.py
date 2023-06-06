#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) == "e" or chr(letter) == "q":
        continue
    print("{0}".format(chr(letter)), end="")
