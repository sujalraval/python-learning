"""
Introduction to For Loops in Python

A 'for loop' is used for iterating over a sequence (such as a list, tuple, string, or range).
With each iteration, the loop takes the next element from the sequence and performs the block of code.
"""

# Basic For Loop
# Example: Iterating through a list of numbers

print("Basic For Loop:")
numbers = [1, 2, 3, 4, 5]  # A list of numbers
for number in numbers:
    print(number)  # Output: 1, 2, 3, 4, 5

# For Loop with Strings
# Example: Iterating through characters in a string

print("\nFor Loop with Strings:")
word = "Python"
for char in word:
    print(char)  # Output: P, y, t, h, o, n

# For Loop with Ranges
# Example: Iterating using a range of numbers (0 to 4)

print("\nFor Loop with Ranges:")
for i in range(5):  # Will iterate from 0 to 4
    print(i)  # Output: 0, 1, 2, 3, 4

"""
Key Takeaways:
- A for loop iterates over each item in a sequence, such as a list, string, or range.
- The range() function is often used to generate a sequence of numbers.
- A for loop continues until all items in the sequence have been iterated over.
"""
