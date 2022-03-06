# print even numbers in a given range
n1 = int(input("Please enter a number(lower limit): "))
n2 = int(input("Please Enter another number(upper limit): "))
print("Even numbers are: ")
for j in range(n1, n2 + 1):
    if j % 2 == 0:
        print(j)

