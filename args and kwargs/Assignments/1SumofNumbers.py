"""
[*args] Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers.
Test your function with various input cases.
"""

def sumOfNumbers(*nums):
    sum=0
    for n in nums:
        sum +=n 
    return sum 

# Passing no arguments
print(sumOfNumbers())   

# Passing a single number
print(sumOfNumbers(5))  

# Passing multiple numbers
print(sumOfNumbers(1, 2, 3, 4))  

# Passing negative numbers
print(sumOfNumbers(-1, -2, -3))  

# Passing a mix of positive and negative numbers
print(sumOfNumbers(10, -5, 3, -2))  

# Passing floating-point numbers
print(sumOfNumbers(1.5, 2.5, 3.5))  

# Passing zero
print(sumOfNumbers(0, 0, 0)) 

# Passing a large number of arguments
print(sumOfNumbers(*range(100)))   

# Passing a mix of integers and floats
print(sumOfNumbers(1, 2.5, 3, 4.7))   

# Passing strings (different types than integer for the function)
print(sumOfNumbers("hello", "world")) # gives an error