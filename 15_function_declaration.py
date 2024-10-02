# 1. Basic Function Declaration
def say_hello():
    """
    This function prints a simple greeting.
    """
    print("Hello, World!")

# Calling the basic function
say_hello()  # Output: Hello, World!

# 2. Function with Positional Parameters
def multiply(a, b):
    """
    This function multiplies two numbers.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The product of a and b.
    """
    return a * b

# Calling the function with positional arguments
result = multiply(3, 4)
print("3 multiplied by 4:", result)  # Output: 12

# 3. Function with Default Parameters
def greet(name="User"):
    """
    This function greets a person with a default name.
    
    Parameters:
    name (str): The name of the person to greet. Default is "User".
    """
    print(f"Hello, {name}!")

# Calling the function with and without the default parameter
greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, User!

# 4. Function with Keyword Parameters
def introduce(name, age):
    """
    This function introduces a person using keyword parameters.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    """
    print(f"My name is {name} and I am {age} years old.")

# Calling the function with keyword arguments
introduce(age=30, name="Bob")  # Output: My name is Bob and I am 30 years old.

# 5. Function with Variable-length Parameters
def calculate_sum(*numbers):
    """
    This function calculates the sum of any number of arguments.
    
    Parameters:
    *numbers: A variable number of numeric arguments.
    
    Returns:
    int or float: The sum of all provided numbers.
    """
    return sum(numbers)

# Calling the function with multiple arguments
total = calculate_sum(1, 2, 3, 4, 5)
print("Total sum:", total)  # Output: 15

# 6. Function with Both Positional and Keyword Parameters
def detailed_greet(greeting, *names, punctuation="."):
    """
    This function greets multiple people with a customizable greeting.
    
    Parameters:
    greeting (str): The greeting phrase.
    *names: A variable number of names.
    punctuation (str): The punctuation to end the greeting. Default is '.'.
    """
    for name in names:
        print(f"{greeting}, {name}{punctuation}")

# Calling the function with different arguments
detailed_greet("Hello", "Alice", "Bob", "Charlie", punctuation="!")  
# Output: Hello, Alice! Hello, Bob! Hello, Charlie!

# Conclusion:
# Function declarations in Python allow for flexible and powerful code organization.
# Understanding how to declare functions with various parameters enhances code readability and reusability.
