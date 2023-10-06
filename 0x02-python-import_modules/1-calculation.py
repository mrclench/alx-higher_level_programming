#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
numbersadd = add(a, b)
numberssub = sub(a, b)
numbersmul = mul(a, b)
numbersdiv = div(a, b)
print("{} + {} = {}".format(a, b, numbersadd))
print("{} - {} = {}".format(a, b, numberssub))
print("{} * {} = {}".format(a, b, numbersmul))
print("{} / {} = {}".format(a, b, numbersdiv))
