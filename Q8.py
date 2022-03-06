# Write a Python program to accept a filename from the user and print the extension of that.
file_name = str(input("Enter filename: "))
extension = file_name.split(".")
print(extension[1])