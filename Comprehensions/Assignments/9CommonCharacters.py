"""
[set comprehension] Given two strings, write a Python program to create a set using set comprehension that contains all the characters that are common in both strings.
"""

def getCommonStrings(str1, str2):
    return {m for m in str1 if m in str2}

print(getCommonStrings('Ram', 'Shyam'))