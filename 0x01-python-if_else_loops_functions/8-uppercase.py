#!/usr/bin/python3
def uppercase(str):
    for test_word in str:
        if (ord(test_word) > 96 and ord(test_word) <= 124):
            test_word = chr(ord(test_word) - 32)
        print("{}".format(test_word), end='')
    print()
