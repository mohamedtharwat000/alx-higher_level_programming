#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    argv_len = len(sys.argv) - 1
    if argv_len == 0:
        print(f"{argv_len:d} arguments.")
    else:
        if argv_len == 1:
            print(f"{argv_len:d} argument:")
        else:
            print(f"{argv_len:d} arguments:")
        for arg in sys.argv:
            print(f"{i}: {arg}")
            i += 1
