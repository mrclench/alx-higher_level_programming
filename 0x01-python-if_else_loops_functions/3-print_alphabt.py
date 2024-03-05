#!/usr/bin/python3
for j in range(97,123):
    if chr(j) == 'e' or chr(j) == 'q':
        continue
    print("{}".format(chr(j)), end="")
