# Created by: David Wang
# Created on: 17-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit5-03
# This program finds the smallest value in an array

from numpy import random

def find_smallest_value(array):
    
    smallest_value = array[0]
    for value in array:
        if smallest_value > value:
            smallest_value = value
    
    return smallest_value

my_array = []
for generate_random in range(0, random.randint(1, 25)):
    my_array.append(random.randint(1, 50))
print(my_array)
print(find_smallest_value(my_array))
