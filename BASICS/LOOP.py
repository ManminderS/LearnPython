#WHat is a loop? : In general it means things that have to happen over and over again or something we want to happen over and over again based on the condition. Also Loop is a way of repeating an action until a given condition is met

#1. For Loop: 
#Syntax: 
for item in list_of_items:
  Do Something

#for example lets create a list of fruits and using for loop, to print each element of the list.

#create a list called fruits
fruits = ["Apple", "Banana", "Grapes", "Mango"]

#adding loop to print each element of the list "fruits", unless every element is printed
for fruit in fruits:
  print(fruit)   

#RESULT: 
#Apple
#Banana
#Grapes
#Mango
-------------------------------------------------------------------------------------------------------------------
#Indentation is important, anything after for loop statement is part of for loop
for fruit in fruits:
  print(fruit)  #part of for loop
print(fruit)   #not a part of the loop as there is no indentation in front of it.


--------------------------------------------------------------------------------------------------------------------
#example 2: consider a list of scores
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#first way of printing the total of scores in the student_scores
sum = sum(student_scores)
print(sum) #RESULT: 2068

#Getting the same result with for-loop
sum = 0
for score in student_scores:
    sum += score
print(sum) #RESULT: 2068

----------------------------------------------------------------------------------------------------------------------
#scenario
#find out the biggest number from the following list
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#declaring variable to record the max number from the list
max_num = 0

#for loop
for score in student_scores:
    if score > max_num:
        max_num = score
print(max_num)


---------------------------------------------------------------------------------------------------------------------------
#LEARNING 2: Using range function with For-Loop
#Syntax : for i in range(a,b)    #i: particular elements #a: starting range and b: ending range, a =< num < b

#example: dislay 1-10 numbers on screen
#Solution:
for num in range(1,11):
  print(num)

#Result: 
1
2
3
4
5
6
7
8
9
10


-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Coding Exercise: Print 1-100 on screen, any number divisible by 3 should print "FIZZ", any number divisible by 5 should print "BUZZ", and number divisible by both 3 and 5 should print as "BuzzFizz"
#using for loop with range function to define the range as 1-100
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FIZZBUZZ"
    elif num % 5 == 0:
        num = "BUZZ"
    elif num % 3 == 0:
        num = "FIZZ"
    print(num)

---or--- Alternative Solution to print fizz buzz-------------------------------
# Create a loop with For and Range to go from 1 to 100.
for number in range(1, 101):
  # First check if the number is divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 
  # Then check if the number is only divisible by 3
  elif number % 3 == 0:
    print("Fizz")
 
  # Finally check if the number is only divisible by 5
  elif number % 5 == 0:
    print("Buzz")
 
  # If it's not divisible by either of those numbers, just print the number
  else:
    print(number)

#Result:-----------------------------
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
