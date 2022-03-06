# Write a Python program to calculate number of days between two dates.
from datetime import date
date1 = date(2022, 5, 7)
date2 = date(2025, 5, 8)
delta = date2 - date1
print(delta.days)