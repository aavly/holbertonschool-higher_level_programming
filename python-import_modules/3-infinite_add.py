#!/usr/bin/python3

import sys

sum = 0
totalArgs = len(sys.argv)

for i in range(1, totalArgs):
    sum = sum + int(sys.argv[i])

print(sum)

if __name__ == "__main__":
    pass
