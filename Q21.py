# categorise a person as either child (<13), teenager (>=13 but <20)
#  or adult (>=20),based on age specified

age = int(input("Enter your age: "))
if(age>0 and age<13):
    print("You are a child !")
elif(age>=13 and age<20):
    print("You are teenager")
elif(age>=20):
    print("You are adult")