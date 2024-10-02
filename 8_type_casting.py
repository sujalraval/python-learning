# type_casting.py

"""
This file demonstrates type casting (type conversion) in Python, where values of one data type
can be converted into another data type using built-in functions.
"""

# Type Casting in Python

# 1. Integer to Float
int_value = 10  # An integer
float_value = float(int_value)  # Converting int to float
print("Integer to Float:", float_value)  # Output: 10.0
print("Type of float_value:", type(float_value))  # Output: <class 'float'>

# 2. Float to Integer (Note: This will truncate the decimal part)
float_value = 9.75  # A float
int_value = int(float_value)  # Converting float to int (truncates decimal)
print("\nFloat to Integer:", int_value)  # Output: 9
print("Type of int_value:", type(int_value))  # Output: <class 'int'>

# 3. Integer to String
int_value = 123  # An integer
string_value = str(int_value)  # Converting int to string
print("\nInteger to String:", string_value)  # Output: '123'
print("Type of string_value:", type(string_value))  # Output: <class 'str'>

# 4. String to Integer (Only works if the string contains numeric characters)
string_value = "456"
int_value = int(string_value)  # Converting string to int
print("\nString to Integer:", int_value)  # Output: 456
print("Type of int_value:", type(int_value))  # Output: <class 'int'>

# 5. String to Float
string_value = "78.90"
float_value = float(string_value)  # Converting string to float
print("\nString to Float:", float_value)  # Output: 78.9
print("Type of float_value:", type(float_value))  # Output: <class 'float'>

# 6. Float to String
float_value = 99.99
string_value = str(float_value)  # Converting float to string
print("\nFloat to String:", string_value)  # Output: '99.99'
print("Type of string_value:", type(string_value))  # Output: <class 'str'>

# 7. List to Tuple
list_value = [1, 2, 3, 4]  # A list
tuple_value = tuple(list_value)  # Converting list to tuple
print("\nList to Tuple:", tuple_value)  # Output: (1, 2, 3, 4)
print("Type of tuple_value:", type(tuple_value))  # Output: <class 'tuple'>

# 8. Tuple to List
tuple_value = (5, 6, 7, 8)  # A tuple
list_value = list(tuple_value)  # Converting tuple to list
print("\nTuple to List:", list_value)  # Output: [5, 6, 7, 8]
print("Type of list_value:", type(list_value))  # Output: <class 'list'>

# 9. Set to List
set_value = {10, 20, 30, 40}  # A set
list_value = list(set_value)  # Converting set to list
print("\nSet to List:", list_value)  # Output: [10, 20, 30, 40] (order may vary)
print("Type of list_value:", type(list_value))  # Output: <class 'list'>

# 10. List to Set
list_value = [100, 200, 300, 100]  # A list with duplicate values
set_value = set(list_value)  # Converting list to set (removes duplicates)
print("\nList to Set:", set_value)  # Output: {100, 200, 300}
print("Type of set_value:", type(set_value))  # Output: <class 'set'>

# Important: When converting from one type to another, make sure the data is compatible. 
# Otherwise, it may raise a ValueError.

# Example: String to Int Conversion with an invalid string will raise an error.
invalid_string = "abc123"
# Uncommenting the following line would raise a ValueError
# invalid_value = int(invalid_string)  # ValueError: invalid literal for int() with base 10: 'abc123'
