#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ret = 0
    i = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{}".format(value), end='')
            ret += 1
        except IndexError:
            break
    print("")
    return ret
