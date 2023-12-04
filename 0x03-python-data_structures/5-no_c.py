#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements
    return new_string


if __name__ == "__main__":
    original_string = "This is a test with C and c characters"
    result_string = no_c(original_string)
    print(result_string)
