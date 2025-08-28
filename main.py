import turtle

# Screen setup
window = turtle.Screen()
window.title("movement thing")
window.bgcolor("black")
window.setup(width=500, height=500)

# Window lock
root = window.getcanvas().winfo_toplevel()
root.resizable(False, False)

# MAIN PLAYER
player = turtle.Turtle()
player.penup()
player.color("red")
player.shape("circle")
player.goto(0, 0)

# Define Functions
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Movement Keys
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

turtle.done()