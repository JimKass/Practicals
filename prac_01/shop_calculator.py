
total_price = 0

number_items = int(input('Number of items: '))
while number_items < 0:
    print('Invalid number of items!')
    number_items = int(input('Number of items: '))

for i in range(0, number_items):
    price_of_item = int(input('Price of item: '))
    while price_of_item < 0:
        print('Invalid price!')
        price_of_item = int(input('Price of item: '))
    total_price += price_of_item
if total_price > 100:
    total_price -= total_price*0.10

print('Total price for {} items is ${:.2f}'.format(number_items, total_price))
