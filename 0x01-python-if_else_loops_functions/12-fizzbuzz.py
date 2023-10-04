#!/usr/bin/python3


def fizzbuzz():
    for test_number in range(1, 101):
        if test_number % 3 == 0 and test_number % 5 == 0:
            print("FizzBuzz ", end="")
        elif test_number % 3 == 0:
            print("Fizz ", end="")
        elif test_number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(test_number), end="")
