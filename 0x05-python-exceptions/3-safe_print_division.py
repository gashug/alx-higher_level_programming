#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
        print("division by 0")
    else:
        print("Inside result: {}".format(result))
    finally:
        return result
