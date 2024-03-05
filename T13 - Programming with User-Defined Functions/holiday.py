'''
Pseudo Code:
Define a function hotel_cost(num_nights):
    Calculate the total hotel cost based on the number of nights
    Print the calculated cost
    Return the total hotel cost

Define a function plane_cost(city_flight):
    Create a dictionary to store the costs for different cities
    Get the flight cost based on the chosen city from the dictionary
    Print the flight cost
    Return the flight cost

Define a function car_rental(rental_days):
    Calculate the total car rental cost based on the number of days
    Print the calculated cost
    Return the total car rental cost

Define a function holiday_cost(hotel_cost, plane_cost, car_rental):
    Calculate the total holiday cost by summing up the hotel, flight, and car rental costs
    Print the total holiday cost
    Return the total holiday cost

Define a function flight_options():
    Display the city options
    Prompt the user to choose a city
    Validate the input and keep prompting until a valid city is chosen
    Return the chosen city

Define a function hotel_stay():
    Prompt the user to enter the number of hotel nights
    Validate the input and keep prompting until a valid number is entered
    Return the number of hotel nights

Define a function car_rental_days():
    Prompt the user to enter the number of car rental days
    Validate the input and keep prompting until a valid number is entered
    Return the number of car rental days

Main program starts here:

Display a welcome message

Start an infinite loop:
    Display the menu options
    Prompt the user to choose a calculation option

    Based on the user's choice, perform the corresponding calculation:
        If the user chooses 1:
            Call the hotel_stay() function to get the number of hotel nights
            Call the hotel_cost() function with the number of hotel nights and store the result
        If the user chooses 2:
            Call the flight_options() function to get the chosen city
            Call the plane_cost() function with the chosen city and store the result
        If the user chooses 3:
            Call the car_rental_days() function to get the number of car rental days
            Call the car_rental() function with the number of car rental days and store the result
        If the user chooses 4:
            Call the hotel_stay() function to get the number of hotel nights
            Call the flight_options() function to get the chosen city
            Call the car_rental_days() function to get the number of car rental days
            Call the hotel_cost(), plane_cost(), and car_rental() functions with the respective inputs and store the results
            Call the holiday_cost() function with the calculated costs and store the result

        If the user chooses an invalid option, display an error message
'''



def hotel_cost(num_nights):

    # Calculate the total hotel cost based on the number of nights and the price per night
    price_per_night = 60
    total_hotel_cost = num_nights * price_per_night
    print(f"\nYour hotel stay will cost £{total_hotel_cost} at £{price_per_night} per night.")
    return total_hotel_cost


def plane_cost(city_flight):

    # Define the costs for different cities using a dictionary
    city_costs = {
        "1": 200,  # Barcelona, Spain
        "2": 450,  # Rome, Italy
        "3": 500,  # Athens, Greece
        "4": 300   # Berlin, Germany
    }

    # Get the flight cost based on the chosen city
    flight_cost = city_costs.get(str(city_flight))
    print(f"\nYour flights will cost £{flight_cost}.")

    return flight_cost


def car_rental(rental_days):

    # Calculate the total car rental cost based on the number of days and the price per day
    price_per_day = 45
    total_rental_cost = rental_days * price_per_day
    print(f"\nYour car rental will cost £{total_rental_cost} at £{price_per_day} per day.")
    return total_rental_cost


def holiday_cost(hotel_cost, plane_cost, car_rental):

    # Calculate the total holiday cost by summing up the hotel, flight, and car rental costs
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    print(f"Your total holiday will cost £{total_holiday_cost}.")
    return total_holiday_cost


def flight_options():
    while True:

        # Display city options
        print('''\nCity Options:
                1. Barcelona, Spain
                2. Rome, Italy
                3. Athens, Greece
                4. Berlin, Germany''')

        # Prompt user for choice of city
        city = input("\nPlease choose the number for the city you will be flying to: ")

        # Try/Except statement to check if the user input is valid
        try:
            city = int(city)
            if (1 <= city <= 4):
                break
            else:
                print("\nPlease choose a number between 1 and 4.\n")
        except:
            print("\nPlease choose a valid number.\n")

    return city


def hotel_stay():
    while True:

        # Prompt the user for the number of nights to stay at a hotel
        hotel_nights = input("\nHow many nights will you be staying at a hotel: ")

        # Try/Except statement to check if the user input is valid
        try:
            hotel_nights = int(hotel_nights)
            if 1 <= int(hotel_nights):
                break
            else:
                print("\nPlease choose a valid number.\n")
        except:
            print("\nPlease choose a valid number.\n")

    return hotel_nights


def car_rental_days():
    while True:

        # Prompt the user for the number of days to rent a car
        num_rental_days = input("\nHow many days they you need to rent a car for: ")

        # Try/Except statement to check if the user input is valid
        try:
            num_rental_days = int(num_rental_days)
            if 0 <= int(num_rental_days):
                break
            else:
                print("\nPlease choose a valid number.\n")
        except:
            print("\nPlease choose a valid number.\n")

    return num_rental_days

# print the menu title
print("Welcome to your Holiday Calculator")

# Uses a While loop to create a menu loop
while True:

    # Prints the menu
    print("\nMenu:\n\n1. Hotel Costs\n2. Flight Costs\n3. Car Rental\n4. Entire Holiday Cost\n")

    # Get the user's choice for checking
    match input("Please choose the corresponding number for what you would like to caclulate: "):

        # 1. Calculates hotel costs
        case "1":
            hotel_cost(hotel_stay())

        # 2. Calculates flight costs
        case "2":
            plane_cost(flight_options())

        # 3. Calculates car rental costs
        case "3":
            car_rental(car_rental_days())

        # 4. Calculates the costs for an entire holiday
        case "4":
            holiday_cost(hotel_cost(hotel_stay()), plane_cost(flight_options()), car_rental(car_rental_days()))

        # A catch all for an invalid user choice
        case _:
            print("\nPlease make a valid choice\n")
