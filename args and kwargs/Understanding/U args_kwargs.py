"""
Sajjan Acharya
11:22am , 10th April, 2024
Understanding the *args and **kwargs 
"""

#Important notes about the terms
"""
    - used in definitions of the functions
    - to pass an unspecified number of arguments to a function 
    (*args and *kwargs), * means any number of arguments
"""

# *args for sending non-keyworded variable length argument list 

def arg_func(arg1, *arguments):
    print(arg1)
    print(f'Type of args is {type(arguments)}\n')
    for arg in arguments:
        pass
        # print(arg)

arg_func(2,3,34,534,6,"324")

# **kwargs to pass keyworded variable length of arguments to function
# ** for named arguments ?
# named arguments are -> 

def kwargs_func(arg1, **others):
    print(arg1)
    print(f'\nType of kwargs is {type(others)}')
    

    for a, b in others.items():
        print(a, b)
        # pass 

kwargs_func({1:2,4:234,"sdf":234,"p":2,0:"sd"})

print('TOGETHER')

def args_kwargs(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

args = ("two", 3, 5)
args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
args_kwargs(**kwargs)
