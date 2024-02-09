#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        var = a / b
        return var
    except ZeroDivisionError:
        return None
    finally:
        if b == 0:
            print("Inside result: None")
        else:
            print("Inside result: {}".format(a/b))
