#Lists are the data structures and multiple values can be stored in a list
#for example, let's create list called fruits with 5 elements
fruits = ["Mango", "Papaya", "Kiwi", "Orange", "Banana" ]

#In Python, lists are zero-indexed, meaning the first element is at index 0. The offset is essentially the index you use to reference elements in the list.
#An offset is commonly used to access or manipulate data at a certain distance from the beginning (or any reference point) of the structure. 
#For example, an offset of 5 means accessing or operating on the element 5 positions away from the starting point.

#print the first element from the list
print(fruits[0]) #answer: Mango

#print the second element from the list
print(fruits[1]) #answer: Papaya

#print the last element from the list
print(fruits[-1]) #answer: Banana

#print the second last element from the list and so on
print(fruits[-2]) #answer: Orange

#To calculate the length(total values in a list) we can use len function
len(fruits) #answer will be 5

# The previous line of code gives you the length of the list, but if you try to print out the last element of the list using the below code thinking that the 
# The last element sits in the last place which is 5 and writes the code below:
print(fruits[5]) #this will result in an IndexError: List index out of range
#to set the offset correct from the index 0 when we have 5 elements in the list we can also do:
print(fruits[5-1]) #answer: Banana

#Appending Items to the list: Adding items to the lists
#General syntax
listname.append[item] #this will add the item to the end of the list 
fruits.append["Cherry"] #As a result Now list fruits looks like fruit = ["Mango", "Papaya", "Kiwi", "Orange", "Banana", "Cherry"]

#appending an extended list of
fruits.extend(["Watermelon", "Pear"]) 

#print the entire list after the last code
print(fruits) #As a result Now:  ["Mango", "Papaya", "Kiwi", "Orange", "Banana", "Cherry", "Watermelon", "Pear"]


    
