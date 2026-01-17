
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


squares = [i**2 for i in range(start, end + 1)]


odd_squares = [num for num in squares if num % 2 != 0]
even_squares = [num for num in squares if num % 2 == 0]


print(f"Square values: {squares}")
print(f"Odd squares: {odd_squares}")
print(f"Even squares: {even_squares}")