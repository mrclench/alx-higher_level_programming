#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add

    add = 0
    n = len(sys.argv)

    for i in range(1, n):
        add += int(sys.argv[i])
    print("{}".format(add))
