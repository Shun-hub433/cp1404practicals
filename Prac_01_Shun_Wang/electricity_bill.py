print("Electricity bill estimator")


price_KWh_cents = float(input("Enter cents per kWh:"))
daily_usage = float(input("Enter daily use in kWh:"))
num_billing_days = int(input("Enter number of billing days:"))

bills =  price_KWh_cents * 0.01 * daily_usage * num_billing_days
print(f"Estimated bill: {bills:.2f}")



print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_choice = int(input("Which tariff? 11 or 31:"))
daily_usage = float(input("Enter daily use in kWh:"))
num_billing_days = int(input("Enter number of billing days:"))

if tariff_choice ==11:
    estimated_bill = daily_usage * num_billing_days * TARIFF_11
else:
    estimated_bill = daily_usage * num_billing_days * TARIFF_31

print(f"Estimated bill: ${estimated_bill:.2f}")






