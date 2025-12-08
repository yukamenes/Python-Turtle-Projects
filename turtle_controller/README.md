# 🐢 Turtle Controller

A simple and fun program that lets you **control a turtle using your keyboard**.  
Perfect for beginners learning real-time input handling and turtle graphics.

---

## 🎮 Controls

Use these keys to move the turtle:

| Key | Action |
|-----|--------|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Turn left |
| **D** | Turn right |
| **C** | Clear the screen and reset the turtle |

---

## 🚀 How to Run

### Requirements
- **Python 3.x**
- Uses only built-in modules: `turtle`

### Run the script:
```bash
python controller.py
```

If stored inside a folder:
```bash
python turtle_controller/controller.py
```

---

## 📂 File Structure

```
turtle_controller/
│── controller.py
```

---

## 🧠 How It Works

### 🎛️ Setting Up the Screen
A window is created with:
```python
screen = Screen()
screen.setup(width=800, height=600)
```

### 🐢 The Turtle
A turtle object is created:
```python
turtle = Turtle(shape="turtle")
turtle.speed(0)
```

### ⌨️ Keyboard Bindings
Each key is linked to a movement function:
```python
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
```

The screen listens for input:
```python
screen.listen()
```

### 🧹 Clearing the Screen
Press **C** to:
- Clear everything
- Move home
- Start drawing again

---

## 🌟 Why This Project Is Useful

Great for teaching:
- Event-based programming  
- Keyboard input handling  
- Movement and rotation math  
- Turtle graphics basics  

Perfect for kids and beginners learning Python!

---

## 🎉 Enjoy Controlling the Turtle!
Try modifying speed, movement distance, or adding new controls.
