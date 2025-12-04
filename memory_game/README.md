# 🎮 Memory Game (Turtle)

A simple and fun **memory challenge** built with Python's `turtle` module.  
Random shapes appear on the screen for a few seconds — your goal is to **remember how many shapes were drawn**!

---

## 🧠 How the Game Works

1. The game draws **5–20 random shapes** (circles, squares, triangles).  
2. You have **5 seconds** to look at the screen and remember the number.  
3. The screen clears.  
4. You are asked:  
   **"How many shapes did you count?"**  
5. If your answer is correct — you win!  
6. You can choose to play again.

---

## 🖼️ Features

- Random shapes  
- Random colors  
- Random positions  
- Adjustable display time  
- User-friendly pop‑up input windows  
- Infinite replay option  
- Cute success/failure messages ✨

---

## 🚀 How to Run

### Requirements
- **Python 3.x**
- Uses only built-in modules: `turtle`, `time`, `random`

### Run the game:
```bash
python memory_game.py
```

If your file is located inside a folder:
```bash
python memory_game/memory_game.py
```

---

## 📁 File Structure

```
memory_game/
│── memory_game.py
```

---

## 📌 Key Code Concepts

### 🎲 Random Shape Generator
The game randomly chooses one of three shapes:
```python
SHAPES = ["circle", "square", "triangle"]
```

### 🎨 Random Colors
```python
COLORS = ["red", "pink", "orange", "yellow", "purple", "cyan"]
```

### ⏳ Countdown Timer
Uses `time.sleep()` to show a real countdown in the console.

### 🐢 Turtle Objects
Each shape is drawn using a **new Turtle instance**, so old shapes remain visible until cleared.

---

## ❤️ Why This Project Is Useful

Perfect for:
- Kids learning Python  
- Memory training games  
- Turtle graphics lessons  
- Demonstrating randomness & user interaction  

The code is short, readable, and easy to expand with more shapes or difficulty levels.

---

## 📘 Enjoy the Game!
Feel free to modify shapes, colors, or time limit to create your own version!
