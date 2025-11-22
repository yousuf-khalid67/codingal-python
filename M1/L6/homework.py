# Operator Precedence Demonstration

print("=== Operator Precedence in Python ===\n")

# Multiplication vs Addition
expr1 = 3 + 4 * 2
print("3 + 4 * 2 =", expr1, "(Multiplication happens before Addition)")

# Parentheses overriding precedence
expr2 = (3 + 4) * 2
print("(3 + 4) * 2 =", expr2, "(Parentheses evaluated first)")

# Exponent has higher precedence than multiply/divide
expr3 = 2 * 3 ** 2
print("2 * 3 ** 2 =", expr3, "(Exponent applied before Multiplication)")

# Unary minus has high precedence
expr4 = -3 ** 2
print("-3 ** 2 =", expr4, "(Exponent first, then unary minus → -(3²))")

expr5 = (-3) ** 2
print("(-3) ** 2 =", expr5, "(Parentheses first → (-3)²)")

# Division and multiplication have same precedence (left to right)
expr6 = 20 / 5 * 2
print("20 / 5 * 2 =", expr6, "(Left to Right evaluation)")

# Addition and subtraction same precedence (left to right)
expr7 = 10 - 3 + 2
print("10 - 3 + 2 =", expr7)

# Comparison operators
expr8 = 3 + 2 > 4
print("3 + 2 > 4 =", expr8, "(Addition before comparison)")

# Logical operators (not > and > or)
expr9 = not False or False
print("not False or False =", expr9, "(not before or)")

expr10 = not (False or False)
print("not (False or False) =", expr10)

print("\n=== End of Demonstration ===")
