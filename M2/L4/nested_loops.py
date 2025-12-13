start=int(input("enter first number"))
stop=int(input("enter second number"))
for num in range(start,stop+1): 
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)