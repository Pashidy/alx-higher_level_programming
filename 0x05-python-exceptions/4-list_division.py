#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError("out of range")

                dividend = my_list_1[i]
                divisor = my_list_2[i]

                if not (
                    isinstance(dividend, (int, float))
                    and isinstance(divisor, (int, float))
                ):
                    print("wrong type")
                    result.append(0)
                elif divisor == 0:
                    print("division by 0")
                    result.append(0)
                else:
                    result.append(dividend / divisor)
            except IndexError as e:
                print(e)
                result.append(0)
    finally:
        return result
