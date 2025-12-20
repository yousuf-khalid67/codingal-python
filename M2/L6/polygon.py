import turtle    #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,350)
polygon = turtle.Turtle() #defined variable
 
num_sides = 7 #variable
side_length = 60
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
     
turtle.done()

