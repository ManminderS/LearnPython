#Write a Python program that accepts 
#a list of numbers from the user, calculates the product of all even numbers in the list, and prints the result. 
#If there are no even numbers, display a message indicating so.

#make empty list to get user data
num_list = []

#make an empty list to append even numbers from user list
even_list = []

#accept input from user
add_num = input("Enter multiple whole integer separated by space")

#insert the input into a list called num
num = add_num.split()

#convert the list 'num' into list 'num_list' with integer values
num_list = [int(x) for x in num]

#Insert the even number in another list
for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
        
#Calculate the sum of this list with even numbers
total = sum(even_list)

#If list is empty, display message "No even number to add the number"
if len(even_list) == 0:
    print("No even number to add the number")
elif len(even_list) > 0:
    print(f"The sum of the even numbers in the list is: {total}")
