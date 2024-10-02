# 1. Basic Structure of a While Loop
# The basic syntax of a while loop is:
# while condition:
#     # Code to execute while condition is True

# Example 1: Counting Down from 5
countdown = 5

while countdown > 0:
    print(countdown)  # Output: 5, 4, 3, 2, 1
    countdown -= 1  # Decrease the countdown by 1

print("Liftoff!")  # Output: Liftoff!

# 2. Infinite Loop Example
# Be cautious with while loops; if the condition is always True, it can lead to an infinite loop.

# Uncommenting the following code will create an infinite loop:
# while True:
#     print("This will run forever unless stopped.")

# 3. Using a Break Statement
# You can use the break statement to exit a while loop prematurely.

number = 0

while number < 10:
    print(number)  # Output: 0 to 9
    number += 1
    if number == 5:
        print("Breaking the loop at 5.")
        break  # Exit the loop when number is 5

# 4. Using a Continue Statement
# You can use the continue statement to skip the current iteration and move to the next one.

number = 0

while number < 10:
    number += 1
    if number == 5:
        print("Skipping 5.")  # Output: Skipping 5.
        continue  # Skip the rest of the loop when number is 5
    print(number)  # Output: 1, 2, 3, 4, 6, 7, 8, 9, 10

# 5. Using While Loop for User Input
# While loops can be useful for repeatedly asking for user input until a valid input is received.

user_input = ""

while user_input.lower() != "exit":
    user_input = input("Type 'exit' to quit: ")
    print(f"You typed: {user_input}")

# 6. Example: Summing Numbers Until a Condition is Met
# This example demonstrates using a while loop to sum numbers until a certain condition is met.

total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break  # Exit the loop if the user enters 0
    total += number  # Add the entered number to total

print(f"The total is: {total}")  # Output the total sum

"""
Key Takeaways:
- A while loop repeats a block of code as long as a condition is True.
- Be cautious of infinite loops; ensure the loop condition will eventually be False.
- Use the break statement to exit the loop early, and use continue to skip the current iteration.
- While loops are useful for scenarios where the number of iterations is not known in advance, such as user input.
"""
