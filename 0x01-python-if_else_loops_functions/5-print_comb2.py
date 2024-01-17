#!/usr/bin/python3
for num in range(1, 100):
    if num < 10:
        print("0{}".format(num), end=", ")
    elif num == 99:
        print("{}".format(num))
    else:
        print("{}".format(num), end=", ")
print('\n')
