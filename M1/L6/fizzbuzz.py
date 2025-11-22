num=int(input("enter a number: " ))
if num%3==0 and num%5==0:
    print("fizz buzz")
elif num%5==0:
    print("buzz")
elif num%3==0:
    print("fizz")
else:
    print(num)