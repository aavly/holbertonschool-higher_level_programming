#!/usr/bin/python3
def uppercase(str):
    result = ""
    for a in str:
        if ord(a) < 123 and ord(a) > 96:
            a = chr(ord(a) - 32)
        result = result + a
    print("{}".format(result))
