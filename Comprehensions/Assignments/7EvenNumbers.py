"""
[set comprehension] Given a list of numbers, create a set using set comprehension that contains only unique even numbers.
"""

def getEvenNumbers(numbers_list):
    return {num for num in numbers_list if num%2==0}

print(getEvenNumbers([3,5,2,34,35,34,5,2,3,2,23,1,123,12,4,2,12]))
