#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_og = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return list_og
    list_og[idx] = element
    return list_og
