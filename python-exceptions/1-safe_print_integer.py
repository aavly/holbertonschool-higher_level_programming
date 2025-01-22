#!/usr/bin/python3

def safe_print_integer(value):

    isInteger = True

    if not isinstance(value, int):
        return False

    try:
        print("{:d}".format(value))
    except ValueError:
        isInteger = False
    finally:
        return isInteger
