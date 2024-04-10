"""
Implement a function called concatenate_strings that takes a list of strings as input and uses the reduce function to return a single string containing the concatenation of all the elements.
"""
from functools import reduce 

# x + y for a string concatenates them together! 
def concatenate_strings(*args):
    """
    Takes any length of strings in the form of a list, but as a tuple

    Returns a list with concatenated string
    """
    return reduce(lambda x,y:x+y, args)

print(concatenate_strings("Fuse", "Machines", "Corporation"))

# for multiple length strings
print(concatenate_strings("F", "U", "S", "E", " ", "MACHINES"))
