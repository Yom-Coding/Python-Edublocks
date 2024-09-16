from turtle import *
screen = Screen()
turtle = Turtle()
colour = input("What do you want your stair's colour to be?")
turtle.color(colour)
steps = int(input('Enter the Number of Steps: '))
for i in range(steps):
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(30)