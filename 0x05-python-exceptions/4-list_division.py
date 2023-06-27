#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for x in range(list_length):
        try:
            result.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
        except TypeError:
            result.append(0)
            print("wrong type")
    return result
