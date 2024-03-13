import turtle
import math
import random

# Bán kính elip
r = 100

t = turtle.Turtle()
t.speed(0)
# Vòng lặp vẽ elip xoay
while True:
    t.pencolor(random.choice(["red", "green", "blue"]))

    # Vẽ elip
    for i in range(2):
        for j in range(90):
            t.forward(2 * math.pi * r / 360)
            t.left(1)

        for j in range(90):
            t.forward(math.pi * r / 180)
            t.left(1)
    # Xoay hình elip
    t.right(10)

turtle.done()