# Initialize two variables
x = 0
y = 5

# The loop will continue as long as both conditions are true
while x < 5 and y > 0:
    print(f"x: {x}, y: {y}")  # Print the values of x and y
    x += 1  # Increment x by 1
    y -= 1  # Decrement y by 1

# Once one of the conditions becomes false, the loop stops
print("The loop ended because one of the conditions is no longer true")

# Another example: managing multiple variables in a while loop

a = 2
b = 3
count = 0

# Loop runs while both a and b are less than 10
while a < 10 and b < 10:
    a += 1  # Increment a by 1
    b += 2  # Increment b by 2
    count += 1  # Increment the count
    print(f"Iteration {count}: a = {a}, b = {b}")

print("Loop completed when a or b reached 10")


# Example of using "or" in a while loop with multiple conditions

x = 0
y = 5

# The loop will continue as long as one of the conditions is true
while x < 5 or y > 0:
    print(f"x: {x}, y: {y}")
    x += 1  # Increment x by 1
    y -= 1  # Decrement y by 1

# Once both conditions become false, the loop stops
print("The loop ended because both conditions became false")
