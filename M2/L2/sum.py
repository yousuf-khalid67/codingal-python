start = int(input('enter start number: '))
stop = int(input('enter stop number: '))
sum = 0
for i in range(start, stop+1):
    print(i)
    sum += i
print(f'Sum = {sum}')