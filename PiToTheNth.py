# -*- coding: utf-8 -*-
"""
This program will calculate Pi to the nth.
"""

number = ''
print("This program will calculate Pi to the 'nth'")
print("Pick a number less than 621 or type 'exit' to exit the program.")
from math import *
while number != 'exit':
    number = input('What number? ')
    try:
        if number.isnumeric():
             print (pi ** int(number))
        elif number == 'exit':
            print('exiting')
        else:
             print('Numbers only')
    except OverflowError:
        print('Pick a number lower than 621')
