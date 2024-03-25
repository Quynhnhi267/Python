import turtle
import random

def create_rectangle(turtle, color, x, y, width, height):
  """Draws a rectangle on the screen."""
  # ... rest of the function remains the same ...
    
def create_circle(turtle, x, y, radius, color):
  """Draws a circle on the screen."""
  # ... rest of the function remains the same ...

BG_COLOR = "#80C0FF"
oogway = turtle.Turtle()

# set turtle speed
oogway.speed(2)
screen = oogway.getscreen()

# set background color
screen.bgcolor(BG_COLOR)

# set title of screen
screen.title("Merry Christmas")

# maximize the screen
screen.setup(width=1.0, height=1.0)

y = -100

# create tree trunk
create_rectangle(oogway, "red", 250, y-100, 30, 60)

# create tree
width = 240
oogway.speed(10)
while width > 10:
  width = width - 10
  height = 10
  x = 260 - width/2
  create_rectangle(oogway, "green", x, y-40, width, height)
  y = y + height

# create a star a top of tree
oogway.speed(1)
oogway.penup()
oogway.color('yellow')
oogway.goto(240, y-30)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
  oogway.forward(40)
  oogway.right(144)
oogway.end_fill()

tree_height = y + 40

# create moon in sky
# create a full circle
create_circle(oogway, 230, 180, 60, "white")
# overlap with full circle of BG color to make a crescent shape
create_circle(oogway, 220, 180, 60, BG_COLOR)

# now add few stars in sky
oogway.speed(10)
number_of_stars = random.randint(20,30)
# print(number_of_stars)
for _ in range(0,number_of_stars):
  x_star = random.randint(-(screen.window_width()//2),screen.window_width()//2)
  y_star = random.randint(tree_height, screen.window_height()//2)
  size = random.randint(5,20)
  oogway.penup()
  oogway.color('white')
  oogway.goto(x_star, y_star)
  oogway.begin_fill()
  oogway.pendown()
  for i in range(5):
    oogway.forward(size)
    oogway.right(144)
  oogway.end_fill()

# print greeting message
oogway.speed(1)
oogway.penup()
msg = "Merry Christmas Quynh Nhi"
oogway.goto(0, -200)  # y is in minus because tree trunk was below x axis
oogway.color("white")
oogway.pendown()
oogway.write(msg, move=False, align="center", font=("Arial", 15, "bold"))
oogway.hideturtle()
screen.mainloop()