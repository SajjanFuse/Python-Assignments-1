"""
[list comprehension] Given two lists of integers, create a list that contains the product of each element of the first list with the corresponding element in the second list using list comprehension.

"""
# ints1 and ints2 are two lists of integers
def product_list(ints1, ints2):
    
    # for same length between two lists of integers 
    assert len(ints1) == len(ints2)

    return [ints1[i]*ints2[i] for i in range(len(ints1))]

print(product_list([2,4,2,45], [23,5,21,3]))

print(product_list([2,4,2,45, 21], range(5)))