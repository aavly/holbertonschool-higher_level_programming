#!/usr/bin/python3

import sys

totalArgs = len(sys.argv)
print("{} arguments:".format(totalArgs - 1))

for i in range(1, totalArgs):
    print("{}: {}".format(i, sys.argv[i]))
