# Write a Python program which accepts a sequence  from user and generate a list and a tuple with those numbers
values = input("Please enter number separated by commas: ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple: ', tuple)