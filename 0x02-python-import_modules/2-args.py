#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argv_len = len(argv) - 1
    if argv_len == 0:
        print(f"{argv_len:d} arguments.")
    else:
        if argv_len == 1:
            print(f"{argv_len:d} argument:")
        else:
            print(f"{argv_len:d} arguments:")
        for i in range(1, argv_len + 1):
            print(f"{i}: {argv[i]}")
