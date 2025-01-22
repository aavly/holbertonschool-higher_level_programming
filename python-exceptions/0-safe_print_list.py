#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        for i in range(x):
            print(my_list[i], end="")
    except IndexError as e:
        print(e)
        print("The list isn't that big!")
    except ValueError as e:
        print(e)
        print("Enter only numbers please")
    except Exception as e:
        print(e)
        print("Whomp whomp, an error occurred.")
