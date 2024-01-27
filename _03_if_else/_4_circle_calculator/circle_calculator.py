# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
#Area = πr^2
#Circumference = 2πr
radius = int(input("input a radius for a circle: "))
choice = input("calculate the area or circumference: ")
if choice.lower() == "area":
    print(math.pi * (radius ** 2))
elif choice.lower() == "circumference":
    print(math.pi*2*radius)
else:
    print("invalid input")
