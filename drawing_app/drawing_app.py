"""
Simple Turtle Drawing App
-------------------------
Menu-based drawing tool with multiple shapes and text input.

"""

from turtle import Turtle, Screen
from random import choice

COLORS = ["pink", "red", "green", "blue", "orange", "purple", "cyan"]

t = Turtle()
t.speed(5)
screen = Screen()
screen.title("Turtle Drawing App")


def random_color():
    t.pencolor(choice(COLORS))


def square():
    random_color()
    for _ in range(4):
        t.forward(60)
        t.left(90)


def circle():
    random_color()
    t.circle(50)


def triangle():
    random_color()
    for _ in range(3):
        t.forward(80)
        t.left(120)


def rectangle():
    random_color()
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)


def write_text():
    text = screen.textinput("Text Input", "Enter your text:")
    if text:
        random_color()
        t.write(text, font=("Arial", 18, "italic"))
        t.penup()
        t.forward(150)
        t.pendown()


def main_loop():
    while True:
        choice = screen.textinput("Drawing Menu",
                                  "Choose an action:\n\n"
                                  "1. Square\n"
                                  "2. Circle\n"
                                  "3. Text\n"
                                  "4. Triangle\n"
                                  "5. Rectangle\n"
                                  "\nType 'quit' to exit")

        if choice in ["quit", "exit", "stop"]:
            break
        elif choice in ["1", "square"]:
            square()
        elif choice in ["2", "circle"]:
            circle()
        elif choice in ["3", "text"]:
            write_text()
        elif choice in ["4", "triangle"]:
            triangle()
        elif choice in ["5", "rectangle"]:
            rectangle()

    screen.bye()


main_loop()
screen.mainloop()