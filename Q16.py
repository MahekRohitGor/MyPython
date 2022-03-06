# Write a Python program to calculate the sum of three given numbers, if the values are equal
# then return three times of their sum.
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

if num1 == num2 == num3:
    print(3*num1)

else:
    print(num1+num2+num3)