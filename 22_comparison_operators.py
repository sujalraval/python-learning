# 1. Equal to (==)
x = 5
y = 10

# Checking if two values are equal
print(x == y)  # Output: False (since 5 is not equal to 10)

# 2. Not equal to (!=)
# Checking if two values are not equal
print(x != y)  # Output: True (since 5 is not equal to 10)

# 3. Greater than (>)
# Checking if x is greater than y
print(x > y)  # Output: False (since 5 is not greater than 10)

# 4. Less than (<)
# Checking if x is less than y
print(x < y)  # Output: True (since 5 is less than 10)

# 5. Greater than or equal to (>=)
# Checking if x is greater than or equal to y
print(x >= y)  # Output: False (since 5 is not greater than or equal to 10)

# 6. Less than or equal to (<=)
# Checking if x is less than or equal to y
print(x <= y)  # Output: True (since 5 is less than or equal to 10)

# 7. Chained Comparisons
# You can chain comparison operators together to check multiple conditions in one line
z = 7
print(x < z < y)  # Output: True (since 5 < 7 < 10 is true)

# 8. Using comparison operators with strings
name1 = "Alice"
name2 = "Bob"

# Strings are compared lexicographically (alphabetically)
print(name1 == name2)  # Output: False (since "Alice" is not equal to "Bob")
print(name1 < name2)   # Output: True (since "Alice" comes before "Bob" alphabetically)

"""
Comparison Operators:
- == : Equal to
- != : Not equal to
- >  : Greater than
- <  : Less than
- >= : Greater than or equal to
- <= : Less than or equal to
"""

# 9. Comparisons with booleans
is_active = True
is_admin = False

# Checking boolean comparisons
print(is_active == True)   # Output: True (since is_active is True)
print(is_admin != True)    # Output: True (since is_admin is False)

# 10. Comparing different types (int vs string)
num = 10
string_num = "10"

# Direct comparison between int and string would fail
# print(num == string_num)  # Uncommenting this line would return False because 10 (int) is not "10" (string)

# To compare, we need to convert one type to another
print(num == int(string_num))  # Output: True (after converting "10" to integer)

"""
Key Takeaways:
- Comparison operators are used to compare values and return a boolean result.
- Chaining comparisons can check multiple conditions in a single statement.
- String comparisons are lexicographical (alphabetical).
- Be careful when comparing different data types; conversions may be needed.
"""

