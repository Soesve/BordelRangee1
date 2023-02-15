# import package and making object
import turtle 
  
  
pen = turtle.Turtle()
  
# method to draw square with dots
# space --> distance between dots
# x     --> side of square
def draw(space,x):
  for i in range(x):
    for j in range(x):
        
        # dot
        pen.dot()
          
        # distance for another dot
        pen.forward(space)
    pen.backward(space*x)
      
    # direction
    pen.right(90)
    pen.forward(space)
    pen.left(90)
  
# Main Section
pen.penup()
draw(10,8)
  
# hide the turtle
pen.hideturtle()