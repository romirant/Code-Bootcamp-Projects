# Defining variables for car price and discount
car_price = 100
discount = 10

# Intended to apply discount and then add tax (suppose tax rate is 10%)
final_price = car_price - discount + 0.10

print(f"£{final_price}")  # Logical Error: Expected 99 but will return 90.10