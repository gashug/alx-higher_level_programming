#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > my_list[len(my_list) - 1]:
        return None
    else:
        return my_list[idx]
