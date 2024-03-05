'''
Pseudo Code:
Create two lists, one to hold names and another to hold birthdates
Open the txt file to read line by line and with standard encoding to a file variable
    For each line, remove the white space and split it from the right three times to separate the birthdate from the name
    The name is the first part, and the birthdate is the last three parts joined
Print the names section
Print a separator for better readability
Print the birthdates section
'''

# Initialise lists to hold names and birthdates
names = []
birthdates = []

# Open the file and read line by line
with open('10-018 IO Operations - Input/Task file/DOB.txt', 'r', encoding='utf-8') as file:
    for line in file:

        # Strip the line to remove any leading/trailing whitespace
        # Then split it from the right three times to separate the birthdate from the name
        parts = line.strip().rsplit(' ', 3)
        if len(parts) == 4:

            # The name is the first part, and the birthdate is the last three parts joined
            name = parts[0]
            birthdate = ' '.join(parts[1:])
            names.append(name)
            birthdates.append(birthdate)

        else:
            print(f"Skipping invalid line: {line.strip()}")

# Print the names section
print("Name")
for name in names:
    print(name)

# Print a separator for better readability
print("\n")

# Print the birthdates section
print("Birthdate")
for birthdate in birthdates:
    print(birthdate)
