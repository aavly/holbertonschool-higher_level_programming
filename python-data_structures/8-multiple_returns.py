#!/usr/bin/python3

def multiple_returns(sentence):

    firstChar = None
    length = len(sentence)

    if length == 0:
        return length, firstChar

    return length, sentence[0]
