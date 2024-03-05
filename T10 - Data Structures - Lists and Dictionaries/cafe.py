'''
Pseudo Code:
Define a list labelled 'menu' of items sold in the cafe
Define a dictionary lebelled 'stock' containing the stock value for each item
Define a dictionary lebelled 'price' containing the prices for each item
Calculate the total stock worth in the cafe
Print out the result of the calculation
'''

# List of items sold in the cafe
menu = ["latte", "espresso", "sandwich", "croissant"]

# Dictionary containing the stock value for each item
stock = {
    "latte": 12,
    "espresso": 15,
    "sandwich": 7,
    "croissant": 5
    }

# Dictionary containing the prices for each item
price = {
    "latte": 3.50,
    "espresso": 2,
    "sandwich": 5.50,
    "croissant": 3
    }

# Calculate the total stock worth in the cafe
total_stock_worth = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value


# Print out the result of the calculation
print(f"The total stock worth of the cafe is: £{total_stock_worth:.2f}")
