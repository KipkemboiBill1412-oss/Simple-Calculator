from datetime import datetime

current_year = datetime.now().year

yob = int(input("What year were you born in? "))
age = current_year - yob

print(f"You are {age} years old.")
