#Problem statement: 
#1. The program randomly selects a number between 1 and 100, 
#2. The user has to guess the number within a limited number of attempts.
#3. The program should provide hints if the guess is too high or too low.

#Guess the number chosen by the computer and ask user to guess it

#import important modules
import random

#Welcome Message
print("Welcome to Guessing Game")

#ask user if he wants to know the rule:
print("You have 5 tries to guess the number correctly")


#Computer randomly selects a number between 1 to 10
random_num = random.randint(1,101)
#print(random_num)

#Ask user to guess the number, atleast 5 tries
for n in range(1,6):
    print(f"Try {n}")
    user_guess = int(input("Guess the number: "))
    print(f" You selected {user_guess}")
    if user_guess > random_num:
        print("Oops! High")
    elif user_guess < random_num:
        print("Your guess is below the random number")
    else:
    # congratulate user if the guess was correct
        print("Hoot! Hoot! You guessed it right")

