#!/usr/bin/python3

"""
    script that adds all arguments to a Python list,
    and then save them to a file.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    list_arg = []
    for arg in sys.argv[1:]:
        list_arg.append(arg)
    try:
        list_arg += load_from_json_file("add_arg.json")
    except:
        save_to_json_file(list_arg, "add_arg.json")
    else:
        save_to_json_file(list_arg, "add_arg.json")
