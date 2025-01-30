#importing modules
import random

#wordlists
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")

#placeholder
placeholders = len(chosen_word)*"_ "
placeholders = [placeholders]
print(placeholders)
print(len(placeholders))


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please enter a letter to guess:").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("Wrong")
        
#put the the right guessed letter into the place holder
