from tkinter import messagebox, simpledialog
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askinteger("What color tomato?", "Pick from one of these three colors, enter 1 for red 2 for green and 3 for yellow")
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color == 1:
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
elif color == 2:
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
elif color == 3:
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")

root.mainloop()
