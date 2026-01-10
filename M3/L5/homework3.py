try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Error: Age cannot be negative.")
    elif age > 150:
        print("Error: Age seems unrealistic.")
    else:
        if age % 2 == 0:
            print(f"Age {age} is even.")
        else:
            print(f"Age {age} is odd.")
except ValueError:
    print("Error: Please enter a valid number for age.")