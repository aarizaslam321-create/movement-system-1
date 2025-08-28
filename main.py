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

# Forward movement
def move_forward():
    player.forward(5)
    window.ontimer(move_forward, 50)

# Keybinds
def move_up():
    player.setheading(90)

def move_down():
    player.setheading(270)

def move_left():
    player.setheading(180)
    
def move_right():
    player.setheading(0)

window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Borders
x, y = player.xcor(), player.ycor()
if x > 240: player.setx(240)
if x < -240: player.setx(-240)
if y > 240: player.sety(240)
if y < -240: player.sety(-240)

# Start the movement
move_forward()