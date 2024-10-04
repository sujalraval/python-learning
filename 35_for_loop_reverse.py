"""
For Loop in Reverse in Python

A 'for loop' can iterate through a sequence in reverse order by using either the reversed() function or a negative step value in range().
"""

# 1. Using reversed() Function
# Example: Reverse a list of numbers

print("For Loop Using reversed():")
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)  # Output: 5, 4, 3, 2, 1

# 2. Using range() with a Negative Step
# Example: Counting down from 10 to 1

print("\nFor Loop Using range() with Negative Step:")
for i in range(10, 0, -1):  # Start at 10, end at 1, decrement by 1
    print(i)  # Output: 10, 9, 8, ..., 1

# 3. Reverse a String
# Example: Iterate over the characters of a string in reverse

print("\nFor Loop Reversing a String:")
word = "Python"
for char in reversed(word):
    print(char)  # Output: n, o, h, t, y, P

# 4. Reverse a List using slicing
# Example: Reverse a list with list slicing [::-1]

print("\nFor Loop Using List Slicing:")
for number in numbers[::-1]:  # Reverses the list
    print(number)  # Output: 5, 4, 3, 2, 1

"""
Key Takeaways:
- The 'reversed()' function is a straightforward way to iterate through a sequence in reverse order.
- A negative step in the 'range()' function can also be used to reverse the iteration over a range of numbers.
- Strings and lists can be reversed using 'reversed()' or slicing techniques.
"""
