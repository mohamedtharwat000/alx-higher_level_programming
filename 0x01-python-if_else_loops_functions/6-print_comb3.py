#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(0, 10):
        if number1 == number2 or number1 > number2:
            continue
        if number1 == 8:
            print("{0}{1}".format(number1, number2))
        else:
            print("{0}{1}".format(number1, number2), end=", ")
