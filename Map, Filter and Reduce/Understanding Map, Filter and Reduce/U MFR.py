"""
Sajjan Acharya 
12:32, 10th April, 2024
Understanding Map, Filter and Reduce
"""

# Basic Notes About the Terms 

"""
Map: 
    - applies a function to all items in an input list 
    - map(func, inp_list)

Filter: 
    - gives list of elements for which a function returns true 
    - filter(func, inp_list)
    - faster than for loop!!!

Reduce: 
    - computation on a list and return result 
    - rolling computation? 
    - involving the numbers in the list together with each other?

    Returns a list itself, no need to make the result class as list again as above methods 

"""

inps = [3,423,4,34,2,3,4,52,7]

def sub(num):
    return 1000-num 

print(type(map(sub, inps))) # -> returns a class <'map'>

print(list(map(sub, inps)))

# lambda function one liner expression function 
# lambda x:y -> x is inputs, y is the operation to be performed! 
print(list(map(lambda x:x-1000, inps )))

# lambda function in filter should return bool? 

print(list(filter(lambda x:x>12, inps)))

from functools import reduce 
inp_list = [1, 2, 3, 4]

print(reduce((lambda x,y:x*y), inp_list))

# should involve all n elements in the list for reduce! 