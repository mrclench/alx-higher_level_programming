#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number *= -1

    the_last_digit = number % 10
    print("{}".format(the_last_digit), end='')

    return (the_last_digit)
