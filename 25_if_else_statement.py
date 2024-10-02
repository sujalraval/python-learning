# 1. Basic if-else Statement
number = 10

# Check if the number is positive or negative
if number > 0:
    print(f"{number} is positive.")  # Output: 10 is positive.
else:
    print(f"{number} is negative or zero.")


# 2. if-elif-else Statement
temperature = 25

# Check the temperature range and print the appropriate message
if temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a pleasant day.")  # Output: It's a pleasant day.
else:
    print("It's a cold day.")


# 3. Multiple Conditions with Logical Operators
age = 20
has_ticket = True

# Check if the person is allowed to enter an event based on age and ticket possession
if age >= 18 and has_ticket:
    print("You are allowed to enter.")  # Output: You are allowed to enter.
else:
    print("You cannot enter.")


# 4. Using Comparison Operators in if-else
a = 15
b = 10

# Compare two values and print the larger one
if a > b:
    print(f"{a} is greater than {b}.")  # Output: 15 is greater than 10.
else:
    print(f"{b} is greater than {a}.")


# 5. Checking for Even or Odd Numbers
number = 7

# Determine if a number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")  # Output: 7 is odd.


# 6. Nested if-else Statements
score = 85

# Check the grade based on score using nested if-else
if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")  # Output: Grade: B
    else:
        print("Grade: C")


# 7. Using Ternary Operator (Conditional Expression)
x = 10
y = 20

# Short form of if-else
larger = x if x > y else y
print(f"The larger number is {larger}.")  # Output: The larger number is 20


# 8. Checking Multiple Conditions Using elif
weather = "sunny"

if weather == "rainy":
    print("Take an umbrella.")
elif weather == "sunny":
    print("Wear sunglasses.")  # Output: Wear sunglasses.
elif weather == "snowy":
    print("Wear a jacket.")
else:
    print("Enjoy the weather!")


# 9. if-else with Booleans
is_logged_in = False

# Check if a user is logged in or not
if is_logged_in:
    print("Welcome back, user!")
else:
    print("Please log in.")  # Output: Please log in.


"""
Key Takeaways:
- The if-else statement helps make decisions based on conditions.
- elif (else if) can be used to handle multiple conditions.
- Logical operators (and, or, not) allow combining conditions.
- Python supports a shorthand ternary operator for simple if-else conditions.
- Nested if-else allows for more complex decision-making.
- Booleans are often used in if-else to handle true/false conditions.
"""
