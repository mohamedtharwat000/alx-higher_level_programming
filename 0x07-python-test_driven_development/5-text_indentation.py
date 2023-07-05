#!/usr/bin/python3

"""
    This module contains function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        text_indentation - prints a text with 2 new lines
        after each of these characters: ., ? and :
        Args:
            text (str): text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            if text[i] == ' ' and \
                (text[i - 1] == '.' \
                    or text[i - 1] == '?' \
                    or text[i - 1] == ':'):
                continue
            else:
                print(text[i], end='')
