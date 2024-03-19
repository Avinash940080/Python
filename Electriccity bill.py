def calculate_electricity_bill(units):
    if units <= 100:
        return units * 1.50
    elif units <= 200:
        return 100 * 1.50 + (units - 100) * 2.00
    elif units <= 300:
        return 100 * 1.50 + 100 * 2.00 + (units - 200) * 3.00
    else:
        return 100 * 1.50 + 100 * 2.00 + 100 * 3.00 + (units - 300) * 4.00

units_consumed = float(input("Enter the units consumed: "))
print("Electricity bill: $", calculate_electricity_bill(units_consumed))