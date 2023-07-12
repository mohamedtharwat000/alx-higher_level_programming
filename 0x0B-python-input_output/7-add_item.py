#!/usr/bin/python3

"""
    script that adds all arguments to a Python list,
    and then save them to a file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    list_args = []
    for arg in sys.argv[1:]:
        list_args.append(arg)
    try:
        list_exist = load_from_json_file("add_arg.json")
    except FileNotFoundError:
        list_exist = []
    finally:
        list_exist += list_args
        save_to_json_file(list_exist, "add_arg.json")
