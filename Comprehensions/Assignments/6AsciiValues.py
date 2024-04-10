"""
[dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase alphabets (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.
"""

def getAscii(alphabets):
    # for lowercase alphabets 
    assert alphabets.islower()
    return {key:ord(key) for key in alphabets}

print(getAscii("asdfsdf"))

print(getAscii("HelloWorld")) # assertion error for all alphabets to be lower

print(getAscii("234dsksdf")) # same error since the number is present when only alphabets are expected