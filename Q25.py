# Write a program to create a simple calculator performing only 
# four basic operations.

value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))
op = input("Enter operation (+,-,/,*): ")

if op == "+":
    result = value1 + value2

elif op == "-":
    result = value1 - value2

elif op == "*":
    result = value1*value2

elif op == "/":
    if value2 == 0:
        result = print("Error! Division by zero is not allowed.")
    else:
        result = value1/value2

else: 
    result = print("Enter valid operation! Program is terminated...!")

print("Your Result is: " + str(result))
