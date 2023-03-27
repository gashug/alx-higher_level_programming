#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format the value as an integer using "{:d}".format()
        print("{:d}".format(value))
        # If we get here, the value was printed correctly as an integer
        return True
    except (ValueError, TypeError):
        # If we get a ValueError or TypeError, the value cannot be formatted as an integer
        return False
