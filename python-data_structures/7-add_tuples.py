#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    aList = []
    bList = []

    for i in [0, 1]:
        if tuple_a[i]:
            aList[i] = tuple_a[i]
        else:
            aList[i] = 0
    
    for i in [0, 1]:
        if tuple_b[i]:
            bList[i] = tuple_b[i]
        else:
            bList[i] = 0

    first = aList[0] + bList[0]
    second = bList[1] + bList[1]

    return first, second



tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))