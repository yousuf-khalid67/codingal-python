import random
user_choice= input("Enter rock, paper, or scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")
print(f"User chose: {user_choice}")
if user_choice not in options:
    print("Invalid choice! Please choose rock, paper, or scissors.")
elif user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")
    
