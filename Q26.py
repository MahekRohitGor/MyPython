# Write a python program to take two float values to add, subtract, multiply and 
# divide and print fractional representation.

from fractions import Fraction
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
print("Addition is {}".format(Fraction(a+b)))
print("Subtraction is {}".format(Fraction(a-b)))
print("Multiplication is {}".format(Fraction(a*b)))
print("Division is {}".format(Fraction(a/b)))
