medical_reason=input ("Do you have a medical reson? ")
if medical_reason=="yes":
    print("you are allowed")
else:
    attendance=int(input ("enter your attendance:"))
    if attendance<75:
        print("you are not allowed")
    else:
        print("you are allowed")