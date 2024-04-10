"""
Given an array of strings (str), group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict

def group_anagrams(strings):
    anagrams = defaultdict(list) 

    for s in strings: 
        print(f'String: [{s}] Sorted String: {sorted(s)}')
        # getting all the sorted letters in the single letter

        sorted_s = ''.join(sorted(s))
        # print(s, anagrams[sorted_s])

        #grouping strings with same sorted string together!
        anagrams[sorted_s].append(s)
    
    
    return list(anagrams.values())

# Test the function
strs = ["eat", "tea", "tan", "ate", "nat", "bat", "pant", "antp", "tapn"]
print(group_anagrams(strs))
