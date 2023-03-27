#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a count variable to keep track of the number of elements printed
    count = 0

    try:
        # Loop over the first x elements of the list
        for i in range(x):
            # Print the i-th element of the list, without adding a new line at the end
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # If we try to access an element that doesn't exist, pass over and end the loop
        pass

    # Print a new line at the end, to separate this list from future printed output
    print("")

    return count
