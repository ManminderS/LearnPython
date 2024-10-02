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
    print("These are the rules \n 1. Rock wins against scissors.\n 2. Scissors win against paper. \n 3.Paper wins against rock: ")
else:
    print("Lets Go!")

#Human Chose an input
human_choice = input("What do you choose? Rock, Paper or Scissors: ").lower()
if human_choice == "rock":
    print(task.rock)
    print("You chose rock")
elif human_choice == "paper":
    print(task.paper)
    print("You chose Paper")
elif human_choice == "scissors":
    print(task.scissors)
    print("You chose Scissors")
else:
    print("Invalid input")

#Computer's choice
comp_choose = random.choice(game_choices)
if comp_choose == "rock":
    print(task.rock)
    print("Computer chooses rock")
elif comp_choose == "scissors":
    print(task.scissors)
    print("Computer chooses Scissors")
else:
    print(task.paper)
    print("Computer chooses paper")

#Logic to play the game
if human_choice == "rock" and comp_choose == "Scissors":
    print("You Won!")
elif human_choice == "paper" and comp_choose == "rock":
    print("You Won!")
elif human_choice == "scissors" and comp_choose == "paper":
    print("You Won!")
elif human_choice == comp_choose:
    print("Its a tie")
else:
    print("You Lost!")

#Results
