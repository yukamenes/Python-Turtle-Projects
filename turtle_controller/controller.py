"""
Turtle Controller
-----------------
Control a turtle with keyboard:
W - forward, S - back, A - left, D - right, C - clear
"""

from turtle import Turtle, Screen

def main():
    """Initialize turtle and set up controls."""
    screen = Screen()
    screen.title("Turtle Controller")
    screen.setup(width=800, height=600)

    turtle = Turtle(shape="turtle")
    turtle.speed(0)

    def forward():
        turtle.forward(15)

    def backward():
        turtle.backward(15)

    def left_turn():
        turtle.left(10)

    def right_turn():
        turtle.right(10)

    def clear_screen():
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    # Key bindings
    screen.onkeypress(forward, "w")
    screen.onkeypress(backward, "s")
    screen.onkeypress(left_turn, "a")
    screen.onkeypress(right_turn, "d")
    screen.onkeypress(clear_screen, "c")

    screen.listen()
    screen.exitonclick()



main()