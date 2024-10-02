# 1. Defining a Function
def greet(name):
    """
    This function takes a name as an argument and prints a greeting.
    
    Parameters:
    name (str): The name of the person to greet.
    """
    print(f"Hello, {name}!")

# 2. Calling the Function
greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!

# 3. Function with Return Value
def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# 4. Using the Return Value
result = add_numbers(5, 7)
print("Sum of 5 and 7:", result)  # Output: 12

# 5. Function with Default Parameter
def greet_with_default(name="Guest"):
    """
    This function greets a person, using "Guest" as the default name.
    
    Parameters:
    name (str): The name of the person to greet. Default is "Guest".
    """
    print(f"Hello, {name}!")

# 6. Calling Function with Default Parameter
greet_with_default()          # Output: Hello, Guest!
greet_with_default("Charlie") # Output: Hello, Charlie!

# 7. Function with Variable Number of Arguments
def sum_all(*args):
    """
    This function takes a variable number of arguments and returns their sum.
    
    Parameters:
    *args: A variable number of arguments.
    
    Returns:
    int or float: The sum of all arguments.
    """
    return sum(args)

# 8. Using Variable Arguments Function
total = sum_all(1, 2, 3, 4, 5)
print("Sum of all arguments:", total)  # Output: 15

# Conclusion:
# Functions are essential for organizing and reusing code.
# They improve code readability and allow for modular programming.
