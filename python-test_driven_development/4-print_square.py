#!/usr/bin/python3
"""Print squares function"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: size length of the square.

    Returns:
        A square in length 'size' of character #.

    Raises:
        TypeError:	size must be an integer.
        ValueError: size must be >= 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
