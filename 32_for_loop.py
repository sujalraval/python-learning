"""
This file demonstrates various counting techniques using for loops in Python.
We will cover counting up, counting down, and iterating through ranges with steps.
"""

# 1. Counting Upwards
# Example: Count from 1 to 10

print("Counting Upwards:")
for count_up in range(1, 11):
    print(count_up)  # Output: 1, 2, 3, ..., 10

# 2. Counting Downwards
# Example: Count down from 10 to 1

print("\nCounting Downwards:")
for count_down in range(10, 0, -1):
    print(count_down)  # Output: 10, 9, 8, ..., 1

# 3. Counting Even Numbers
# Example: Count even numbers from 2 to 20

print("\nCounting Even Numbers:")
for even_count in range(2, 21, 2):
    print(even_count)  # Output: 2, 4, 6, ..., 20

# 4. Counting Odd Numbers
# Example: Count odd numbers from 1 to 19

print("\nCounting Odd Numbers:")
for odd_count in range(1, 20, 2):
    print(odd_count)  # Output: 1, 3, 5, ..., 19

# 5. Counting with a Step
# Example: Count from 0 to 100 with a step of 10

print("\nCounting with a Step of 10:")
for step_count in range(0, 101, 10):
    print(step_count)  # Output: 0, 10, 20, ..., 100

# 6. Reverse Step Counting
# Example: Count down from 100 to 0 with a step of 10

print("\nCounting Downwards with a Step of 10:")
for reverse_count in range(100, -1, -10):
    print(reverse_count)  # Output: 100, 90, 80, ..., 0

"""
Key Takeaways:
- For loops are powerful tools for iterating through ranges with flexible conditions.
- You can define start, stop, and step values for the range() function to control the counting behavior.
- This demonstrates various counting techniques using for loops.
"""
