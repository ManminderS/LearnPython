# Q 1: When to use the for loop and 
# When you have to iterate over something and with iteration you have to do something

# For example: for a list of fruits
fruits = [Apple, Orange, Guava]
#in order to do something with each iteration like priting the fruit we need to use the for loop, this cant be done easily using thw while loop.
for fruit in fruits:
  print(fruit)

# Q 2: When to use the while loop?
# use a while loop when you don't really care what number in a sequence you're in, which item you're iterating through in a list and you just simply want to carry out some sort of functionality many,
# many times until some sort of condition that you set. And this is also a good point to mention that while loops are a little bit more dangerous than for loops because in for loops, you're setting ahead of time
# how many times something is going to run. It's going to stop once it reaches the end of the list of items in this case, and it's going to stop once it reaches the upper bound of the range in this case. 

# But for while loops, they will continue running until this particular condition switches to false. So if you have some sort of condition that actually never becomes false, well
# then your while loop becomes something known as an infinite loop. Because let's say that our while loop tested while five is greater than three, then carry out these three lines of code. Well,
# five is always going to be larger than three until the end of time.

# And so that means your code is also going to run until the end of time, which is probably not what you want in most cases. If instead of saying, while not at_goal, I said, while five is greater than three,
# then you're going to see this robot perform this jump until eternity. And it's basically going to stop only once it's crashed and timed out.

# Now every single program at some point in their lives will create an infinite loop. Don't worry about it. Just quit the program, restart and try to prevent this from happening in the future.

# And very often I find that it's really helpful when you don't know why you're getting an infinite loop to simply just print out your condition. So in this case, if I printed out five greater than three,
# then it's always going to print true. And it's never going to become false basically. 

---------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------
#WHat is a loop? : In general it means things that have to happen over and over again or something we want to happen over and over again based on the condition. Also Loop is a way of repeating an action until a given condition is met
#loop type 1: 
for item in list_of_items:
do something to each item

loop type 2: for number in range(a,b):
  print(number)

loop type 3: While loop
while something_is_true:
  #do something repeatedly






-----------------------------------------------------------------------------------------------------------------------
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
