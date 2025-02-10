#!/usr/bin/python3
"""
2. Append to a file
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8).
    Returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        if not isinstance(text, str):
            s = str(text)
            return f.write(s)
        else:
            return f.write(text)
