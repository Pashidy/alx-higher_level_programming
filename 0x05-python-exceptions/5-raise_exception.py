#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Custom Type Exception")
    except TypeError as e:
        raise e
