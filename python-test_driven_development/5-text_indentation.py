#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after ',' '?' and ':'

    Args:
        text: text to check for characters

    Returns:
        Text with according new lines.

    Raises:
        TypeError:	text must be a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i == ',' or '?' or ':':
            print("{}\n\n".format(i))
        else:
            print(i)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
