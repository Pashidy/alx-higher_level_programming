#!/usr/bin/python3
""" To find the peak of a list of integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list of int): List of integers to find peak of
    Returns:
        int: Peak of list_of_integers or None if list is empty
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
