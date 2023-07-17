"""
CP1404/CP5632 - Practical
FENG YUAN
Pseudocode:

get number_of_items
while number_of_items < 0
    print Invalid number of items!
    get number_of_items

initialize total_price to 0.0
for i in range 0 to number_of_items - 1
    get price_of_item
    add price_of_item to total_price

if total_price > 100
    total_price = total_price * 0.90

print Total price for number_of_items items is total_price

"""


number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0.0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:
    total_price *= 0.90

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
