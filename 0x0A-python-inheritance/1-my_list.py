#!/usr/bin/python3

"""
module for my lists (inherits form list)
"""


class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        # sorted method
        # sorted(iterable[, key][, reverse])
        print(sorted(self))

# Check if the script is executed directly
if __name__ == "__main__":
    # Test case
    test_list = MyList([4, 2, 7, 1, 9])
    print("Sorted list:")
    test_list.print_sorted()

    # Add more test cases as needed
    # Test 2:
    # more_test = MyList([10, 5, 3])
    # print("Another sorted list:")
    # more_test.print_sorted()
