# Pseduo Code
# Define the variable "age" that requests the user's age as an integer
# Create if-elif-else statement structure based on several conditions in decending value
# Open the if-elif-else statement: if age is greater than 100 print out "Sorry, you're dead."
# Second condition: age is equal or greater than 65 print out "Enjoy your retirement!"
# Third condition: age is equal or greater than 40 print out "You're over the hill."
# Fourth condition: age equals exactly 21 print out "Congrats on your 21st!"
# Fifth condition: age is less than 13 print out "You qualify for the kiddie discount."
# Close the if-elif-else statement: for any other age print out "Age is but a number."


# Defines the variable "age" that requests the user's age as an integer
age = int(input("How old are you?: "))

# Opens the if-elif-else statement in decending value order: if age is greater than 100 prints out "Sorry, you're dead."
if (age > 100):
    print("Sorry, you're dead.")

# Defines the second condition: age is equal or greater than 65 prints out "Enjoy your retirement!"
elif (age >= 65):
    print("Enjoy your retirement!")

# Defines the third condition: age is equal or greater than 40 prints out "You're over the hill."
elif (age >= 40):
    print("You're over the hill.")

# Defines the fourth condition: age equals exactly 21 prints out "Congrats on your 21st!"
elif (age == 21):
    print("Congrats on your 21st!")

# Defines the fifth condition: age is less than 13 prints out "You qualify for the kiddie discount."
elif (age < 13):
    print("You qualify for the kiddie discount.")

# Closes the if-elif-else statement: for any other age prints out "Age is but a number."
else:
    print("Age is but a number.")