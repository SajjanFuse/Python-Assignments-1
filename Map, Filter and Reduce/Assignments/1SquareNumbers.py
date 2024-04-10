"""
[map] Write a Python function square_numbers that takes a list of integers as input and uses the map function to return a new list containing the square of each element.
"""

def square_numbers(*arrgs):
    """
    takes a list of integers as input

    Returns new list containing square of each element 
    """
    return list(map(lambda x:x*x, arrgs))


print(square_numbers(1,2,3,4,5,6,7,8))