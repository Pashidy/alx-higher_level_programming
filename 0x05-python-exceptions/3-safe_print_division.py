#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        try:
            print("Inside result: {}".format(div))
        except NameError:
            print("Inside result: None")
    return div
