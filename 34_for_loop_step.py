"""
For Loop with Step in Python

A 'for loop' can iterate through a sequence of numbers with a specified step value.
The step value defines how much the loop variable should increment (or decrement) after each iteration.
"""

# 1. For Loop with a Positive Step
# Example: Counting from 0 to 10 with a step of 2

print("For Loop with Step of 2:")
for i in range(0, 11, 2):  # Start at 0, end at 10, increment by 2
    print(i)  # Output: 0, 2, 4, 6, 8, 10

# 2. For Loop with a Negative Step
# Example: Counting down from 10 to 0 with a step of -2

print("\nFor Loop with Step of -2:")
for i in range(10, -1, -2):  # Start at 10, end at 0, decrement by 2
    print(i)  # Output: 10, 8, 6, 4, 2, 0

# 3. For Loop with Custom Step
# Example: Counting from 5 to 50 with a step of 5

print("\nFor Loop with Step of 5:")
for i in range(5, 51, 5):  # Start at 5, end at 50, increment by 5
    print(i)  # Output: 5, 10, 15, ..., 50

# 4. For Loop Counting Backwards
# Example: Counting down from 20 to 0 with a step of -5

print("\nFor Loop Counting Backwards with Step of -5:")
for i in range(20, -1, -5):  # Start at 20, end at 0, decrement by 5
    print(i)  # Output: 20, 15, 10, 5, 0

"""
Key Takeaways:
- The 'range()' function allows you to specify a start, stop, and step value for the loop.
- A positive step value increments the loop variable, while a negative step decrements it.
- By controlling the step value, you can easily create loops that count by any interval.
"""
