#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0 or my_list == []:
        return
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        i += 1
    except IndexError:
        pass
    finally:
        print()
        return i
