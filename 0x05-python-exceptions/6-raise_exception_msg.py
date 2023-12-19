#!/usr/bin/python3

def raise_exception_msg(message=""):
    class NameException(Exception):
        pass

    try:
        raise NameException(message)
    except NameException as e:
        raise e
