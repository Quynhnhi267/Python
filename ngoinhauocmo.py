import turtle
t = turtle.Turtle()
# nhấc ngòi
t.penup()
t.goto(-100,-100)
t.pendown()
 #vẽ hình vuông
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)
# vẽ mái
t.right(45)
t.forward(140)
t.right(90)
t.forward(140)
# vẽ mặt trời
t.penup()
t.goto(200,200)
t.pendown()
t.circle(50)
# vẽ tia mặt trời 
t.penup()
t.goto(190,190)
t.pendown()
t.right(90)
t.forward(50)

t.penup()
t.goto(170,225)
t.pendown()
t.right(45)
t.forward(50)

t.penup()
t.goto(175,265)
t.pendown()
t.right(45)
t.forward(50)

t.penup()
t.goto(175,265)
t.pendown()
t.right(45)
t.forward(50)

t.penup()
t.goto(175,265)
t.pendown()
t.right(45)
t.forward(50)
#vẽ cây
t.penup()
t.goto(-250,-100)
t.pendown()
t.right(45)
t.forward(40)
t.right(90)
t.forward(200)
t.right(90)
t.forward(40)
t.right(90)
t.forward(200)
#vẽ lá cây
t.left(90)
t.forward(80)
t.right(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(45)
t.forward(80)



turtle.done()