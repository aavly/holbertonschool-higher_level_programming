#!/usr/bin/python3
"""
1. Write to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns number of chars written
    """
    with open(filename, encoding="utf-8") as f:
        if not isinstance(text, str):
            s = str(text)
            return f.write(s)
        else:
            return f.write(text)
