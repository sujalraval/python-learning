# 1. Counting Upwards
# Example: Count from 1 to 10

count_up = 1

print("Counting Upwards:")
while count_up <= 10:
    print(count_up)  # Output: 1, 2, 3, ..., 10
    count_up += 1  # Increment the counter by 1

# 2. Counting Downwards
# Example: Count down from 10 to 1

count_down = 10

print("\nCounting Downwards:")
while count_down >= 1:
    print(count_down)  # Output: 10, 9, 8, ..., 1
    count_down -= 1  # Decrement the counter by 1

# 3. Counting Even Numbers
# Example: Count even numbers from 2 to 20

even_count = 2

print("\nCounting Even Numbers:")
while even_count <= 20:
    print(even_count)  # Output: 2, 4, 6, ..., 20
    even_count += 2  # Increment the counter by 2

# 4. Counting Odd Numbers
# Example: Count odd numbers from 1 to 19

odd_count = 1

print("\nCounting Odd Numbers:")
while odd_count < 20:
    print(odd_count)  # Output: 1, 3, 5, ..., 19
    odd_count += 2  # Increment the counter by 2

# 5. Counting with a Step
# Example: Count from 0 to 100 with a step of 10

step_count = 0

print("\nCounting with a Step of 10:")
while step_count <= 100:
    print(step_count)  # Output: 0, 10, 20, ..., 100
    step_count += 10  # Increment the counter by 10

"""
Key Takeaways:
- A while loop can be used to count upwards or downwards based on a defined condition.
- You can modify the counting behavior by changing the increment or decrement values.
- This demonstrates the flexibility of while loops for iterative processes.
"""
