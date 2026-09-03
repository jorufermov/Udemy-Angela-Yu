from turtle import Turtle, Screen

cursor = Turtle()

screen = Screen()

for i in range(4):
    cursor.forward(100)
    cursor.right(90)

screen.exitonclick()