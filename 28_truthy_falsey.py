# 1. What are Truthy and Falsy Values?
# Truthy values are those that evaluate to True in a boolean context.
# Falsy values are those that evaluate to False.

# 2. Common Falsy Values in Python
# The following values are considered falsy in Python:
# - None
# - False
# - 0 (zero of any numeric type)
# - Empty sequences or collections (e.g., "", [], {}, set())

falsy_values = [None, False, 0, "", [], {}, set()]

for value in falsy_values:
    if not value:  # This condition checks for falsy values
        print(f"{value!r} is falsy.")  # Output for each falsy value.

# 3. Common Truthy Values in Python
# Any value that is not falsy is considered truthy. Some examples include:
# - Non-zero numbers
# - Non-empty sequences or collections (e.g., "Hello", [1, 2], {1: "one"})

truthy_values = [1, -1, 3.14, "Hello", [1, 2], {1: "one"}, set([1])]

for value in truthy_values:
    if value:  # This condition checks for truthy values
        print(f"{value!r} is truthy.")  # Output for each truthy value.

# 4. Using Truthy and Falsy in Conditional Statements
# You can use truthy and falsy values directly in if statements.

user_input = ""

if user_input:  # Check if user_input is truthy (non-empty)
    print("User provided input.")
else:
    print("No input provided.")  # Output: No input provided.

# 5. Example: Checking User Age
age = 18

if age:
    print("Age is provided.")  # Output: Age is provided.
else:
    print("Age is not provided.")

# 6. Truthy and Falsy in Lists
# When working with lists, you can check if a list is empty or not.

my_list = [1, 2, 3]

if my_list:  # Check if the list is truthy (non-empty)
    print("List has elements.")  # Output: List has elements.
else:
    print("List is empty.")

# 7. Practical Example: Function Returning Values
def check_status(status):
    if status:
        print("Status is active.")  # Output when status is truthy.
    else:
        print("Status is inactive.")  # Output when status is falsy.

check_status(True)  # Output: Status is active.
check_status(False)  # Output: Status is inactive.

"""
Key Takeaways:
- Truthy values evaluate to True, while falsy values evaluate to False in boolean contexts.
- Common falsy values include None, False, 0, and empty collections.
- Any value that is not falsy is considered truthy, including non-zero numbers and non-empty collections.
- You can directly use truthy and falsy values in conditional statements to control flow based on their presence or absence.
"""
