# Compilation Error: Missing quotes around string, should be "Hello, World!"
print(Hello, World!)

# Compilation Error: Missing colon at the end of the if statement
if x == 10
    print("x is 10")

# Runtime error: Division by zero
numerator = 10
denominator = 0
result = numerator / denominator  # Runtime Error: Zero Division Error due to division by zero

# Logical Error: Incorrectly checking for even number
number = 5
# Logical Error: Using assignment '=' instead of comparison '=='
is_even = number % 2 = 0  # Logical Error: This should be 'is_even = number % 2 == 0'
print(is_even)  # This will print an incorrect result if it were to run
