# 1. Positional Parameters
def subtract(a, b):
    """
    This function subtracts two numbers using positional parameters.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The result of a - b.
    """
    return a - b

# Calling the function with positional arguments
result = subtract(10, 5)
print("10 minus 5:", result)  # Output: 5

# 2. Keyword Parameters
def describe_pet(animal_type, pet_name):
    """
    This function describes a pet using keyword parameters.
    
    Parameters:
    animal_type (str): The type of the animal.
    pet_name (str): The name of the pet.
    """
    print(f"I have a {animal_type} named {pet_name}.")

# Calling the function with keyword arguments
describe_pet(animal_type="dog", pet_name="Buddy")  # Output: I have a dog named Buddy.

# 3. Default Parameters
def power(base, exponent=2):
    """
    This function raises a base to a given exponent, with a default exponent of 2.
    
    Parameters:
    base (int or float): The base number.
    exponent (int): The exponent to raise the base to. Default is 2.
    
    Returns:
    int or float: The result of base raised to the exponent.
    """
    return base ** exponent

# Calling the function with and without the default parameter
print("2 to the power of 3:", power(2, 3))  # Output: 8
print("3 to the power of 2:", power(3))      # Output: 9 (uses default exponent)

# 4. Variable-length Parameters
def concatenate_strings(*args):
    """
    This function concatenates a variable number of strings.
    
    Parameters:
    *args: A variable number of string arguments.
    
    Returns:
    str: The concatenated string.
    """
    return " ".join(args)

# Calling the function with multiple arguments
concatenated_result = concatenate_strings("Hello", "World!", "Welcome", "to", "Python.")
print("Concatenated string:", concatenated_result)  # Output: Hello World! Welcome to Python.

# 5. Combining Different Parameter Types
def full_introduction(name, age, *hobbies, city="Unknown"):
    """
    This function provides a full introduction using various parameter types.
    
    Parameters:
    name (str): The name of the person.
    age (int): The age of the person.
    *hobbies: A variable number of hobbies.
    city (str): The city of the person. Default is "Unknown".
    """
    print(f"Hi, my name is {name}, I am {age} years old, and I live in {city}.")
    if hobbies:
        print("My hobbies are:", ", ".join(hobbies))

# Calling the function with different arguments
full_introduction("Alice", 25, "reading", "hiking", city="New York")
# Output:
# Hi, my name is Alice, I am 25 years old, and I live in New York.
# My hobbies are: reading, hiking

# Conclusion:
# Understanding how to use different types of parameters in functions allows for greater flexibility and modularity in code.
# This enhances code reusability and maintainability.
