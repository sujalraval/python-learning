# variable_naming_conventions_and_assignments.py

"""
This file demonstrates how to declare variables in Python, discusses variable naming conventions, 
provides examples including reassigning variables, and shows multiple assignments.
"""

# Variable Declaration
# A variable is a name used to refer to data stored in memory.

# Example:
message = "Hello, World!"  # A string variable
age = 25  # An integer variable
price = 99.99  # A float variable

# Printing variables to show their values
print(message)  # Output: Hello, World!
print(age)      # Output: 25
print(price)    # Output: 99.99

# Reassigning Variables
# Variables can be reassigned to hold new values of the same or different types.

message = "Goodbye, World!"  # Reassigned the string value
age = 30  # Reassigned the integer value
price = 89.50  # Reassigned the float value

# Printing reassigned variables to show their new values
print(message)  # Output: Goodbye, World!
print(age)      # Output: 30
print(price)    # Output: 89.50

# Multiple Assignments
# Python allows assigning values to multiple variables in a single statement.

x, y, z = 10, 20, 30  # Assigning values 10, 20, and 30 to x, y, and z respectively
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

# Assigning the same value to multiple variables
a = b = c = 100  # All three variables hold the value 100
print(a)  # Output: 100
print(b)  # Output: 100
print(c)  # Output: 100


# Naming Conventions for Variables

# Variable names should be meaningful and describe the stored data.

greeting_message = "Welcome to the platform!"  # Clear and descriptive
total_price = 150.75  # Describes the purpose of the variable

# Variables cannot begin with numbers or special characters except the underscore.
  
_name = "John"     # Starts with an underscore
user_age = 30      # Starts with a letter

# Variable names should only contain letters, numbers, and underscores (_). Avoid symbols like @, #, $, etc.
  

# Use underscores or camelCase to separate words in variable names.
  
user_address = "123 Street Name"  # Correct
firstName = "John"                # Correct camelCase style
# Incorrect Example:
# user address = "123 Street Name"  (This will raise a syntax error)


# Do not use Python's reserved keywords (like `class`, `def`, `return`) as variable names.
  
"""
Examples of Good and Bad Variable Names:

Good:
- student_count = 45
- total_amount = 300.50
- is_active = True

Bad:
- 1st_user = "Alice"  (Cannot start with a number)
- total$ = 200  (Special character not allowed)
- return = "Complete"  (Using a reserved keyword)
"""

# Demonstrating good variables with meaningful names
student_count = 45
total_amount = 300.50
is_active = True

# Reassigning variables to new values
student_count = 50  # New student count
total_amount = 350.75  # Updated total amount
is_active = False  # Changing the boolean value

# Print examples of meaningful variables after reassignment
print(student_count)  # Output: 50
print(total_amount)   # Output: 350.75
print(is_active)      # Output: False
