#!/usr/bin/python3
import random
number = random.randint(-10, 10)
numberType = ""

if number > 0:
    numberType = "is positive"
if number == 0:
    numberType = "is zero"
if number < 0:
    numberType = "is negative"

print(f"{number:d} {numberType}")
