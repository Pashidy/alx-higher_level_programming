#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    i = 0
    for i in range(x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
