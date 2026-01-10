age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
print(f"Your age is: {age} years.")
from datetime import date

today = date.today()
print("Today's date is", today)
print("Date components:", today.year, today.month, today.day)
print(f"Your age is: {age} years.")
