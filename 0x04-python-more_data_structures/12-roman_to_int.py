#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_string_len = len(roman_string)
    result = 0
    for i in range(roman_string_len):
        if i + 1 < roman_string_len \
          and numbers[roman_string[i]] < numbers[roman_string[i + 1]]:
            result -= numbers[roman_string[i]]
        else:
            result += numbers[roman_string[i]]
    return result
