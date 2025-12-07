print("Currency Converter Program")
try:
    amountGBP = float(input("Enter amount in GBP (£): "))
    #validate: amount must be between £0 and £2500
    if amountGBP <=0 or amountGBP >=2500:
        print("Invalid amount. Must be between £0 and £2500.")
        quit()
except ValueError:
    print("Invalid input")
    quit()
#currency selection
print ("\nAvailable currencies: USD,EUR,BRL,JPY,TRY")
currencyCode= input("Enter currency code: ").upper()
#validate the currency
if currencyCode not in ["USD","EUR","BRL", "JPY", "TRY"]:
    print(" Invalid currency code.")
#defining exchanging rates
exchangeRates= {
        "USD": 1.40,
        "EUR": 1.14,
        "BRL": 4.77,
        "JPY": 151.05,
        "TRY": 5.68
        }
#conversion calculation
convertedAmount = amountGBP*exchangeRates[currencyCode]
# determine fee rate
if amountGBP <= 300:
    feeRate =0.035
elif amountGBP <= 750:
    feeRate = 0.03
elif amountGBP <= 1000:
    feeRate =0.025
elif amountGBP <= 2000:
    feeRate = 0.02
else:
    feeRate = 0.015
transactionFee=amountGBP * feeRate
totalCost= amountGBP + transactionFee
#staff discount check
staffStatus = input ("Are you a member of staff? (Yes/No): ").lower()
if staffStatus=="yes":
    discount = totalCost *0.05
    totalCost =totalCost-discount
else:
        discount =0
#outputs
print("\n Transaction summary")
print(f"Amount entered:£{amountGBP:.2f}")
print(f"Converted amount: {convertedAmount:.2f} {currencyCode}")
print(f"Transaction fee: {transactionFee:.2f}")
print(f"Discount: £{discount:.2f}")
print(f"Total cost: £{totalCost:.2f}")
