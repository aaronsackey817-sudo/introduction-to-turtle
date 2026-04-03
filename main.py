import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
pen=turtle.Turtle()
slides=3
angle=120
length=100
for i in range(slides):
    pen.forward(length)
    pen.left(angle)
turtle.done()