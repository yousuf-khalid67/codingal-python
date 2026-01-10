def calculate_due_amount(total_amount, paid_amount):
    due_amount = total_amount - paid_amount
    return due_amount

# Example usage
total_amount = float(input("Enter the total bill amount: "))
paid_amount = float(input("Enter the amount paid: "))

due_amount = calculate_due_amount(total_amount, paid_amount)

print(f"The customer due amount is: ${due_amount:.2f}")
