import turtle
shapeInput = input("Circle or Square?: ")
if shapeInput == "Circle" or shapeInput == "Square":
	
else:
	print("Sorry, I don't have this shape :(")
	
...
else:
    print("Sorry, I don't have this shape :(")
colorInput = input('What color will it be?, yellow, pink or black? :')
if colorInput == 'yellow' or colorInput == 'pink' or colorInput == 'black': 
	...
else:
	print("Sorry, I don't have this color :(")
	wn = turtle.Screen()
	wn.bgcolor("black")
	wn.title("Your shape")
displayShape = turtle.Turtle()
displayShape.shape(shapeInput)
displayShape.color(colorInput)
turtle.done()