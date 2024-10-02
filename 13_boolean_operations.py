# Initialize some boolean variables
a = True
b = False

# 1. AND Operator
and_result = a and b  # True if both a and b are True
print("AND Operation: a and b =", and_result)  # Output: False

# Using AND with conditions
num1 = 10
num2 = 5
and_condition_result = (num1 > 5) and (num2 < 10)  # True if both conditions are True
print("AND with Conditions: (num1 > 5) and (num2 < 10) =", and_condition_result)  # Output: True

# 2. OR Operator
or_result = a or b  # True if either a or b is True
print("\nOR Operation: a or b =", or_result)  # Output: True

# Using OR with conditions
or_condition_result = (num1 < 5) or (num2 < 10)  # True if at least one condition is True
print("OR with Conditions: (num1 < 5) or (num2 < 10) =", or_condition_result)  # Output: True

# 3. NOT Operator
not_result_a = not a  # Inverts the value of a
not_result_b = not b  # Inverts the value of b
print("\nNOT Operation: not a =", not_result_a)  # Output: False
print("NOT Operation: not b =", not_result_b)  # Output: True

# Using NOT with conditions
not_condition_result = not (num1 == num2)  # True if num1 is not equal to num2
print("NOT with Condition: not (num1 == num2) =", not_condition_result)  # Output: True

# Conclusion:
# Boolean operations are essential for controlling the flow of programs,
# allowing for conditional execution based on logical conditions.
