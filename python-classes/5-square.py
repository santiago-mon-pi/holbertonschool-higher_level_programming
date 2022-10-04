#!/usr/bin/python3
"A class Square that defines a square"


class Square:
    "init allow square class to be used"
    def __init__(self, size=0):
        "asign private instance attribute size"
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        " this function prints in stdout the square with the character #"
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size):
                print('#' * self.__size)
