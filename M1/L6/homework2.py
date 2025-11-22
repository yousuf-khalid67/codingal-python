print("=== How Python Solves Maths ===\n")

# Multiplication happens before addition
answer1 = 3 + 4 * 2
print("3 + 4 * 2 =", answer1, "(Times first, then plus)")

# Brackets always go first
answer2 = (3 + 4) * 2
print("(3 + 4) * 2 =", answer2, "(Brackets first)")

# Powers happen before times
answer3 = 2 * 3 ** 2
print("2 * 3 ** 2 =", answer3, "(Power first)")

# Minus happens after powers
answer4 = -3 ** 2
print("-3 ** 2 =", answer4, "(Power first, then the minus)")

# Brackets change the answer
answer5 = (-3) ** 2
print("(-3) ** 2 =", answer5, "(Brackets make it positive)")

# Divide and times are same level (go left to right)
answer6 = 20 / 5 * 2
print("20 / 5 * 2 =", answer6, "(Left to right)")

# Plus and minus are same level (left to right)
answer7 = 10 - 3 + 2
print("10 - 3 + 2 =", answer7)

# Do the maths before checking > or <
answer8 = 3 + 2 > 4
print("3 + 2 > 4 =", answer8, "(Do maths first)")

# 'not' happens before 'or'
answer9 = not False or False
print("not False or False =", answer9, "(not happens first)")

# Brackets first again
answer10 = not (False or False)
print("not (False or False) =", answer10)

print("\n=== Done! ===")
