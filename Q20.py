# Write a Python program to count the number 4 in a given list. 

def count_list_4(nums):
    count = 0
    for num in nums:
        if num == '4':
           count += 1

    return count


numbers = str(input("Enter numbers seperated by commas: "))
list1 = numbers.split(",")
print(count_list_4(list1))



