#Importing datetime modeule from datetime library/module for date and time.
from datetime import datetime

#Storing the current date in current_date variable and printing it for reference.
current_date=datetime.now().date()

#Welcome screen for the user and taking input from the user for the flight date.
print("____________Welcome to the flight calculator_________\n")
flight_date_input=input("What date are you flying in the format(YYYY-MM-DD): ")

#Convert the input string to a date object
flight_date=datetime.strptime(flight_date_input, "%Y-%m-%d").date()

#Calculating the number of days remaining in the flight.
days_remaining= (flight_date - current_date).days

# #Displaying results to the user on how many days are remaining in the flight.
print("Total days remaining in your flight: " + str(days_remaining) + " days")
