#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    rip = int(str(number)[-1]) * -1
    if (rip < 0):
        print("the last digit of {} is {} and is less than 6 and not 0".format(number, rip))
elif (number > 0):
    rip = int(str(number)[-1])
    if(rip > 0 and rip < 6):
        print("the last digit of {} is {} and is less than 6 and not 0".format(number, rip))
    elif (rip > 6):
            print("the last digit of {} is {} and is greater than 5".format(number, rip))
    elif(rip == 0):
        print("the last digit of {} is {} and is 0".format(number, rip))

else:
    print("number is 0")
