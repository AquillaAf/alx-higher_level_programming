#!/usr/bin/python3
"""Defines a class square"""

class Square:
    """rep as square"""
    def __init__(self, size=0):
        """ initializes a new square
        Args:
            size (int): the size of the square
        """
        if not isinstance (size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)
