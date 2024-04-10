""""
[dictionary comprehension] Given two lists
one containing keys and another containing values, create a dictionary using dictionary comprehension.
"""

def getSet(list1, list2):
    assert len(list1)==len(list2)
    return {list1[i]:list2[i] for i in range(len(list1))}

print(getSet(["key1", "key2", "key3"], [2,3,3]))