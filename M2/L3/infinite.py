print("game starts")
print("game over")
while True:
    user_input=input("do you want to continue (Y or N): ")
    if user_input=="N": 
        print("returning to home screen")
        break
    elif user_input=="Y": 
        print("level restarting")
        print("game over")
    else: 
        print("invalid input. Please try again")