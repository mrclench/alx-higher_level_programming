#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    count = []

    for i in range(list_length):
        try:
            count.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            count.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            count.append(0)
        except IndexError:
            print("out of range")
            count.append(0)
    return count
