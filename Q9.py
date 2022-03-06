# Write a Python program to display the first and last colors
# from the following list.
n = int(input("Enter how many colours you want to enter: "))
colour_list = str(input("Enter colours separated by commas: "))
list_colour = colour_list.split(",")
print(list_colour[0] + " and " + list_colour[n-1])