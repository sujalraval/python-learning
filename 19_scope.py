# 1. Global Scope
x = 10  # This variable is in the global scope

def print_global_x():
    """
    This function can access the global variable 'x' because it is defined in the global scope.
    """
    print(f"Global x: {x}")

# Calling the function
print_global_x()  # Output: Global x: 10

# 2. Local Scope
def define_local_variable():
    """
    This function defines a variable in the local scope, which is only accessible within this function.
    """
    local_var = "I am local"  # Local variable
    print(local_var)

# Calling the function to access the local variable
define_local_variable()  # Output: I am local

# Trying to access the local variable outside the function will cause an error
# print(local_var)  # Uncommenting this will raise a NameError: local_var is not defined

# 3. Function Modifying Global Variable with 'global' Keyword
counter = 0  # Global variable

def increase_counter():
    """
    This function modifies the global variable 'counter' using the global keyword.
    """
    global counter  # Declare that we're using the global 'counter' variable
    counter += 1

# Calling the function multiple times
increase_counter()
increase_counter()
print(f"Counter after increasing: {counter}")  # Output: Counter after increasing: 2

# 4. Nested Functions and Enclosing Scope (Nonlocal Scope)
def outer_function():
    """
    This function defines another function inside it, demonstrating nonlocal scope.
    """
    outer_var = "outer"
    
    def inner_function():
        """
        This function accesses the enclosing variable from the outer function.
        """
        nonlocal outer_var  # Modify the variable in the enclosing scope
        outer_var = "modified outer"
        print(f"Inner function: {outer_var}")
    
    inner_function()
    print(f"Outer function after modification: {outer_var}")

# Calling the outer function
outer_function()
# Output:
# Inner function: modified outer
# Outer function after modification: modified outer

# 5. Shadowing Global Variables
y = 5  # Global variable

def shadow_global_y():
    """
    This function defines a local variable with the same name as a global variable.
    It "shadows" the global variable inside the function.
    """
    y = 50  # Local variable with the same name as the global variable
    print(f"Local y (shadowing global y): {y}")

# Calling the function
shadow_global_y()  # Output: Local y (shadowing global y): 50

# The global variable 'y' remains unchanged
print(f"Global y: {y}")  # Output: Global y: 5

# Conclusion:
# - Variables defined outside functions are in the global scope and accessible globally.
# - Variables defined inside functions are in the local scope and accessible only within that function.
# - The `global` keyword allows modifying global variables within a function.
# - Nested functions can access variables from enclosing functions using the `nonlocal` keyword.
# - Local variables can shadow global variables, meaning the local version is used inside the function.
