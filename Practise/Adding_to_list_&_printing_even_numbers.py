#Work in Progress 

#Write a Python program that accepts #a list of numbers from the user, calculates the product of all even numbers in the list, and prints the result. 
#If there are no even numbers, display a message indicating so.

#make an empty list
num_list = []

#accept input from user
add_num = input("Enter multiple whole integer separated by space")

#insert the input into a list
num = add_num.split()

#convert the list to integer values
num_list = [int(x) for x in num]


total = sum(num_list)
print(total)
print(num_list)

#Insert the even number in another list

#Calculate the sum of this list with even numbers

#If list is empty, display message "No even number to add the number"
