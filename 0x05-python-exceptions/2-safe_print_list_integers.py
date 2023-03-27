#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Try to format the i-th element of the list as an integer using "{:d}".format()
            # If it can be formatted, print it and increment the count variable
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        # Print a new line at the end, to separate this list from future printed output
        print("")
        return count
    except IndexError:
        # If we try to access an element that doesn't exist, print nothing and return the count of integers printed so far
        print("")
        return count
