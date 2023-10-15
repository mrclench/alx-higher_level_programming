#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''this function returns a new 
    dictionary with all values multiplied by 2'''
    if(a_dictionary):
        return(dict((x, y*2) for x, y in a_dictionary.items()))

