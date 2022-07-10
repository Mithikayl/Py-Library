def main():
    print("[*] Interest")
    amount = float(input("[*] Enter the amount: "))
    rate = float(input("[*] Enter the rate: "))
    years = float(input("[*] Enter the years: "))
    print("[*] The compound interest is", compound_interest(amount, rate, years))
    print("[*] The linear interest is", linear_interest(amount, rate, years))

def compound_interest(amount, rate, years):
    interest = amount * (1 + rate / 100) ** years
    return interest

def linear_interest(amount, rate, years):
    interest = amount * rate * years
    return interest
