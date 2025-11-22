maths=int(input("Enter your maths number : "))
mathstotal=int(input("enter maths total marks :"))
it=int(input("enter your IT marks :"))
ittotal=int(input("enter IT total marks :"))
science=int(input("enter your science marks :"))
sciencetotal=int(input("enter science total marks :"))
english=int(input("enter your english marks :"))
englishtotal=int(input("enter english total marks :"))
total=maths+it+science+english
outoff=mathstotal+ittotal+sciencetotal+englishtotal
average=total/4
percentage=(total/outoff)*100
print(f"your average marks: {average}")
print(f"your percentage is: {percentage}%")