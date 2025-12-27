def sum (a, b): 
    return a+b
def sub (a, b): 
    return a-b
def multiple (a, b):
    return a*b
def div (a, b):
    return a/b
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
print(f"sum of {a} and {b} is {sum(a, b)}")
print(f"multiple of {a} and {b} is {multiple(a, b)}")
print(f"div of {a} and {b} is {div(a, b)}")
print(f"sub of {a} and {b} is {sub(a, b)}")