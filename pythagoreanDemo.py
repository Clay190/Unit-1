#Clay Kynor
#9/1/17
#pythagoreanDemo -finding the hypotenuse of a right triangle

from math import sqrt

a = float(input("Enter leg 1: "))
b = float(input("Enter leg 2: "))
print("The hypotenuse is", sqrt(a**2 + b**2))