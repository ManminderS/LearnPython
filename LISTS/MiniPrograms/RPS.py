#import modules
import task
import random

#List of choices
game_choices = ["rock", "paper", "scissors"]

#Welcome Screen
print("Welcome to Rock Paper Scissors Game")

#Rules
rules = input("Do you want to learn about rules? 'yes' or 'no': ").lower()
if rules == "yes":
    print("These are the rules \n 1. Rock wins against scissors.\n 2. Scissors win against paper. \n 3.Paper wins against rock.")
else:
    print("Lets Go!")

#Human Chooses an input
human_choice = int(input("What do you choose? 0 for Rock, 1 for Paper and 2 for Scissors:"))
if human_choice == 0:
    print(task.rock)
elif human_choice == 1:
    print(task.scissors)
else:
    print(task.paper)


#Computer's choice
comp_choose = random.choice(game_choices)
print(comp_choose)
if comp_choose == "rock":
    print(task.rock)
    print("Computer chooses rock")
else:
    print(task.paper)
    print("Computer chooses paper")




#Logic to play the game


#Results


#test
