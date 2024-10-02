# 1. Function with Default Arguments
def greet(name="Guest", greeting="Hello"):
    """
    This function greets the user. 
    If no name or greeting is provided, it uses default values.
    """
    print(f"{greeting}, {name}!")

# Calling the function without any arguments (uses both default values)
greet()  # Output: Hello, Guest!

# Calling the function with only the 'name' argument (uses default greeting)
greet("Sujal")  # Output: Hello, Sujal!

# Calling the function with both arguments (no default values used)
greet("Sujal", "Welcome")  # Output: Welcome, Sujal!


# 2. Function with a Mix of Required and Default Arguments
def describe_person(name, age=30, country="India"):
    """
    This function describes a person with a required 'name' and default values for 'age' and 'country'.
    """
    print(f"Name: {name}, Age: {age}, Country: {country}")

# Calling the function with only the required argument
describe_person("John")  # Output: Name: John, Age: 30, Country: India

# Calling the function with all arguments
describe_person("Emily", 25, "USA")  # Output: Name: Emily, Age: 25, Country: USA


# 3. Important Notes on Default Arguments:
"""
- Default arguments must come after all required arguments in the function definition.
- If you provide an argument for a parameter with a default value, the default is overridden.
- You can mix required and default arguments, but required arguments must be passed first.
"""

# 4. Overriding only the middle default argument using keyword arguments
describe_person("Emily", country="Canada")  # Output: Name: Emily, Age: 30, Country: Canada

"""
Key Takeaways:
- Default arguments allow functions to be called with fewer arguments than defined.
- You can override default arguments by passing new values.
- Keyword arguments can be used to specify specific arguments, allowing you to skip some default values.
"""

# 5. Using Default Arguments with Mutables (Be Careful)
def add_item_to_list(item, my_list=[]):
    """
    This function demonstrates the issue with using mutable default arguments like lists.
    Default arguments are evaluated once at function definition time.
    """
    my_list.append(item)
    return my_list

# Calling the function multiple times
print(add_item_to_list("Apple"))  # Output: ['Apple']
print(add_item_to_list("Banana"))  # Output: ['Apple', 'Banana'] (unexpected behavior!)

# To avoid this, use `None` as the default value for mutable arguments
def add_item_to_list_fixed(item, my_list=None):
    """
    This is a better way to handle mutable default arguments.
    If no list is provided, a new list is created inside the function.
    """
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# Calling the fixed function
print(add_item_to_list_fixed("Apple"))   # Output: ['Apple']
print(add_item_to_list_fixed("Banana"))  # Output: ['Banana'] (expected behavior)
