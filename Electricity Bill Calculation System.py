def input_units():
    units = int(input("Enter units consumed: "))
    return units


def calculate_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + (units - 100) * 2.5
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4
    return bill


def generate_bill_summary(units, bill):
    print("\n--- Electricity Bill ---")
    print("Units Consumed:", units)
    print("Total Amount: ₹", bill)


units = input_units()
amount = calculate_bill(units)
generate_bill_summary(units, amount)
