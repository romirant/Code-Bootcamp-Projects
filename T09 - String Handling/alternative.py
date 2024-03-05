'''
Pseudo Code
1. Prompt the user to provide a string statement and store it in the variable 'string'
2. Initialise an empty string variable 'new_string' to store the result of alternating character cases
3. Loop through each character in 'string' with its index
   a. If the index is odd (using modulus 2), append the uppercase version of the character to 'new_string'
   b. If the index is even, append the lowercase version of the character to 'new_string'
4. Print the 'new_string' which now contains the original string with alternating character cases
5. Split 'string' into a list of words called 'string_list'
6. Loop through each word in 'string_list' with its index
   a. If the index is odd, convert the word at that index to uppercase and replace the original word in 'string_list'
   b. If the index is even, convert the word at that index to lowercase and replace the original word in 'string_list'
7. Join the words in 'string_list' into a single string with spaces in between and print it
'''

# Prompt the user to provide a string statement and store it in the variable 'string'
string = input("Please provide a string statement: ")

# Initialise an empty string variable 'new_string' to store the result of alternating character cases
new_string = ""

# Loop through each character in 'string' with its index
for i, letter in enumerate(string):

    # If the index is odd (using modulus 2), append the uppercase version of the character to 'new_string'
    if i % 2:
        new_string += string[i].upper()

    # If the index is even, append the lowercase version of the character to 'new_string'
    else:
        new_string += string[i].lower()

# Print the 'new_string' which now contains the original string with alternating character cases
print(new_string)

# Split 'string' into a list of words called 'string_list'
string_list = string.split()

# Loop through each word in 'string_list' with its index
for i, word in enumerate(string_list):

    # If the index is odd, convert the word at that index to uppercase and replace the original word in 'string_list'
    if i % 2:
        string_list[i] = string_list[i].upper()

    # If the index is even, convert the word at that index to lowercase and replace the original word in 'string_list'
    else:
        string_list[i] = string_list[i].lower()

# Join the words in 'string_list' into a single string with spaces in between and print it
print(" ".join(string_list))
