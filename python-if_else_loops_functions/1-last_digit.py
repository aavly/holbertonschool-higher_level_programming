#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

if number < 0:
    lastDigit = number % -10
else:
    lastDigit = number % 10

str = "Last digit of"

if lastDigit > 5:
    print(f"{str} {number} is {lastDigit} and is greater than 5")
elif lastDigit == 0:
    print(f"{str} {number} is {lastDigit} and is 0")
else:
    print(f"{str} {number} is {lastDigit} and is less than 6 and not 0")
