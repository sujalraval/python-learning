# 1. Basic Use of Return Statement
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# Calling the function and storing the return value
sum_result = add_numbers(5, 3)
print("Sum of 5 and 3:", sum_result)  # Output: 8

# 2. Function Returning Multiple Values
def get_full_name(first_name, last_name):
    """
    This function returns both the first name and last name.
    
    Parameters:
    first_name (str): The first name.
    last_name (str): The last name.
    
    Returns:
    tuple: A tuple containing the full name and its length.
    """
    full_name = f"{first_name} {last_name}"
    return full_name, len(full_name)

# Calling the function and unpacking multiple return values
name, name_length = get_full_name("John", "Doe")
print(f"Full Name: {name}, Length: {name_length}")  # Output: Full Name: John Doe, Length: 8

# 3. Returning Different Data Types
def check_even_odd(number):
    """
    This function checks if a number is even or odd and returns a string message.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Calling the function and displaying the return message
result_message = check_even_odd(7)
print(result_message)  # Output: 7 is odd.

# 4. Returning None (Optional return)
def display_message(message):
    """
    This function displays a message but doesn't return anything (returns None by default).
    
    Parameters:
    message (str): The message to display.
    """
    print(message)

# Calling the function (It doesn't return anything)
display_message("This is a simple message.")  # Output: This is a simple message.

# 5. Early Return from a Function
def divide_numbers(a, b):
    """
    This function divides two numbers, but returns early if the divisor is 0.
    
    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.
    
    Returns:
    float: The result of the division, or None if division by zero.
    """
    if b == 0:
        print("Error: Division by zero.")
        return  # Early return if b is 0
    return a / b

# Calling the function with different values
result = divide_numbers(10, 2)
print("10 divided by 2:", result)  # Output: 5.0

result = divide_numbers(10, 0)  # Output: Error: Division by zero.

# Conclusion:
# The return statement is a crucial part of functions, allowing the result of the function's work to be used elsewhere in the program.
# It can return a single value, multiple values (as a tuple), different data types, or nothing at all.
