
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input('Which tariff? 11 or 31: '))
while tariff != 11 and tariff != 31:
    print('Invalid Input')
    tariff = int(input('Which tariff? 11 or 31: '))
if tariff == 11:
    tariff_cost = TARIFF_11
else:
    tariff_cost = TARIFF_31

daily_kWh = int(input('Enter daily use in kWh: '))
while daily_kWh < 0:
    print('Invalid Input')
    daily_kWh = int(input('Enter daily use in kWh: '))

number_billing_days = int(input('Enter number of billing days: '))
while number_billing_days < 0:
    print('Invalid Input')
    number_billing_days = int(input('Enter number of billing days: '))

estimated_bill = number_billing_days * daily_kWh * tariff_cost
print('Estimated bill: ${:.2f}'.format(estimated_bill))
