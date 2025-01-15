#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return print(number % -10)
    else:
        return print(number % 10)
