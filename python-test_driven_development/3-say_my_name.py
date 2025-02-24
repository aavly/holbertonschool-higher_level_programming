#!/usr/bin/python3
"""Say my name function"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name: string of first name.
        last_name: string of last name.

    Returns:
        "My name is <first name> <last name>".

    Raises:
        TypeError:  first_name must be a string
                    last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_namse must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
