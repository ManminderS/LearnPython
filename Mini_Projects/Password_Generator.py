#import the important module
import random

#Welcome Screen
print("Welcome to Strong password generator")

#Different lists
letter = ['a', 'b', 'c','d','e', 'f','g','h','i','j','k']
number = ['0', '1', '2', '3','4','5','6','7','8','9']
symbol = ['!', '@', '#', '$','%','^','&','*','(',')','-']

#get the values for the variables
nr_letter = int(input("How many letters do you want"))
nr_num = int(input("How many numbers do you want"))
nr_symbol = int(input("How many symbol do you want"))

#Create an empty list called password, this will be used to store the random elements from the lists(letter, number and symbol)
password = []
pw = ""
#APPEND RANDOM ELEMENTS FROM THE LISTS ABOVE INTO A NEW LIST CALLED password
#random.sample(listname_from_where_to_get_the_element,user_input_from_nr_letter), as a result this randomly selects asked number of values from the given list
random_letter = random.sample(letter,nr_letter)

#randomly add element from list "number" to list random_number
random_number = random.sample(number,nr_num)

#randomly add element from list "symbol" to list random_symbol
random_symbol = random.sample(symbol,nr_symbol)

#Add the elements from random_letter, random_symbol, and random_symbol into list password
password.extend(random_letter)
password.extend(random_number)
password.extend(random_symbol)

#shuffle the elements in list "password"
random.shuffle(password)

#use the for loop to pick the element from list "password".
for item in password:
    #print each element next to each other without spacing
    pw += item
print(f"Your password is: {pw}")


----------------Alternative Solution--------------------------------

#import the important module
import random

#Welcome Screen
print("Welcome to Strong password generator")

#empty list to store the values
password = []
pw = ""

#Different lists
letter = ['a', 'b', 'c','d','e', 'f','g','h','i','j','k']
number = ['0', '1', '2', '3','4','5','6','7','8','9']
symbol = ['!', '@', '#', '$','%','^','&','*','(',')','-']

#get the values for the variables
nr_letter = int(input("How many letters do you want"))
nr_num = int(input("How many numbers do you want"))
nr_symbol = int(input("How many symbol do you want"))

for char in range(0, nr_letter):
    password.append(random.choice(letter))
    
for num in range(0,nr_num):
    password.append(random.choice(number))

for symb in range(0,nr_symbol):
    password.append(random.choice(symbol))

random.shuffle(password)

for element in password:
    pw += element
print(f"Your password is: {pw}")
