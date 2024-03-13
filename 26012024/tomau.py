import turtle
shapeInput = input('Circle and square, what is your favorite shape?:')
if shapeInput == 'circle' or shapeInput == 'square':
	colorInput = raw_input('What color will it be?, yellow, red or blue? :')
	if colorInput == 'yellow' or colorInput == 'red' or colorInput == 'blue': 
		wn = turtle.Screen()
		wn.bgcolor("black")
		wn.title("Your shape")
		
        displayShape = turtle.Turtle()
	
	
	
	
	
	displayShape = turtle.Turtle()
	displayShape.shape(shapeInput)
	displayShape.color(colorInput)
	
	turtle.done()
	
	print("Sorry, I don't have this shape :(")
	print("Sorry, I don't have this color :(")