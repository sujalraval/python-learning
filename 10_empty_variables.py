# empty_variable.py

"""
This file demonstrates the concept of empty variables in Python.
An empty variable is a variable that has been declared but has no value or contains no items.
"""

# 1. Empty String
empty_string = ""  # An empty string
print("Empty String:", empty_string)  # Output: ''
print("Is empty_string empty?", not empty_string)  # Output: True

# 2. None Type
none_value = None  # A variable that is explicitly set to None
print("\nNone Value:", none_value)  # Output: None
print("Is none_value None?", none_value is None)  # Output: True

# 3. Empty List
empty_list = []  # An empty list
print("\nEmpty List:", empty_list)  # Output: []
print("Is empty_list empty?", len(empty_list) == 0)  # Output: True

# 4. Empty Tuple
empty_tuple = ()  # An empty tuple
print("\nEmpty Tuple:", empty_tuple)  # Output: ()
print("Is empty_tuple empty?", len(empty_tuple) == 0)  # Output: True

# 5. Empty Dictionary
empty_dict = {}  # An empty dictionary
print("\nEmpty Dictionary:", empty_dict)  # Output: {}
print("Is empty_dict empty?", len(empty_dict) == 0)  # Output: True

# 6. Empty Set
empty_set = set()  # An empty set
print("\nEmpty Set:", empty_set)  # Output: set()
print("Is empty_set empty?", len(empty_set) == 0)  # Output: True

# Conclusion: 
# An empty variable can represent the absence of a value or the lack of items in a collection.
# These empty variables are useful for initializing and managing data structures in Python.
