"""
Turtle Racing Game
------------------
Bet on which colored turtle will win the race!
"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race")

user_bet = screen.textinput("Make your bet", 
                            "Which turtle will win? Choose a color:\n"
                            "red, orange, yellow, green, blue, purple")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_position = -100

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-280, y=y_position)
    turtles.append(t)
    y_position += 40

if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 270:
            race_on = False
            winner = turtle.pencolor()
            if winner.lower() == user_bet.lower():
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost. The {winner} turtle won!")
            screen.textinput("Race Over", 
                             f"The {winner} turtle won!\nYou bet on {user_bet}")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()