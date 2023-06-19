#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_string_len = len(roman_string)
    result = 0
    for i in range(roman_string_len):
        if roman_string[i] not in numbers:
            return 0
        if i + 1 < roman_string_len:
            if numbers[roman_string[i]] < numbers[roman_string[i + 1]]:
                result -= numbers[roman_string[i]]
        else:
            result += numbers[roman_string[i]]
    return result
