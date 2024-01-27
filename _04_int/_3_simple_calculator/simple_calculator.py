"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import math
num1=float(input("Give me 1 number 1 operation then 1 more number(press enter after each input): "))
oper = input()
num2 = float(input())

if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "/":
    print(num1/num2)
elif oper == "*":
    print(num1*num2)
elif oper == "^":
    print(num1**num2)
else:
    print("incorrect operator")
