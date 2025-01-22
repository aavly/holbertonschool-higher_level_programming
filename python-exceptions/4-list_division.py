#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    quotient = None

    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
            new_list.append(quotient)
        except (ValueError, TypeError):
            new_list.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
        finally:
            print(end="")

    return new_list
