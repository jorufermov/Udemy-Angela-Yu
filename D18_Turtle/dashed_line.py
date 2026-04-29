from turtle import Turtle, Screen

cursor = Turtle()
window = Screen()

ancho = window.window_width()

cursor.color("white")
cursor.goto(-ancho/2,0.0)
for _ in range(50):
    cursor.color("black")
    cursor.fd(10)
    cursor.color("white")
    cursor.fd(10)
    
window.exitonclick()