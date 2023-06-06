#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberType = ""
n = 0

if number > 0:
    n = 10
if number < 0:
    n = -10

lastDigit = number % n

if lastDigit > 5:
    numberType = "and is greater than 5"
if lastDigit == 0:
    numberType = "and is 0"
if lastDigit < 6:
    numberType = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {lastDigit} {numberType}")
