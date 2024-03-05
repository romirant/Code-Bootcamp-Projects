# Pseudo Code
'''
1. Define the variable "stars" with a string value of '*'
2. Start a 'for' loop for "i" from 0 to 8 (inclusive)
3.   Check if "i" is less than or equal to 4
4.     If true, print the value of "stars" and then append '*' to "stars"
5.     If false, check if "i" is greater than or equal to 5
6.       If true, calculate "index" as 9 minus "i", then print the substring of "stars" from index 0 to "index"
7. End loop
'''

# This defines the variable as a string of '*'s
stars = '*'

# Sets for loop for the variable i to iterate in the range 0 to 9
for i in range(0,9):

    # Opens if statement for when i is less than or equal to 4 to print
    # the variable "stars" and add one additional '*' each iteration
    if i <= 4:
        print(stars)
        stars = stars + '*'

    # The second condition in the if statement for when i is greater than or equal to 5
    # it defines the variable "index" to slice and then print the variable "stars"
    elif i >= 5:
        index = 9-i
        print(stars[0:index])
