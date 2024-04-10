"""
[list comprehension] Given a list of strings, create a new list that contains only the strings with more than 5 characters using list comprehension.
"""

def comprehend_list(list_of_string):
    return [s for s in list_of_string if len(s) >=5]

print(comprehend_list(['', 'p', 'E', 'Xj', 'ac', 'mGf', 'SQR', 'xFZL', 'RwIjn', 'vTJGkL']))