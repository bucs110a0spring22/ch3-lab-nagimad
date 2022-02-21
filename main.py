import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
n = random.randrange(1, 10)
print(n)
leonardo.forward(77)
michelangelo.forward(90)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
#equilateral triangle
for i in range(3):
  michelangelo.down()
  michelangelo.forward(120)
  michelangelo.left(120)
  
#square
michelangelo.clear()
for i in range(4):
  michelangelo.left(90)
  michelangelo.forward(90)
  
#hexagon
michelangelo.clear() 
for i in range (6):
  michelangelo.forward(30)
  michelangelo.right(300)

#nonagon
michelangelo.clear()
for i in range(9):
  michelangelo.forward(40)
  michelangelo.left(40)

#dodecagon
michelangelo.clear()
for i in range(12):
  michelangelo.forward(40)
  michelangelo.left(30)
  
window.exitonclick()
