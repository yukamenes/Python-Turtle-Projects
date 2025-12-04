"""
Turtle Memory Game
------------------
A simple memory game where random shapes appear for 5 seconds.
You have to remember and count how many shapes were drawn.
"""

from turtle import Turtle, Screen
from random import choice, randint
import time

# Configuration
SHAPES = ["circle", "square", "triangle"]  # You can extend this list
COLORS = ["red", "pink", "orange", "yellow", "purple", "cyan"]
DISPLAY_TIME = 5  # seconds

screen = Screen()
screen.setup(width=600, height=500)
screen.title("Turtle Memory Game")


def draw_random_shape():
    """Draw a single random shape at a random position."""
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    t.up()
    t.goto(randint(-200, 200), randint(-180, 180))
    t.down()
    t.color(choice(COLORS))

    shape = choice(SHAPES)
    if shape == "circle":
        t.circle(randint(10, 40))
    elif shape == "square":
        side = randint(20, 60)
        for _ in range(4):
            t.forward(side)
            t.left(90)
    elif shape == "triangle":
        side = randint(30, 70)
        for _ in range(3):
            t.forward(side)
            t.left(120)


def play_game():
    """Main game loop."""
    screen.clear()
    num_shapes = randint(5, 20)
    
    for _ in range(num_shapes):
        draw_random_shape()

    screen.update()
    print(f"You have {DISPLAY_TIME} seconds to memorize the number of shapes!")
    
    for i in range(DISPLAY_TIME, 0, -1):
        print(i)
        time.sleep(1)

    screen.clear()
    
    user_guess = screen.textinput("Memory Test", 
                                  f"How many shapes did you count?")
    
    if user_guess and user_guess.isdigit() and int(user_guess) == num_shapes:
        screen.textinput("Correct!", "Amazing! You're right! (˶ᵔ ᵕ ᵔ˶)")
    else:
        screen.textinput("Wrong", f"Better luck next time! ♪(´▽｀) There were {num_shapes})")

    again = screen.textinput("Play Again?", "Do you want to play again? (yes/no)")
    if again and again.lower().startswith('y'):
        play_game()
    else:
        screen.bye()


# Start the game
play_game()
screen.mainloop()