def generate_bill(amount, tax_function):
    tax = tax_function(amount)
    total = amount + tax
    return total


def tax_india(amount):
    return amount * 0.18


def tax_usa(amount):
    return amount * 0.10


def tax_uk(amount):
    return amount * 0.20


amount = float(input("Enter bill amount: "))

total_india = generate_bill(amount, tax_india)
print("Total bill (India):", total_india)

total_usa = generate_bill(amount, tax_usa)
print("Total bill (USA):", total_usa)
