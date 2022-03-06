# Write a Python program to display the examination schedule.
# date_of_exam = str(input("Enter Date of exam in dd,mm,yyyy(should be separated by commas):"))
# x = date_of_exam.split(",")
# print("Date of examination is "+x[0]+"/"+x[1]+"/"+x[2])
# Or
day = int(input("Enter day of exam: "))
month = int(input("Enter month of exam: "))
year = int(input("Enter year of exam: "))
date_of_exam = (day, month, year)
print("Date of exam is : %i/%i/%i"%date_of_exam)
