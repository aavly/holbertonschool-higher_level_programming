#!/usr/bin/python3
"""Text-indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.' '?' and ':'

    Args:
        text: text to check for characters
    Raises:
        TypeError:	text must be a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newText = ""
    for char in text:
        newText += char
        if char in ['.', '?', ':']:
            newText += "\n\n"

    print(newText.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
