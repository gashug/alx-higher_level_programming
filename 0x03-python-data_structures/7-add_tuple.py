#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        first_value = tuple_a[0] + tuple_b[0]
        second_value = 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        first_value = tuple_a[0] + tuple_b[0]
        second_value = tuple_a[1] + 0
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) == 0:
        return tuple_b
    else:
        first_value = tuple_a[0] + tuple_b[0]
        second_value = tuple_a[1] + tuple_b[1]

    new_tuple = (first_value, second_value)
    return new_tuple
