#import random module
import random

#create list friends and add elements
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#logic to choose random person from the list 'friends'
# payee = random.choice(friends)

# #display a random element from the list friends
# print(f"{payee} is selected randomly to pay the bill")

# or Method 2 of doing the program
x = random.randint(0, len(friends) - 1)
print(friends[x])
