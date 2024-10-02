# 1. Variables declared outside an if statement (global scope) can be accessed inside it
x = 10  # Global scope

if x > 5:
    print(f"x is {x}, and it's accessible inside the if statement.")  # Output: x is 10, and it's accessible inside the if statement.


# 2. Variables declared inside an if statement are limited to the block's scope
if x > 5:
    y = 20  # y is declared inside the if statement (local to this block)
    print(f"y is {y} inside the if statement.")  # Output: y is 20

# Trying to access y outside the if block
# print(y)  # Uncommenting this line would raise a NameError because y is not accessible here.


# 3. Variable shadowing: A variable declared inside an if block can have the same name as a global variable, but it will only be accessible inside the block.
z = 30  # Global variable

if z == 30:
    z = 100  # Local to this block (shadowing the global variable z)
    print(f"Inside if block, z is {z}")  # Output: Inside if block, z is 100

# The global variable z remains unchanged outside the if block
print(f"Outside if block, z is {z}")  # Output: Outside if block, z is 100 (since the local z modified the global one)


# 4. Scope in nested if statements
if x > 5:
    if y == 20:
        a = 50  # Variable a is declared in this nested if statement
        print(f"a is {a} inside the nested if statement.")  # Output: a is 50

# Variable a is accessible outside both if blocks since it's not confined to the if scope
print(f"a is {a} outside the nested if.")  # Output: a is 50


# 5. Using variables outside if statements
# Variables declared inside the block can only be used outside if they were declared in a higher (outer) scope.

if x < 15:
    b = 40  # b is declared inside the if block and can be used later if the block is executed

# Since the condition was true, b is now accessible outside the if block
print(f"b is {b} and accessible outside the if.")  # Output: b is 40


# 6. Variable declarations in else/elif blocks
# Variables declared inside an else or elif block will only be available in that block.

if x > 15:
    c = 60  # This block won't execute, so c won't be declared
else:
    c = 70  # c is declared here because this block executes
    print(f"c is {c} inside the else block.")  # Output: c is 70

# Now, c is accessible outside because the else block was executed
print(f"c is {c} outside the else block.")  # Output: c is 70

"""
Key Takeaways:
- Variables declared outside of an if statement (global scope) can be accessed inside the block.
- Variables declared inside an if block are local to that block and can't be accessed outside unless the block executes.
- Variable shadowing occurs when a variable declared inside a block has the same name as a global variable.
- Nested if statements follow the same scoping rules.
- Variables declared in else/elif blocks will only be accessible if the respective block executes.
"""
