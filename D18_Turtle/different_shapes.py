from turtle import Turtle, Screen
import random

cursor = Turtle()
ventana = Screen()

pasos = 75
for lados in range(3, 11):
    ang = 360/lados
    pasos += 0
    cursor.color(random.random(),random.random(),random.random())
    for _ in range(lados):
        cursor.fd(pasos)
        cursor.right(ang)

ventana.exitonclick()