# 🏁 Turtle Racing Game

A fun and colorful racing game built with Python’s `turtle` module.  
Place your bet on a turtle and watch the race unfold!

---

## 🎮 How the Game Works

1. The program asks you to **choose a turtle color** as your bet:
   - red, orange, yellow, green, blue, purple
2. Six turtles line up at the start.
3. The race begins — each turtle moves forward by a random amount.
4. The first turtle to reach the finish line wins.
5. You are told whether **your bet was correct**.

---

## 🐢 Features

- Six turtles with different colors  
- Randomized movement (every race is unique!)  
- Betting system  
- Interactive pop-up messages  
- Simple, beginner-friendly code  

---

## 🚀 How to Run

### Requirements
- **Python 3.x**
- Only uses built-in modules: `turtle` and `random`

### Run the game:
```bash
python turtle_race.py
```

If inside a folder:
```bash
python turtle_race/turtle_race.py
```

---

## 📂 File Structure

```
turtle_race/
│── turtle_race.py
```

---

## 🧠 How It Works

### 🎬 Setup
A window is created:
```python
screen.setup(width=600, height=400)
```

### 🎨 Turtle Creation
Each turtle:
- Gets a color  
- Gets positioned at a different height  
- Starts at x = -280  

### 🏎️ The Race Loop
Every iteration:
```python
turtle.forward(random.randint(0, 10))
```
The first turtle reaching `x > 270` wins.

### 🏆 Determining the Winner
The program checks:
```python
winner = turtle.pencolor()
```
Then displays a message showing:
- Which turtle won  
- Whether your bet matched the winner  

---

## 🌟 Why This Project Is Useful

Great for learning:
- Loops  
- Turtle movement  
- Randomization  
- User input  
- Event-driven graphics  

And it’s super fun for kids!

---

## 🎉 Enjoy the Race!
Customize colors, speeds, or add more turtles to make it even more exciting.
