#Pseudocode
#repeat the following 36 times:
     #repeat the following 6 times:
           #move 100 steps forward
           #turn 60 degrees to the left
      #turn 10 degrees to the right

#import module
import turtle

#create turtle and assign it to variable
frank_turtle = turtle.Turtle()

#generate a geometric pattern
#implement for loop
for x in range(36):
    #repeat the following 6 times
    for n in range(6):
        frank_turtle.forward(100)
        frank_turtle.left(60)
    #add a turn to the right
    frank_turtle.right(10)




