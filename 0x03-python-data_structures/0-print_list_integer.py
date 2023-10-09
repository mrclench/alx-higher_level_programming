#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """This function prints all integers in a List"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
