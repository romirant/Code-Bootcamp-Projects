# Pseudo Code
'''
Import the math library.
Ask the user to choose between 'bond' and 'investment' and store the choice in a variable called 'user_choice'.
If 'user_choice' is 'bond' (ignoring case):
    Ask the user for the present value of the house, the annual interest rate, and the bond term in months, and store these values in appropriate variables.
    Calculate the monthly interest rate by dividing the annual interest rate by 1200 (100 to convert percentage to decimal and 12 for months).
    Calculate the monthly repayment using the formula for bond repayment.
    Display the calculated monthly repayment, along with the input values, formatted appropriately.
Else if 'user_choice' is 'investment' (ignoring case):
    Ask the user for the deposit amount, the interest rate, and the investment term in years, and store these values in appropriate variables.
    Calculate the interest rate as a decimal by dividing the interest rate by 100.
    Ask the user to choose between 'simple' and 'compound' interest and store the choice in a variable called 'interest'.
    If 'interest' is 'simple' (ignoring case):
        Calculate the total investment amount using the formula for simple interest.
        Calculate the interest gained by subtracting the deposit amount from the total investment amount.
        Display the calculated total investment amount, the interest gained, and the input values, formatted appropriately.
    Else if 'interest' is 'compound' (ignoring case):
        Calculate the total investment amount using the formula for compound interest.
        Calculate the interest gained by subtracting the deposit amount from the total investment amount.
        Display the calculated total investment amount, the interest gained, and the input values, formatted appropriately.
    Else, display an error message.
Else, display an error message.
'''


# Imports math library
import math

# Requests the user make a choice between 'bond' and 'investment' and saves the value as a variable
user_choice = input("\n\ninvestment - to calculate the amount of interest you'll earn on your investment \
                    \nbond - to calculate the amount you'll have to pay on a home loan \
                    \n\nEnter either 'investment' or 'bond' from the menu above to proceed: ")

# The first condition that checks the 'user_choice' variable for the input of several correct versions of 'bond' from the user
if (user_choice == "bond") or (user_choice == "Bond") or (user_choice == "BOND"):

    # Prints an empty line
    print("")

    # These three inputs request the present house value, annual interest rate percentage
    # and bond told time in months and stores them respectively as integer variables
    present_value_house = float(input("What is the present value of your house?: £"))
    bond_annual_interest_rate_int = float(input("What is the annual interest rate percentage?: "))
    bond_time_months = int(input("Over how many months would you like repay this bond?: "))

    # Calculates the bond monthly interest rate and stores it as a variable
    bond_monthly_interest_rate_int = (bond_annual_interest_rate_int/1200)

    # Calculates the bond monthly repayment amount and stores it as a variable
    bond_monthly_repayment = (bond_monthly_interest_rate_int * present_value_house)/(1 - (1 + bond_monthly_interest_rate_int)**(-bond_time_months))

    # Prints an empty line
    print("")
    
    # Prints an fstring with the present house value, formated to include a ',' at the thousands place,
    # the bond annual interest rate, the bond term length in months, and the monthly bond repayment amount, rounded to 2 decimals
    print(f"With a present house value of £{present_value_house:,.2f}, a bond with an annual interest rate\
 of {bond_annual_interest_rate_int:.2f}% repayed over {bond_time_months} months\
 will have a £{bond_monthly_repayment:,.2f} monthly repayment")

# The second condition that checks the 'user_choice' variable for the input of several correct versions of 'investment' from the user
elif (user_choice == "investment") or (user_choice == "Investment") or (user_choice == "INVESTMENT"):
    
    # Prints an empty line
    print("")
    
    # These three inputs request the deposit amount, annual interest rate percentage
    # and investment length in months and stores them respectively as integer variables
    deposit_amount = float(input("How much will you deposit?: £"))
    investment_interest_rate_int = float(input("What is the interest rate percentage?: "))
    investment_time_years = int(input("How many years would you like to invest this amount?: "))
    
    # Calculates the interest rate as a decimal and stores it as a variable
    investment_interest_rate_pct = (investment_interest_rate_int/100)
    
    # Prints an empty line 
    print("")
    
    # Requests an input from the user to chose 'simple' or 'compound' and stores it as a variable
    interest = input("Would you like to calculate your investment by simple interest or compound interest? \
                    \n\nPlease enter either 'simple' or 'compound' to proceed: ")

    # The first condition that checks the 'interest' variable for the input of several correct versions of 'simple' from the user
    if (interest == "simple") or (interest == "Simple") or (interest == "SIMPLE"):
        
        # Prints an empty line
        print("")
        
        # Calculates the final total investment amount with the user's deposit, interest rate, and term length and stores it as a variable
        simple_interest_total = deposit_amount * (1 + investment_interest_rate_pct * investment_time_years)

        # Calculates the simple interest gained and stores it as a variable
        simple_interest_gain = simple_interest_total - deposit_amount
    
        # Prints a string that includes the initial deposit amount, interest rate, investment length, end total, and interest gain
        print(f"With an deposit of £{deposit_amount:,.2f} at {investment_interest_rate_int:.2f}% for {investment_time_years} years, \
you will have a total of £{simple_interest_total:,.2f}. \
\n\nWith simple interest this is a net gain of £{simple_interest_gain:,.2f}.")

    # The second condition that checks the 'interest' variable for the input of several correct versions of 'compound' from the user
    elif (interest == "compound") or (interest == "Compound") or (interest == "COMPOUND"):
        
        # Prints an empty line
        print("")
        
        # Calculates the final total investment amount with the user's deposit, interest rate, term length  and stores it as a variable
        compound_interest_total = deposit_amount * math.pow((1 + investment_interest_rate_pct),investment_time_years)

        # Calculates the compound interest gained and stores it as a variable
        compound_interest_gain = compound_interest_total - deposit_amount

        # Prints a string that includes the initial deposit amount, interest rate, investment length, end total, and interest gain
        print(f"With an deposit of £{deposit_amount:,.2f} at {investment_interest_rate_int:.2f}% for {investment_time_years} years, \
you will have a total of £{compound_interest_total:,.2f}. \
\n\nWith compound interest this is a net gain of £{compound_interest_gain:,.2f}.")
    
    # Closes the if-elif-else statement and prints a statement if the user inputs a string that is neither 'simple' or 'compound'
    else:
        print("Sorry, there was an issue with your selection.")

# Closes the if-elif-else statement and prints a statement if the user inputs a string that is neither 'bond' or 'investment'
else:
    print("Sorry, there was an issue with your selection.")
