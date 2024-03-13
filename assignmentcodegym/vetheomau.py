import turtle
import math
# Bán kính elip
r = 100

t = turtle.Turtle()
t.speed(0)
t.pencolor("black")

# Vòng lặp vẽ elip
for i in range(2):
    # Vẽ 1 nửa elip
    for j in range(90):
        t.forward(2 * math.pi * r / 360)
        t.left(1)

    # Vẽ 1 nửa elip với bán kính r/2
    for j in range(90):
        t.forward(math.pi * r / 180)
        t.left(1)

turtle.done()


