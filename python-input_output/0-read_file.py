#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, encoding="utf=8") as f:
        read_file = f.read()

    print(read_file, end="")
