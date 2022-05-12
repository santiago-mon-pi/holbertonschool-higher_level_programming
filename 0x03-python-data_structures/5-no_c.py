#!/usr/bin/python3
def no_c(my_string):
    # create a string that won't contain "C" ni "c"
    string_without_C = ""
    # for loop to go thru every character on string
    # add character if it does not contain C
    # return new string without the C
    for char in my_string:
        if char != 'c' and char != 'C':
            string_without_C += char
    return string_without_C
