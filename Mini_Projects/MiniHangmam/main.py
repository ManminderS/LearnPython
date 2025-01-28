#importing modules
import random

#wordlists
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")
chosen_word_list = list(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please enter a letter to guess: ").lower()


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
for char in chosen_word_list:
    if char == guess:
        print("right")
    else:
        print("wrong")
