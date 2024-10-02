# 1. Basic if Statement
x = 10

# Check if x is greater than 5
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# 2. if-else Statement
y = 3

# Check if y is greater than 5, otherwise print a different message
if y > 5:
    print("y is greater than 5")
else:
    print("y is less than or equal to 5")  # Output: y is less than or equal to 5


# 3. if-elif-else Statement
z = 8

# Check multiple conditions using elif (else if)
if z > 10:
    print("z is greater than 10")
elif z == 8:
    print("z is equal to 8")  # Output: z is equal to 8
else:
    print("z is less than 8")


# 4. Nested if Statements
a = 12

# You can nest if statements within other if statements
if a > 10:
    print("a is greater than 10")  # Output: a is greater than 10
    if a < 20:
        print("a is also less than 20")  # Output: a is also less than 20


# 5. Multiple Conditions with Logical Operators (and, or, not)
age = 25
has_id = True

# Use 'and' to check if both conditions are true
if age >= 18 and has_id:
    print("You are allowed to enter.")  # Output: You are allowed to enter.

# Use 'or' to check if at least one condition is true
if age >= 18 or has_id:
    print("You are either old enough or have an ID.")  # Output: You are either old enough or have an ID.

# Use 'not' to negate a condition
is_logged_in = False
if not is_logged_in:
    print("Please log in.")  # Output: Please log in.


# 6. Ternary (Conditional) Operator
b = 15

# A shorter way to write if-else statements (ternary)
result = "b is even" if b % 2 == 0 else "b is odd"
print(result)  # Output: b is odd


# 7. Checking for Emptiness (Falsy Values)
my_list = []

# In Python, empty lists, strings, and other collections evaluate to False
if my_list:
    print("The list is not empty.")
else:
    print("The list is empty.")  # Output: The list is empty.

"""
Key Takeaways:
- The if statement is used to run code only if a condition is true.
- You can use if-else to handle both true and false conditions.
- The elif statement is used to check multiple conditions.
- Logical operators like 'and', 'or', and 'not' can combine multiple conditions.
- Python supports a shorthand ternary operator for simple if-else conditions.
- Empty sequences (like lists and strings) are considered False in Python.
"""
