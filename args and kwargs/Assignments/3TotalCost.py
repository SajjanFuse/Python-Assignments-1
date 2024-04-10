"""
[**kwargs] Write a Python function calculate_total_cost that
 calculates the total cost of items purchased from a store.
 The function should accept multiple keyword arguments,
 where the key is the item name, and the value is the item's price.
 The function should return the total cost of all items.
"""

def calculate_total_cost(**kwargs):
    total_cost = 0
    for item, price in kwargs.items():
        total_cost+=price 

    return total_cost

# Empty dictionary
dict1 = {}
print(calculate_total_cost(**dict1))  

# Dictionary with one item
dict2 = {"apple": 1.5}
print(calculate_total_cost(**dict2))  

# Dictionary with multiple items
dict3 = {"apple": 1.5, "banana": 0.75, "orange": 0.99, "mango": 5.99, "litchi": 1.99, }
print(calculate_total_cost(**dict3))  

# Dictionary with items of different prices
dict4 = {"shirt": 20.99, "pants": 30.50, "shoes": 49.99}
print(calculate_total_cost(**dict4))  

# Dictionary with items of the same price
dict5 = {"pen": 0.5, "pencil": 0.5, "eraser": 0.5}
print(calculate_total_cost(**dict5))  

# Dictionary with no items
dict6 = {"": 0}
print(calculate_total_cost(**dict6))  
