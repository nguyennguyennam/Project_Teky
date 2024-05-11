import json


with open("data.json") as f:
    data = json.load(f)

class ItemResult:
    def __init__(self, total_price, count_item):
        self.total_price = total_price
        self.count_item = count_item

def handleItem(name_list, item):
    total_price = 0
    count_item = 0
    for data_item in data[name_list]:
        for sub_item in item:
            if sub_item == data_item['name']:
                total_price += data_item['price']
                count_item += 1
    return ItemResult(total_price, count_item)


            





