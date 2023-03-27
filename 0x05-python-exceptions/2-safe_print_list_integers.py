#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            # Try to format the i-th element
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        # Print a new line at the end
        print("")
        return count
    except IndexError:
        # print nothing and return integer count, if int absent
        print("")
        return count
