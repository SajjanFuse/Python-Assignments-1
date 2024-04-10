"""
Sajjan Acharya
14:12 , 10th April, 2024
Understanding Collections in Python
"""

# Some notes about Collections 

"""
- has a number of container data types 

DefaultDict: 
    - allows to specify default value for 'keys that are not set'
    - defaultdict(data type of values)

OrderedDict: 
    - normal dict has no specific order as it is inserted!
    - keeps order of entries same as during insertion 
    - deleting or reinserting -> at the last order

Counter 
    - count number of occurences of a particular item 

Deque: 
    - double ended queue 

Enum: 
    - organize things 

"""
from collections import defaultdict, OrderedDict, Counter, deque
from enum import Enum


# defaultdict

#counting the occurences of keys? 
my_list = ['apple', 'banana', 'apple', 'orange', 'banana']
my_counter = defaultdict(int)
print(f'DefaultDict output: {my_counter}\n')

# print(f'DefaultDict .items output : {my_counter.items}\n')
# gives object of default dict 
for item in my_list:
    my_counter[item] += 1
print(f'\nAfter incrementation by 1:\n {my_counter}')

new_dict ={}

# print(new_dict['key']) -> error since there is no such key 

new_dict2 = defaultdict(int)
print(new_dict2['key'])

# keeps this order as it is in the beginning 
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

print(Counter(colours))
print(Counter([1, 1, 2, 3, 3, 3, 4, 4, 4, 4]))


d = deque() 
d.append(20)
d.append(12)
d.append(21)
d.append(22)
print(d)

d2 = deque(range(5))
print(d2)
print(d2.popleft()) 
print(d2)
print(d2.pop())
print(d2) 

class Direction(Enum):
    North= 'N'
    South='S'
    East='E'
    West= 'W'

for dir in Direction:
    print(dir)
print(Direction.South)