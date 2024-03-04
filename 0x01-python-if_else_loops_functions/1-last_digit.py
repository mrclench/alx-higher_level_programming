#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number % -10
j = number % 10

if number < 0:
    if i == 0:
        print(f"Last digit of {number} is {number % 10} and is 0")
    elif i < 6:
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")

else:
    if j == 0:
        print(f"Last digit of {number} is {number % 10} and is 0")
    elif j < 6:
        print(f"Last digit of {number} is {i} and is less than 6 and not 0")
    else:
        print("Last digit of {} is {} and is greater than 5".format(number, j))
