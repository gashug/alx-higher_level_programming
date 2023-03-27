#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a count variable to keep track of elements
    count = 0

    try:
        # Loop over the first x elements of the list
        for i in range(x):
            # Print the i-th element of the list, without new line
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # Pass over and end loop if element non-existent
        pass

    # Print a new line at the end
    print("")

    return count
