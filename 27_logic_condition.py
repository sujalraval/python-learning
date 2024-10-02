# 1. Using the 'and' Operator
# The 'and' operator returns True if both conditions are True.

age = 25
has_permission = True

if age >= 18 and has_permission:
    print("You can vote.")  # Output: You can vote.
else:
    print("You cannot vote.")

# In this example, both conditions must be True for the message to print.


# 2. Using the 'or' Operator
# The 'or' operator returns True if at least one condition is True.

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax today!")  # Output: You can relax today!
else:
    print("You have to work today.")

# Here, if either is_weekend or is_holiday is True, the message is printed.


# 3. Using the 'not' Operator
# The 'not' operator negates a boolean value, returning True if the condition is False.

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")  # Output: You don't need an umbrella.
else:
    print("Take your umbrella.")

# This checks if it is not raining; if true, it prints the message.


# 4. Combining Logical Operators
# You can combine multiple logical operators for complex conditions.

temperature = 15
is_sunny = True

if temperature > 20 and (is_sunny or not is_raining):
    print("It's a nice day for a picnic.")
else:
    print("Stay indoors.")  # Output: Stay indoors.

# This checks if the temperature is above 20 and if it's sunny or not raining.


# 5. Example with User Input
# Demonstrating logical conditions with user input for a simple eligibility check.

is_student = True
is_member = False

if is_student or is_member:
    print("You are eligible for a discount!")  # Output: You are eligible for a discount!
else:
    print("No discounts available.")


# 6. Using Logical Conditions in Loops
# Logical conditions can also be used inside loops for more complex logic.

for i in range(1, 11):  # Numbers from 1 to 10
    if i % 2 == 0 and i > 5:
        print(f"{i} is an even number greater than 5.")  # Output for numbers like 6, 8, 10.


# 7. Chained Conditions
# You can chain multiple conditions together for more specific logic.

number = 15

if number > 0 and number < 20:
    print(f"{number} is between 1 and 20.")  # Output: 15 is between 1 and 20.
else:
    print(f"{number} is outside the range.")

"""
Key Takeaways:
- Logical operators 'and', 'or', and 'not' help combine multiple conditions.
- 'and' requires both conditions to be True; 'or' requires at least one condition to be True.
- 'not' negates the condition, making True become False and vice versa.
- Logical conditions can be combined for complex decision-making.
- User inputs can be incorporated for dynamic conditions.
- Logical conditions are often used within loops for repeated checks.
"""
