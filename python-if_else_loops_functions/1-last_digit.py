#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

lastDigit = abs(number) % 10
str = "Last digit of"

if lastDigit > 5:
    print(f"{str} is {number} and is greater than 5")
elif lastDigit == 0:
    print(f"{str} is {number} and is 0.")
else:
    print(f"{str} is {number} and is greater than 5")
