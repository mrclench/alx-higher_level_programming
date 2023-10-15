#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """this function replaces all occurrences of an element"""
    new_list = []
    for i in my_list:
        if i == search:
            new _list.append(replace)
        else:
            new_list.append(i)
    return new_list

