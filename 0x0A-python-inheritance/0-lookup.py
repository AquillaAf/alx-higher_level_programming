#!/usr/bin/python3
"""module that returns a list of attributes and method of an object"""
def lookup(obj):
    """lookup is the function definition
        args:
            obj(obj): the objects of a class
    """
    return (dir(obj))
