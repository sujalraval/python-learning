
# 1. Basic Type Hints for Parameters and Return Values
def add_numbers(a: int, b: int) -> int:
    """
    This function adds two integers and returns their sum.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The sum of the two integers.
    """
    return a + b

# Calling the function with integers
result = add_numbers(5, 3)
print("Sum of 5 and 3:", result)  # Output: 8

# 2. Type Hinting with Strings
def greet(name: str) -> str:
    """
    This function returns a greeting message for the provided name.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

# Calling the function with a string argument
greeting_message = greet("Alice")
print(greeting_message)  # Output: Hello, Alice!

# 3. Type Hinting for Multiple Return Values (Tuple)
from typing import Tuple

def get_name_and_age() -> Tuple[str, int]:
    """
    This function returns a tuple containing a name (str) and age (int).
    
    Returns:
    tuple: A tuple with a name and age.
    """
    return "John Doe", 30

# Unpacking the returned tuple
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")  # Output: Name: John Doe, Age: 30

# 4. Type Hinting with Lists
from typing import List

def get_numbers() -> List[int]:
    """
    This function returns a list of integers.
    
    Returns:
    list: A list of integers.
    """
    return [1, 2, 3, 4, 5]

# Calling the function that returns a list
numbers = get_numbers()
print("Numbers:", numbers)  # Output: Numbers: [1, 2, 3, 4, 5]

# 5. Type Hinting with Optional Parameters (Optional)
from typing import Optional

def find_item(items: List[str], search_item: str) -> Optional[str]:
    """
    This function searches for an item in a list of strings and returns it if found.
    
    Parameters:
    items (list): A list of strings to search in.
    search_item (str): The item to search for.
    
    Returns:
    str or None: The found item, or None if not found.
    """
    if search_item in items:
        return search_item
    return None

# Calling the function with a list of items
items_list = ["apple", "banana", "orange"]
found_item = find_item(items_list, "banana")
print(f"Found item: {found_item}")  # Output: Found item: banana

# 6. Type Hinting with Dictionaries
from typing import Dict

def get_student_scores() -> Dict[str, int]:
    """
    This function returns a dictionary where the keys are student names and the values are their scores.
    
    Returns:
    dict: A dictionary of student names and scores.
    """
    return {"Alice": 85, "Bob": 90, "Charlie": 78}

# Calling the function that returns a dictionary
scores = get_student_scores()
print("Student Scores:", scores)  # Output: Student Scores: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# 7. Type Hinting with Callable (Functions as Parameters)
from typing import Callable

def execute_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    """
    This function accepts two integers and a function (operation) as a parameter and applies the operation to the integers.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    operation (Callable): A function that takes two integers and returns an integer.
    
    Returns:
    int: The result of the operation.
    """
    return operation(a, b)

# Example of a function to pass as an operation
def multiply(x: int, y: int) -> int:
    return x * y

# Calling the function with a custom operation
result = execute_operation(5, 3, multiply)
print("Multiplication result:", result)  # Output: 15

# Conclusion:
# Type hints in Python improve code readability and provide better support for static analysis and IDEs.
# They don't enforce types at runtime but are helpful for developers in maintaining clear and correct code.
