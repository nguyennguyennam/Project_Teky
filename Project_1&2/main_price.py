from product import *

item_input = input('Please enter items name: ')
item_name = input('Please enter the type of an item_list: ')
item_list = item_input.split()

# Calculate total price and number of items
price_total_item = handleItem(item_name, item_list)
print(f'Total price: {price_total_item.total_price}, Number of item: {price_total_item.count_item}')

