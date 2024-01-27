import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    t = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring("Shape", "Which shape would you like circle, square or triangle").lower()
    # Draw the shape requested by the user using if-elif-else statements
    t.penup()
    t.right(180)
    if shape == "circle":
        t.forward(100)
        t.pendown()
        t.circle(radius=100)
    elif shape == "square":
        t.forward(50)
        t.pendown()
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif shape == "triangle":
        t.forward(50)
        t.pendown()
        t.left(30)
        for i in range(3):
            t.forward(100)
            t.left(120)
    else:
        messagebox.showerror("Shape Undefined", "The shape you have specified is either incorrectly spelled or is not one of the options available.")
    # Call the turtle .done() method
turtle.done()
