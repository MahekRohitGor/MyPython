# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def copies(str1, num):
    result = ""
    for i in range(num) :
        result = result + " " + str1
    return result


x = str(input("Enter a string: "))
y = int(input("Enter how many times you want to copy string: "))

if y > 0:
    print(copies(x, y))
