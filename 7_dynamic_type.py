# dynamic_types.py

"""
This file demonstrates Python's dynamic typing feature, where variables can change types during execution,
and also shows how to convert a string to an integer if the string contains numeric characters.
"""

# Dynamic Typing in Python

# Python does not require explicit type declarations. The type of a variable is determined at runtime.

# Example 1: Assigning an integer value to a variable
variable = 10  # variable is an integer
print("Initial Value:", variable)  # Output: 10
print("Type of variable:", type(variable))  # Output: <class 'int'>

# Example 2: Reassigning the same variable to a string
variable = "Python is dynamically typed!"  # Now variable is a string
print("\nUpdated Value:", variable)  # Output: Python is dynamically typed!
print("Type of variable:", type(variable))  # Output: <class 'str'>

# Example 3: Reassigning the same variable to a list
variable = [1, 2, 3, 4, 5]  # Now variable is a list
print("\nReassigned to List:", variable)  # Output: [1, 2, 3, 4, 5]
print("Type of variable:", type(variable))  # Output: <class 'list'>

# Example 4: Using the same variable as a float
variable = 99.99  # Now variable is a float
print("\nReassigned to Float:", variable)  # Output: 99.99
print("Type of variable:", type(variable))  # Output: <class 'float'>

# Example 5: Converting a string containing numbers to an integer
numeric_string = "123"  # This is a string containing numeric characters
print("\nString Value:", numeric_string)  # Output: 123
print("Type of 'numeric_string':", type(numeric_string))  # Output: <class 'str'>

# We can convert the string to an integer using the int() function if the string contains numeric characters.
numeric_value = int(numeric_string)  # Converts string to an integer
print("Converted to Integer:", numeric_value)  # Output: 123
print("Type of 'numeric_value':", type(numeric_value))  # Output: <class 'int'>

# Example 6: Potential error when trying to convert non-numeric strings to integers
invalid_string = "abc123"  # This string contains non-numeric characters
print("\nInvalid String:", invalid_string)  # Output: abc123

# Uncommenting the following line would raise a ValueError:
# numeric_value = int(invalid_string)  # ValueError: invalid literal for int() with base 10: 'abc123'

# Solution: Check if the string is numeric before converting
if invalid_string.isnumeric():
    numeric_value = int(invalid_string)
    print("Converted 'invalid_string' to Integer:", numeric_value)
else:
    print("Cannot convert 'invalid_string' to an integer!")  # Output: Cannot convert 'invalid_string' to an integer!

# Type Conversion:
# Python provides built-in functions like int(), float(), str(), etc., to convert types when needed.
