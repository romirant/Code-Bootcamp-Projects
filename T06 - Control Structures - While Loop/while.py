# Pseudo Code
'''
1. Define a variable 'user_number' and prompt the user to enter a number. Convert the input to a floating-point number.
2. Define a counter 'i' to 0. This will keep track of the number of inputs provided by the user.
3. Define a variable 'number_sum' to 0. This will hold the sum of all the numbers entered by the user.
4. Start a while loop that continues until 'user_number' is equal to -1.
    4.1. Increment 'i' by 1.
    4.2. Add 'user_number' to 'number_sum'.
    4.3. Print a message to the user indicating that they can enter -1 to end the program.
    4.4. Prompt the user to enter a new number and convert it to a floating-point number, storing the result in 'user_number'.
5. Once the loop ends, calculate the average of the numbers entered by the user by dividing 'number_sum' by 'i'.
6. Print the average, formatted to two decimal places.
'''

# Defining the variable, requesting the user's first number and formating it as a float
user_number = float(input("Please enter a number: "))

# This index variable defines the initial number of user submitted numbers at zero
i = 0

# This variable defines the initial sum of user submitted numbers at zero
number_sum = 0

# This while loop will run until the user inputs -1
# It will also add 1 to the index variable, sum the user submitted numbers, and request a new number input from the user
while user_number != -1:
    i += 1
    number_sum += user_number
    print("")
    print("If you wish to end the program please input -1")
    user_number = float(input("Please enter a new number: "))

# When the while loop breaks this variable will calculate the average of the user submitted numbers excluding -1
average = number_sum/i

# This prints a blank line
print("")

# This prints out the average formatted to two decimal places
print(f"The average of numbers submitted: {average:.2f}")
