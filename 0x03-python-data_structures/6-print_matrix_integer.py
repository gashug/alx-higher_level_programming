#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Loop through each row in the matrix
    for row in matrix:
        # Loop through each element in the row
        for element in row:
            # Print the element with a space separator and without newline
            print(element, end=' ')
            # After each row, print a newline character to move to the next line
        print()
