"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
x = float(input("Enter a number"))
y = float(input("Enter another number"))
hyp = input( "Is x or a the hypotenuse of a right triangle?" )

if hyp == "yes":
    min(x,y)
    max(x,y)
    c = math.sqrt((x ** 2) - (y ** 2))
    c = round(c, 1)
    print(f"The missing side is {c}")
