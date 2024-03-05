'''
Pseudo Code:
Begin an indefinite while loop to prompt the user for the number of students registering.
    Prompt the user to enter the number of students that are registering.
    Check if the user input is a valid integer using the .isdigit() method.
        If .isdigit() returns True, cast user_input to an integer and assign it to number_students.
            If number_students is greater than 0, exit the loop.
            Otherwise, prompt the user to enter a positive integer.
        If .isdigit() returns False, prompt the user to enter only a numerical value.
Create and open the file reg_form.txt for writing.
Give the .txt file a title
    Begin a for loop that iterates for the number of students.
        Prompt the user to enter the current student's ID number.
        Write the student's ID number to reg_form.txt, followed by a space, a dotted line for signatures, and a newline character.
Close the file after writing is complete.
Print a new line for clarity
Open the file reg_form.txt for reading.
    Read the entire contents of the file into the variable contents.
    Print the contents of the file to display the student ID numbers and signature lines.
'''


# Begin an indefinite while loop to prompt the user for the number of students registering.
while True:

    # Prompt the user to enter the number of students that are registering.
    user_input = input("Enter the number of students that are registering: ")

    # Check if the user input is a valid integer using the .isdigit() method.
    if user_input.isdigit():

        # If .isdigit() returns True, cast user_input to an integer and assign it to number_students.
        number_students = int(user_input)

        # If number_students is greater than 0, exit the loop.
        if number_students > 0:
            break

        # Otherwise, prompt the user to enter a positive integer.
        else:
            print("Please enter a positive number\n")

    # If .isdigit() returns False, prompt the user to enter only a numerical value.
    else:
        print("Please enter only a numerical value\n")


# Create and open the file reg_form.txt for writing. Then close the file after writing is complete.
with open('Software Engineering (Fundamentals)/T15 - IO Operations - Output/Submitted Work/reg_form.txt', 'w') as file:

    # Giving the file a title
    file.write("Student Sign-in Sheet\n\n")

    # Begin a for loop that iterates for the number of students.
    for student in range(number_students):

        # Prompt the user to enter the current student's ID number.
        id_number = input(f"Please enter student {student + 1}'s ID number: ")

        # Write the student's ID number to reg_form.txt, followed by a space, a dotted line for signatures, and a newline character.
        file.write(id_number + ' ' + '.'*80 + "\n")

# Print a new line for clarity
print("\n")

# Open the file reg_form.txt for reading.
with open('Software Engineering (Fundamentals)/T15 - IO Operations - Output/Submitted Work/reg_form.txt', 'r') as file:

    # Read the entire contents of the file into the variable contents.
    contents = file.read()

    # Print the contents of the file to display the student ID numbers and signature lines.
    print(contents)
