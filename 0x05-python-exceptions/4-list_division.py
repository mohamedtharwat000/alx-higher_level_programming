#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for x in range(list_length):
        has_error = False
        try:
            division_result = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        except IndexError:
            division_result = 0
            print("out of range")
        except TypeError:
            division_result = 0
            print("wrong type")
        finally:
            result.append(division_result)
    return result
