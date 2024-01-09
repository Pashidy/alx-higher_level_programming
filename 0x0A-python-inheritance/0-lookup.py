#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: The object for which attributes and methods are to be listed.

    Returns:
    - A list object containing the available attributes and methods of the input object.
    """
    return dir(obj)
