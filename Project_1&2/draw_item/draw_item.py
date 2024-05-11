import turtle
def draw_apple(t):    
    t.begin_fill()
    t.fillcolor('black')
    t.left(134)

    for i in range(30):
        t.forward(1)
        t.left(1)
        t.speed(25)

    t.right(5)

    for i in range(35):
        t.forward(1)
        t.left(1)
        t.speed(25)

    t.left(5)
    t.forward(30)

    for i in range(15):
        t.forward(0.7)
        t.right(3)
        t.speed(25)

    t.forward(25)
    t.left(5)

    for i in range(50):
        t.forward(1)
        t.left(1)
        t.speed(25)
    t.right(3)

    for i in range(50):
        t.forward(1)
        t.left(1)
        t.speed(25)

    t.right(5)

    for i in range(45):
        t.forward(2)
        t.left(1)

    t.right(5)

    for i in range(40):
        t.forward(2)
        t.left(1)

    t.left(5)

    for i in range(20):
        t.forward(1)
        t.left(2)

    t.left(5)
    t.forward(15)

    for i in range(9):
        t.forward(2)
        t.right(3)

    t.forward(1)

    for i in range(15):
        t.forward(1)
        t.right(1)

    t.right(4)
    t.forward(4.5)
    t.right(1)

    for i in range(27):
        t.forward(1)
        t.left(2)

    t.left(8)
    t.forward(5)

    for i in range(25):
        t.forward(2)
        t.left(1)

    t.right(3)
    t.forward(10)
    t.left(83)

    for i in range(75):
        t.forward(1.3)
        t.right(1)

    t.right(4)

    for i in range(24):
        t.forward(1.3)
        t.right(1)

    t.forward(9.66)
    t.end_fill()
    t.penup()
    t.left(132)
    t.forward(100)
    t.right(96)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')

    for i in range(60):
        t.forward(0.8)
        t.right(1)

    t.right(120)

    for i in range(60):
        t.forward(0.8)
        t.right(1)

    t.hideturtle()
    t.end_fill()

    turtle.done()

def draw_banana(t):
    x, y = 20, 30

    def get_position(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    t.color("yellow")
    t.begin_fill()
    t.fillcolor("yellow")
    t.left(180)
    t.circle(20,60)
    t.left(55)
    t.fd(40)
    t.right(80)
    t.circle(20,60)
    t.right(10)
    t.circle(130,180)
    t.circle(15,90)
    t.left(40)
    t.circle(-150, 85)
    t.circle(20,60)
    t.left(-90)
    t.fd(22)
    t.circle(20,70)
    t.end_fill()
    t.pencolor("black")
    t.pensize(3)
    get_position(91,51)
    t.end_fill()

    # Hide the turtle
    t.hideturtle()
    # Keep the window open
    turtle.done()

def draw_orange(t):
    # Set the color of the pen and the fill

    # Draw a circle for the orange
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Hide the turtle
    t.hideturtle()

    # Keep the window open
    turtle.done()

# Test the functions
screen = turtle.Screen()
screen.bgcolor('Gray')
t = turtle.Turtle()
t.speed(0)

# Draw objects
draw_apple(t)
draw_banana(t)
draw_orange(t)

# Keep the window open
turtle.done()
