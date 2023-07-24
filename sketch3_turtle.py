import turtle

turtle.bgcolor("black")
turtle.title("Beautiful Pattern")
# turtle.pencolor("white")

turtle.speed(0)
turtle.pensize(2)

def drawpattern(radius):
    for i in range(20):
        turtle.colormode(255)
        # turtle.pencolor(10*i,5*i,2*i)
        turtle.pencolor(12 * i+10, 6 * i+20, 3 * i)
        turtle.circle(radius)
        radius -= 4

def design():
    for i in range(10):
        drawpattern(120)
        turtle.left(60)

design()
turtle.hideturtle()
turtle.done()
