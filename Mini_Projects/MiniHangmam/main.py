----------------This is fixed version--------------------------------

#importing modules
import random

#wordlists
word_list = ["batman", "Superman", "Avengers", "Hulk", "Transformers"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
length = len(chosen_word)

#Make placeholders for the chosen word
#create a empty list "spaces" & Insert the _ that is equal to lenght of the chosen word
spaces = []
for element in range(length):
    spaces.append("_")


#join the elements of the list and display it
the_word = " ".join(spaces)
print(the_word)

#Ask user to guess the letter:
guess = input("Guess the letter: ")


#join the elements of the list and display it
the_word = " ".join(spaces)
print(the_word)

#when user choose a word, if it matches any alphabet in the word, replace it with the guessed word
if guess in chosen_word:
    print("R")
else:
    print("W")


-----------------------------------------this is previous code----------------------------------------------------------------------
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



--------------------------this is what i just did on Jan 30, 2025--------------------
#wordlists
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}")
length = len(chosen_word)

#make spaces = length of chosen word into a string
spaces = []

for element in range(length):
    spaces.append("_")
print(spaces)

#make place holders
# placeholder = list(chosen_word)
# print(placeholder)

#print the elements in the list
the_word = " ".join(spaces)
print(the_word)
