def currency_converter(amount, rate):
    return amount * rate

amount = float(input("Enter the amount in the original currency: "))
rate = float(input("Enter the exchange rate to the target currency: "))
converted_amount = currency_converter(amount, rate)
print(f"The converted amount is: {converted_amount}")