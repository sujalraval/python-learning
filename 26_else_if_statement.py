# 1. Basic if-elif-else Structure
# A simple example with multiple conditions using elif

temperature = 25

if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a pleasant day.")  # Output: It's a pleasant day.
elif temperature > 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")

# In this example, since temperature is 25, only the second condition is True,
# so the message "It's a pleasant day." is printed.

# 2. Checking Multiple Conditions with elif
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")  # Output: Grade: B
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")


# 3. Using elif to Categorize Age Groups
age = 45

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")  # Output: Adult
else:
    print("Senior Citizen")

# The conditions are checked from top to bottom. As soon as a True condition is found,
# the corresponding code block is executed, and the rest of the conditions are skipped.

# 4. Combining elif with Logical Operators
score = 85
attendance = 90

if score >= 90 and attendance >= 85:
    print("Excellent student.")
elif score >= 75 and attendance >= 75:
    print("Good student.")  # Output: Good student.
elif score >= 60:
    print("Average student.")
else:
    print("Needs improvement.")

# 5. elif without else
# In Python, you don't always need to use an `else` block. You can end with an elif if it's not necessary to handle a final default case.

color = "blue"

if color == "red":
    print("The color is red.")
elif color == "blue":
    print("The color is blue.")  # Output: The color is blue.
elif color == "green":
    print("The color is green.")

# Since the value of the variable `color` is "blue", the elif block for "blue" is executed.


# 6. Nested elif Statements
# You can also nest if-elif statements to handle more complex conditions.

income = 50000

if income > 100000:
    if income > 200000:
        print("High-income group.")
    else:
        print("Upper middle-income group.")
elif income > 50000:
    print("Middle-income group.")
else:
    print("Low-income group.")  # Output: Low-income group.


"""
Key Takeaways:
- The elif statement stands for "else if" and allows you to check multiple conditions in an if-else structure.
- elif statements are useful when you need to execute different code based on several conditions.
- Once a condition is True, the corresponding block executes, and the remaining conditions are skipped.
- You can use elif without an else block if you don't need to handle a default case.
- elif can be combined with logical operators like and/or for more complex condition checks.
- Nested if-elif statements are possible when you need to check conditions within another if block.
"""
