"""
Sajjan Acharya 
15:20, 10th April, 2024
Understanding different comprehensions in Python
"""

# Basic notes on types of Comprehensions 
"""
Comprehensions: 
    - allow sequence to be built from other sequencers 

List Comprehension: 
    - short and concise way to create lists
    - one liner with [ for ..]

Dict Comprehension: 
    - {a:b for a, b in some_dict.items()}

Set Comprehension: 
    - {}

Generator Comprehension:
    - similar to list
    - doesn't allocate memory for whole list
    - generate one item at a time? 
        - memory efficient... 
        - generator expression only has to yield one item at a time
        - next(gen_object)
    - each element gets deleted every time it is iterated?
    - multiple values get by a=next(gen), b = next(gen)
    
"""
# list comprehensions 
arr = [m for m in [3,2,3,45,5,6] if m%3==0]
print(arr)

# nested list comprehension
arr2 = [m for min in [[12,2],[234,23],[12,1]] for m in min if m%2==0 ]
print(arr2)

#dict comprehension
dict_ = {m:m+'value' for m in ["one", "two", "three"]}
print(dict_)

set_ = {m%4 for m in [12,1,2,4,5,6,2,23,4,6] if m%2==0}
print(set_)

gen_ = (m for m in [3,2,3,45,5,6] if m%3==0)
print(gen_) #-> gives generator object only with memory location
print(next(gen_))
print(next(gen_))
print(next(gen_))
print(next(gen_))
# print(next(gen_)) # -> gives StopIteration since it has no more elements left  
print(gen_)
gen_to_list = list(gen_)
print(gen_to_list)

