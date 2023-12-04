#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list


if __name__ == "__main__":

    original_list = [1, 2, 3, 4, 5]
    index = 2
    new_element = 10
    modified_list = new_in_list(original_list, index, new_element)
    print(modified_list)
