#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return
    var = list_of_integers[0]
    
    for index in range(len(list_of_integers) - 1):
        if var < list_of_integers[index + 1]:
            var = list_of_integers[index + 1]
    return (var)
