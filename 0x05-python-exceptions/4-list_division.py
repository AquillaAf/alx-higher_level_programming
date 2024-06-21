#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):   
    try:    
        my_list = []
        while i < list_length:
            var = my_list_1[i] / my_list_2[i]
            i += 1
    except ZeroDivisionError:
        print("division by 0\n")
        var = 0
    except TypeError:
        print("wrong type")
        var = 0
    except IndexError:
        print("out of range")
        var = 0
    #finally:
        #my_list.append(var)
    return my_list
