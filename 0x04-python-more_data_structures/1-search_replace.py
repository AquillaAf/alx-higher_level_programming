#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list.copy()
    copy[copy.index(search)] = replace
    return copy
