#!/usr/bin/python3
for index in range(0, 26):
    test_word = ord('z') - index
    if (index % 2 == 1):
        test_word = chr(test_word - ord('a') + ord('A'))
    else:
        test_word = chr(test_word)
    print("{}".format(test_word), end='')
