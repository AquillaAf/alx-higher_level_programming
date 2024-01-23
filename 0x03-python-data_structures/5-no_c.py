#!/usr/bin/python3
def no_c(my_string):
    final = ""
    for i in range(len(my_string)):
            if (my_string[i] == 'c' or my_string[i] == 'C'):
                continue
            else:
               final += my_string[i]
    return final
