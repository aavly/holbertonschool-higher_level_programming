#!/usr/bin/python3

import sys

totalArgs = len(sys.argv)
if totalArgs == 1:
    print("{} arguments:".format(totalArgs - 1))
elif totalArgs == 2:
    print("{} argument:".format(totalArgs - 1))
else:
    print("{} arguments:".format(totalArgs - 1))

for i in range(1, totalArgs):
    print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    pass
