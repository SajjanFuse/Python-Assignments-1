"""
[set comprehension] Given a list of words, write a Python program to create a set using set comprehension that contains all the unique characters present in the words.
"""

def getUniqueCharacters(word_list):
    return {u for unique in word_list for u in unique}

print(getUniqueCharacters(["word", "unique", "word", "ram", "unique", "shyam"]))