#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return None

    Romans = {'X': 10,
              'V': 5,
              'I': 1,
              'L': 50, 
              'C': 100,
              'D': 500
              }


