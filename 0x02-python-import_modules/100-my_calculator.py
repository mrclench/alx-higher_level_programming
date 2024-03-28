#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    

    argc = len(sys.argv)
    if (argc < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
#    elif operator != + or - or * or /:
#        print("Unknown operator. Available operators: +, -, * and /")
#        exit(1)
    elif (argc > 2):
        print("{} {} {} = {}".format(a, operator, c, result)
        exit(0)
