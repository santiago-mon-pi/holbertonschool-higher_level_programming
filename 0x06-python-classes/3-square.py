#!/usr/bin/python3
"A class Square that defines a square"


class Square:
    "init allow square class to be used"
    def __init__(self, size=0):
        "asign private instance attribute size"
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return self.__size ** 2
