#!/usr/bin/python3

def add_integer(a, b=98):
    """ 
    Returns the sum of 'a' and 'b'.
    
    Args:
        a (int): first integer to be added to sum.
        b (int): second integer to be added to sum.
    
    Returns:
        int: The sum of a + b
  
    Raises:
        TypeError: "{a or b} must be an integer"
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)



print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
