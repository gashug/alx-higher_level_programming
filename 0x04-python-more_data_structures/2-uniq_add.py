#!/usr/bin/python3
def uniq_add(my_list=[]):
    ctr = 0
    new_list = list(set(my_list))
    for i in range(len(new_list)):
        ctr += new_list[i]

    return ctr
