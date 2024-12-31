#What are Logical operators?
# Logical operators are used to combine conditional statements and control the flow of your program. 
# They evaluate expressions and return True or False based on the logic they implement.

..........................................
#types of operators
#AND
#OR
#NOT

------------------------------------------------
Truth Tables(AND)
Operand 1	  Operand 2	   Result 
True	       True	     ->True
True	       False	   ->False
False	       True      ->False
False	       False	   ->False

Truth Tables(OR)
Operand 1	  Operand 2	   Result 
True	      True	      ->True
True	      False	      ->True
False	      True	      ->True
False	      False	      ->False

Truth Tables(NOT)
Operand	   Result 
True	    ->False
False	    ->True

...............................................
#HOW TO USE THE OPERATORS?

a = 3
b = 5

if a>1 and a<4:
  print("Something")


#the program above will print 'Something' as a result because the condition evaluated to true because condition 1 and condition both are true
#and as per truth table under AND: TRUE AND TRUE = TRUE, hence the conditionm is met "Something" is printed.
