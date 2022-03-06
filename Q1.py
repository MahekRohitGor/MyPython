# print odd numbers in a given range
num1 = int(input("Please enter a number(lower limit): "))
num2 = int(input("Please Enter another number(upper limit): "))
print("Odd numbers are: ")
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        print(i)
