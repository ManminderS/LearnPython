-------WIP-----
#import the important module
import random

#Different lists
letter = ['a', 'b', 'c','d','e', 'f','g','h','i','j','k']
number = ['0', '1', '2', '3','4','5','6','7','8','9','10','11','12','13']
symbol = ['!', '@', '#', '$','%','^','&','*','(',')','-']

#get the values for the variables
nr_letter = int(input("How many letters do you want"))
nr_num = int(input("How many numbers do you want"))
nr_symbol = int(input("How many symbol do you want"))

password = []

#APPEND RANDOM ELEMENTS FROM THE LISTS ABOVE INTO A NEW LIST CALLED password
#random.sample(list,number of elements to get) randomly selects asked number of values from the given list
random_letter = random.sample(letter,nr_letter)
random_number = random.sample(number,nr_num)
random_symbol = random.sample(symbol,nr_symbol)

#append these n random elements in the list password
password.extend(random_letter)
password.extend(random_number)
password.extend(random_symbol)

random.shuffle(password)

for item in password:
    print(item, end='')

