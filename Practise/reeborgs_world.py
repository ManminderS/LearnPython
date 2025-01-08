#Challenge Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

#Solution to Hurdle 1 : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for hurdles in range(6):
    jump_hurdle()

-------------------------------------------------------
#2. Solving the reeborg Hurdle 1 using the while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for hurdles in range(6):
 #   jump_hurdle()

no_of_hurdles = 6
while no_of_hurdles > 0:
    jump_hurdle()
    no_of_hurdles -= 1

--------------------------------------------------
#3. Solving reeborg Hurdle 2 using the while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#for hurdles in range(6):
 #   jump_hurdle()

while at_goal() != True:
    jump_hurdle()



-------------------------------------------------------------------
Hurdle 3: WIP

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    
while at_goal() == False:
     while wall_in_front() == True:
            jump()
            while front_is_clear() == True:
                move()
