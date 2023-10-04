#!/usr/bin/python3
for decimal_digit in range(0, 100):
    if decimal_digit == 99:
        print("{}".format(decimal_digit))
    else:
        print("{:02}".format(decimal_digit), end=', ')
