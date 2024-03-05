#Pseudo Code
''' In a variable collect the swim time in minutes from the user as an integer
    In a variable collect the cycle time in minutes from the user as an integer
    In a variable collect the run time in minutes from the user as an integer
    Define a variable that sums the three variables into a total triathlon time
    Print the final triathlon completion time 
    Structure an if-elif-else statement 
    In decending value order the if statement will start with times over 111 mins
    If the time is over 111 mins it will print "Based on your completion time unfortunately you have not recieved an award"
    If the time is between 106 and 110 mins it will print "Based on your completion time you have recieved the Provincial Scroll award!"
    If the time is between 101 and 105 mins it will print "Based on your completion time you have recieved the Provincial Half Colours award!"
    If the time is under 100 mins it will print "Based on your completion time you have recieved the Provincial Colours award!"
'''


# These three variables collect, as integers, the final time in minutes of for the user's triathlon races
swim_time = int(input("What was your final swim time in minutes?: "))
cycle_time = int(input("What was your final cycle time in minutes?: "))
run_time = int(input("What was your final run time in minutes?: "))

# This sums up the variables for a single final triathlon time
total_time = swim_time + cycle_time + run_time

# This prints out the final triathlon time to the user using the f formating with the variable included in the string
print(f"You completed the triathlon in {total_time} minutes.")

# This starts the if-elif-else statement and will print out a response if the final time is 111 mins or over
if (total_time >= 111):
    print("Based on your completion time unfortunately you have not recieved an award")

# This will print out a response if the final time is between 106 and 110 mins
elif (total_time >= 106) and (total_time <= 110):
    print("Based on your completion time you have recieved the Provincial Scroll award!")

# This will print out a response if the time is between 101 and 105 mins
elif (total_time >= 101) and (total_time <= 105):
    print("Based on your completion time you have recieved the Provincial Half Colours award!")

# This closes the if-elif-else statement and will print out a response if the time is 100 or below
else:
    print("Based on your completion time you have recieved the Provincial Colours award!")