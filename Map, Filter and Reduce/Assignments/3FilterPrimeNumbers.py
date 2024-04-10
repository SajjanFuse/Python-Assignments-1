"""
[filter] Implement a function called filter_prime_numbers that takes a list of integers as input and uses the filter function to return a new list containing only the prime numbers.
"""

def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    
    # optimal code for the detection of prime numbers 
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# *args give the variable length of integers for the prime number detection  
def filter_prime_numbers(*args):
    return list(filter(isPrime, args))

print(filter_prime_numbers(3,3,2,43,4,2,23,3,2))