import turtle
t = turtle.Turtle()
# nhấc ngòi lên viết
t.penup()
t.goto(-200,-200)
t.pendown()
# vẽ hình vuông
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
# xoay con trỏ
t.right(45)
t.forward(70)
t.right(90)
t.forward(70)
# vẽ mặt trời 
t.penup()
t.goto(200,200)
t.pendown()
t.circle(50)

turtle.done()
