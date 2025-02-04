----------------This is fixed version--------------------------------
#import modules
import random

#wordlist
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for element in range(length):
    placeholder += '_'

#join the elements of the list and display it
# the_word = " ".join(spaces)
print(placeholder)
guess = input("Guess a letter: ").lower()



# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""

while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    
for element in chosen_word:
    if element == guess:
        display += element
    else:
        display += "_"
print(display)





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
