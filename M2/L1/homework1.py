medical_reason=input ("Do you have a medical reson? ")
if medical_reason=="yes":
    print("you are allowed")
elif medical_reason=="no":
    attendance=int(input ("enter your attendance:"))
    if attendance<75:
        print("you are not allowed")
    else:
            print("you are allowed")
else: print("please provide the answer only in yes or no")