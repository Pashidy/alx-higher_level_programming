#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size  # Using the property setter to set the size

    @property
    def size(self):
        return self.__size  # Property getter to retrieve size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Set the private instance attribute

    def area(self):
        return self.__size ** 2  # Calculate and return the area
    print()
