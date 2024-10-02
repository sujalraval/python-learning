# Example 1: Trying to add a string and an integer (unsupported operand types)
try:
    result = "The number is: " + 10  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)
    # Correct approach: Convert the integer to a string before concatenation
    corrected_result = "The number is: " + str(10)
    print("Corrected:", corrected_result)  # Output: The number is: 10

# Example 2: Calling a string like a function
try:
    my_string = "Hello"
    result = my_string()  # This will raise a TypeError because strings are not callable
except TypeError as e:
    print("\nError:", e)
    # Correct approach: Remove the parentheses since we are not calling the string
    print("Corrected:", my_string)  # Output: Hello

# Example 3: Using the wrong type with arithmetic operators
try:
    result = 5 + "5"  # This will raise a TypeError
except TypeError as e:
    print("\nError:", e)
    # Correct approach: Convert the string to an integer before adding
    corrected_result = 5 + int("5")
    print("Corrected Result:", corrected_result)  # Output: 10

# Example 4: Trying to index a non-iterable object
try:
    number = 12345
    result = number[0]  # This will raise a TypeError because integers are not subscriptable
except TypeError as e:
    print("\nError:", e)
    # Correct approach: Convert the integer to a string if you want to access digits
    corrected_result = str(number)[0]
    print("Corrected Result:", corrected_result)  # Output: 1

# Example 5: Passing the wrong type to a built-in function
try:
    number_list = [1, 2, 3, 4]
    result = sum("12345")  # This will raise a TypeError because sum expects an iterable of numbers
except TypeError as e:
    print("\nError:", e)
    # Correct approach: Convert the string to a list of integers or remove the quotes
    corrected_result = sum([int(char) for char in "12345"])
    print("Corrected Result:", corrected_result)  # Output: 15

# Example 6: Incorrect use of types in function arguments
def multiply(a, b):
    return a * b

try:
    result = multiply(5, "abc")  # This will not raise a TypeError but results in unexpected behavior
    print("\nMultiplication Result:", result)  # Output: abcabcabcabcabc
except TypeError as e:
    print("\nError:", e)

# Solution: Handle such cases based on the desired output or add checks for types if necessary.
if isinstance(multiply(5, "abc"), str):
    print("Multiplication resulted in string repetition instead of numerical multiplication.")
