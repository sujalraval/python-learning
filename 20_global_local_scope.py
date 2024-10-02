# 1. Global Scope
global_var = "I am global"  # This variable is declared in the global scope

def show_global_var():
    """
    This function can access the global variable 'global_var' because it's in the global scope.
    """
    print(f"Accessing global variable inside function: {global_var}")

# Accessing the global variable in the global scope
print(f"Accessing global variable in global scope: {global_var}")  # Output: I am global

# Calling the function to access the global variable
show_global_var()  # Output: Accessing global variable inside function: I am global


# 2. Local Scope
def show_local_scope():
    """
    This function defines a variable within the local scope.
    Local variables are only accessible inside the function where they are defined.
    """
    local_var = "I am local"
    print(f"Accessing local variable inside function: {local_var}")

# Calling the function to access the local variable
show_local_scope()  # Output: Accessing local variable inside function: I am local

# Trying to access a local variable outside its function will cause an error
# print(local_var)  # Uncommenting this will raise a NameError: local_var is not defined


# 3. Global vs Local Scope Example
counter = 10  # Global variable

def modify_counter():
    """
    This function defines a local variable with the same name as a global variable.
    The local variable 'counter' shadows the global variable inside the function.
    """
    counter = 5  # Local variable (shadows the global 'counter')
    print(f"Local 'counter' inside function: {counter}")  # Output: 5

# Calling the function
modify_counter()

# The global 'counter' remains unchanged
print(f"Global 'counter' after function call: {counter}")  # Output: 10


# 4. Using 'global' Keyword to Modify Global Variables
def increase_global_counter():
    """
    This function modifies the global variable 'counter' using the 'global' keyword.
    Without the 'global' keyword, a local variable would be created.
    """
    global counter  # Declare that we are using the global 'counter'
    counter += 1  # Modify the global variable

# Calling the function to modify the global variable
increase_global_counter()
print(f"Global 'counter' after modification: {counter}")  # Output: 11


# 5. Scope Rules Recap:
"""
- Global variables are declared outside functions and are accessible everywhere in the program.
- Local variables are declared inside functions and are only accessible within that function.
- Global variables can be accessed inside functions, but to modify them, you must use the 'global' keyword.
- Local variables with the same name as global variables will shadow the global ones inside the function, creating a new local variable.
"""
