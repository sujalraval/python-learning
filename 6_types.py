# Basic Data Types in Python

# 1. Integer (int)
# Integers are whole numbers, positive or negative, without decimals.
age = 25  # Integer example
print("Age:", age)  # Output: Age: 25

# 2. Float (float)
# Floats are numbers that contain decimal points.
price = 99.99  # Float example
print("Price:", price)  # Output: Price: 99.99

# 3. String (str)
# Strings are sequences of characters, enclosed in single or double quotes.
name = "John Doe"  # String example
print("Name:", name)  # Output: Name: John Doe

# 4. Boolean (bool)
# Booleans represent two values: True or False.
is_active = True  # Boolean example
print("Is Active:", is_active)  # Output: Is Active: True

# 5. List (list)
# Lists are ordered and mutable collections, which can contain elements of different types.
fruits = ["apple", "banana", "cherry"]  # List example
print("Fruits:", fruits)  # Output: Fruits: ['apple', 'banana', 'cherry']

# 6. Tuple (tuple)
# Tuples are ordered and immutable collections. They are like lists but cannot be changed.
coordinates = (10.5, 20.0)  # Tuple example
print("Coordinates:", coordinates)  # Output: Coordinates: (10.5, 20.0)

# 7. Dictionary (dict)
# Dictionaries store data as key-value pairs. They are unordered and mutable.
student = {"name": "John", "age": 25, "grade": "A"}  # Dictionary example
print("Student Info:", student)  # Output: Student Info: {'name': 'John', 'age': 25, 'grade': 'A'}

# 8. Set (set)
# Sets are unordered collections of unique elements.
unique_numbers = {1, 2, 3, 3, 4, 5}  # Set example (duplicates will be ignored)
print("Unique Numbers:", unique_numbers)  # Output: Unique Numbers: {1, 2, 3, 4, 5}

# Type Checking
# You can check the type of any variable using the `type()` function.
print("Type of 'age':", type(age))  # Output: Type of 'age': <class 'int'>
print("Type of 'price':", type(price))  # Output: Type of 'price': <class 'float'>
print("Type of 'name':", type(name))  # Output: Type of 'name': <class 'str'>
print("Type of 'is_active':", type(is_active))  # Output: Type of 'is_active': <class 'bool'>
print("Type of 'fruits':", type(fruits))  # Output: Type of 'fruits': <class 'list'>
print("Type of 'coordinates':", type(coordinates))  # Output: Type of 'coordinates': <class 'tuple'>
print("Type of 'student':", type(student))  # Output: Type of 'student': <class 'dict'>
print("Type of 'unique_numbers':", type(unique_numbers))  # Output: Type of 'set': <class 'set'>

# Special Data Type: None
# The 'None' type represents the absence of a value.
not_defined = None  # None example
print("Not Defined:", not_defined)  # Output: Not Defined: None
print("Type of 'not_defined':", type(not_defined))  # Output: Type of 'not_defined': <class 'NoneType'>
