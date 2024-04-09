#!/usr/bin/python3
""" function defines an addition operation"""

def add_integer(a, b=98):
    """Returns a sum of arg a and b.
    args:
        a(int): the first number
        b(int): the second number
    Float arguments are type casted before addition
    Raises:
        TypeError: if either a or b is a non-integer and non-float.
        """

    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError ("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance (b, float):
        b = int(b)
    
    return (a + b)
