# 🖌️ Turtle Drawing App

A simple **menu-based drawing application** built with Python’s `turtle` module.  
You can draw multiple shapes — squares, circles, triangles, rectangles — or write custom text directly on the screen.

---

## 🎨 Features

- Draw different shapes:
  - Square
  - Circle
  - Triangle
  - Rectangle
- Enter and draw **custom text**
- Random colors for each drawing
- Interactive menu using pop-up dialogs
- Continuous loop until user types **quit**

---

## 🚀 How to Run

### Requirements
- **Python 3.x**
- No external libraries required — only `turtle` and `random`

### Run the app:
```bash
python drawing_app.py
```

If stored in a folder:
```bash
python drawing_app/drawing_app.py
```

---

## 📂 File Structure

```
drawing_app/
│── drawing_app.py
```

---

## 📘 How It Works

### 🎨 Random Color
Each shape uses a randomly chosen color:
```python
COLORS = ["pink", "red", "green", "blue", "orange", "purple", "cyan"]
```

### 🧱 Shapes
Each shape has its own function:
- `square()`
- `circle()`
- `triangle()`
- `rectangle()`

All shapes:
- Pick a random color  
- Draw using turtle movement commands

### ✍️ Writing Text
The user can enter text using:
```python
screen.textinput("Text Input", "Enter your text:")
```
The turtle then writes the text and moves forward to avoid overlap.

### 🔁 Main Loop
The menu repeats until the user types:
```
quit / exit / stop
```

---

## 🧩 Example Menu

When the app runs, a window pops up:

```
Choose an action:

1. Square
2. Circle
3. Text
4. Triangle
5. Rectangle

Type 'quit' to exit
```

---

## 🌟 Why This Project Is Great

Perfect for teaching:
- Turtle graphics basics  
- Functions and code organization  
- User interaction and input windows  
- Randomization  
- Simple menu-driven programs  

And fun for kids learning programming!

---

## 🎉 Enjoy Drawing!
Feel free to modify colors, sizes, or add new shapes!
