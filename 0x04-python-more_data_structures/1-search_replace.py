#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """this function replaces all occurrences of an element"""
    return([replace if x is search else x for x in my_list])

