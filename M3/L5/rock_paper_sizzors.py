import random
user_choice= input("Enter rock, paper, or scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")
print(f"User chose: {user_choice}")
if user_choice not in options:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    