def calculate_age(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age

# Example usage
if __name__ == "__main__":
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")