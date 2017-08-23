
cents_per_kWh = int(input('Enter cents per kWh: '))
while cents_per_kWh < 0:
    print('Invalid Input')
    cents_per_kWh = int(input('Enter cents per kWh: '))

daily_kWh = int(input('Enter daily use in kWh: '))
while daily_kWh < 0:
    print('Invalid Input')
    daily_kWh = int(input('Enter daily use in kWh: '))

number_billing_days = int(input('Enter number of billing days: '))
while number_billing_days < 0:
    print('Invalid Input')
number_billing_days = int(input('Enter number of billing days: '))

estimated_bill = number_billing_days * daily_kWh * cents_per_kWh

print('Estimated bill: $', estimated_bill)
